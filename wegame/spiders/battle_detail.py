import scrapy
import json
import logging
import datetime
from wegame.data.model import Sesssion, Battle, BattleDetail, BattleChess, User, update_or_create, select_or_insert
from wegame.api import get_battle_detail

class BattleDetailSpider(scrapy.Spider):
    name = 'battle_detail'
    allowed_domains = ['wegame.com.cn']
    battle = []
    # start_urls = ['https://m.wegame.com.cn/api/mobile/lua/proxy/index/mwg_tft_proxy//get_total_tier_rank_list']

    def __init__(self, *args, **kwargs):
        self.session = Sesssion()

    def start_requests(self):
        self.battle = self.session.query(Battle).filter_by().all()
        self.index = 0
        self.battle_len = len(self.battle)
        # yield self.request(290)
        yield self.request(0)

    def request(self, index):
        
        if self.battle_len > index:
            obj = self.battle[index]
            area_id = obj.area_id
            battle_id =  obj.id
            slol_id = 'b7y00g4'

            return get_battle_detail(
                callback=self.parse,
                body=json.dumps({
                    "area_id": area_id,
                    "battle_id": battle_id,
                    "slol_id": slol_id,
                })
            )

    def parse(self, response):
        result = json.loads(response.text)
        body = json.loads(response.request.body)
        battle_id = body.get('battle_id')
        area_id = body.get('area_id')
        session = self.session

        obj = result['data']['battle_detail']
        for player in obj.get('player_list', []):
            rank_info = player.get('rank_info')
            try:
                user_instance, created = select_or_insert(session, User, slol_id=player.get('slol_id'), area_id=body.get('area_id'), defaults={
                    'name': player.get('name'),
                    'icon_id': player.get('icon_id'),
                    'tier': rank_info.get('tier'),
                    'rank': rank_info.get('queue')
                })
                user_id = user_instance.id
                battle_id = obj.get('battle_id')
                battle_schema = {
                    'gold_left': player.get('gold_left', ''),
                    'health': player.get('health', ''),
                    'last_round': player.get('last_round', ''),
                    'level': player.get('level', ''),
                    'players_eliminated': player.get('players_eliminated', ''),
                    'show_last_round': player.get('show_last_round', ''),
                    'snapshot_time': player.get('snapshot_time', ''),
                    'snapshot_url': player.get('snapshot_url', ''),
                    'time_eliminated': str(player.get('time_eliminated', '')),
                    'total_damage_to_players': player.get('total_damage_to_players', ''),
                    'total_trait_num': player.get('total_trait_num', ''),
                    'duration': obj.get('duration', ''),
                    'battle_ranking': obj.get('battle_ranking', 0),
                }
                battle_detail_instance, created = update_or_create(session, BattleDetail, battle_id=battle_id, user_id=user_id,defaults=battle_schema)
                # 首先删除本场比赛的所有相关信息
                self.session.query(BattleChess).filter_by(battle_detail_id=battle_detail_instance.id).delete()
                self.session.commit()
                # 将棋子和阵容插入 棋子表
                chess_list = []
                for chess in player.get("chess_list", []):
                    chess_list.append(
                        BattleChess(battle_detail_id=battle_detail_instance.id, hero_id=chess.get('hero_id'), price=chess.get('price', -1), star=chess.get('star', -1), items=chess.get('items', None))
                    )
                self.session.add_all(chess_list)
                self.session.commit()
            except Exception as e:
                print(e)
        battle_instance = self.session.query(Battle).filter_by(id=battle_id, area_id=area_id).first()
        battle_instance.state = 1
        self.session.commit()
        logging.info(f'battle_id: {battle_id} area_id: {area_id} 更新完毕')
        self.index += 1
        yield self.request(self.index)

        
        
