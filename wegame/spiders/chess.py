import scrapy
import json
import logging
from wegame.data.model import Sesssion, Chess, Items, update_or_create
from wegame.api import get_chess_info, get_items_info

class ChessSpider(scrapy.Spider):
    name = 'chess'
    allowed_domains = ['lol.qq.cn', 'wegame.com.cn']
    # start_urls = ['https://m.wegame.com.cn/api/mobile/lua/proxy/index/mwg_tft_proxy//get_total_tier_rank_list']

    def start_requests(self):
        yield self.request(500 * 20)

    def request(self, offset):

        return get_chess_info(
            callback=self.parse
        )

    def request_items(self):
        return get_items_info(
            callback=self.parse_items
        )


    def parse(self, response):
        result = json.loads(response.text)
        version = result.get('version')
        data = result.get('data', [])
        session = Sesssion()
        try:
            for obj in data:
                id = obj.get('chessId')
                id = int(id)
                chess_schema = {
                    'version': version,
                    'name': obj.get('title'),
                    'tft_id': obj.get('TFTID'),
                    'armor': obj.get('armor'),
                    'attack': obj.get('attack'),
                    'attack_data': obj.get('attackData'),
                    'attack_mag': obj.get('attackMag'),
                    'attack_range': obj.get('attackRange'),
                    'attack_speed': obj.get('attackSpeed'),
                    'crit': obj.get('crit'),
                    'display_name': obj.get('displayName'),
                    'illustrate': obj.get('illustrate'),
                    'job_ids': obj.get('jobIds'),
                    'jobs': obj.get('jobs'),
                    'life': obj.get('life'),
                    'life_data': obj.get('lifeData'),
                    'life_mag': obj.get('lifeMag'),
                    'magic': obj.get('magic'),
                    'image': obj.get('name'),
                    'original_image': obj.get('originalImage'),
                    'price': obj.get('price'),
                    'pro_status': obj.get('proStatus'),
                    'race_ids': obj.get('raceIds'),
                    'races': obj.get('races'),
                    'rec_equip': obj.get('recEquip'),
                    'skill_detail': obj.get('skillDetail'),
                    'skill_image': obj.get('skillImage'),
                    'skill_introduce': obj.get('skillIntroduce'),
                    'skill_name': obj.get('skillName'),
                    'skill_type': obj.get('skillType'),
                    'spell_block': obj.get('spellBlock'),
                    'start_magic': obj.get('startMagic'),
                    'synergies': obj.get('synergies'),
                }
                update_or_create(session, Chess, id=id, defaults=chess_schema)
        except Exception as e:
            print(e)
        session.commit()
        
        # yield self.request_items()


    def parse_items(self, response):
        result = json.loads(response.text)
        version = result.get('version')
        data = result.get('result', {})
        data = data.get('equip', [])
        session = Sesssion()
        try:
            for obj in data:
                id = obj.get('id')
                id = int(id)
                chess_schema = {
                    'name': obj.get('name'),
                    'property': obj.get('property'),
                }
                update_or_create(session, Items, id=id,defaults=chess_schema)
        except Exception as e:
            print(e)
        session.close()