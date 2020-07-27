import scrapy
import json
import logging
import datetime
from wegame.data.model import Sesssion, Battle, BattleDetail, User,update_or_create, select_or_insert
from wegame.api import get_battle_list
from scrapy_redis.spiders import RedisSpider


class BattleListSpider(RedisSpider):
    name = 'battle_list'
    # allowed_domains = ['wegame.com.cn']
    # start_urls = ['https://m.wegame.com.cn/api/mobile/lua/proxy/index/mwg_tft_proxy//get_total_tier_rank_list']

    redis_key = 'battle_user'

    def __init__(self):
        self.session = Sesssion()
        today = datetime.datetime.now()
        self.start_time = datetime.datetime(today.year, today.month, today.day)
        self.last_time = self.start_time - datetime.timedelta(days=10)
        self.user = None

    def make_request_from_data(self, data):
        return self.request(area_id=9, slol_id=str(data, "utf-8"), offset=0)


    # def start_requests(self):
    #     today = datetime.datetime.now()
    #     users = self.session.query(User).filter(User.area_id==9).order_by(User.id).limit(100)
    #     # last_battle = self.session.query(Battle).join(BattleDetail).join(User).filter(User.slol_id=='b7y00g4', User.area_id==9).order_by(Battle.start_time.desc()).first()
    #     # self.last_battle = last_battle
    #     self.start_time = datetime.datetime(today.year, today.month, today.day)
    #     self.last_time = self.start_time - datetime.timedelta(days=10)

    #     for user in users:
    #         yield self.user_list(user=user)

    def user_list(self, user=None):
        return self.request(user=user, offset=0)

    def request(self, area_id=9, slol_id=None, offset=0):
        return get_battle_list(
            callback=self.parse,
            body=json.dumps({
                "area_id": area_id,
                "offset": offset,
                "filter_types": [],
                "slol_id": slol_id,
                "topn": 0
            })
        )

    def parse(self, response):
        result = json.loads(response.text)
        body = json.loads(response.request.body)
        area_id = body.get('area_id')
        session = Sesssion()
        slol_id = body.get('slol_id')
        start_time = None
        try:
            for obj in result['data']['battle_list']:
                start_time = datetime.datetime.fromtimestamp(obj.get('start_time'))
                battle_schema = {
                    'game_mode': obj.get('game_mode'),
                    'start_time': start_time,
                    'area_id': area_id,
                    'slol_id': slol_id
                }
                if self.start_time < start_time:
                    # 如果比赛的时间 比 爬取的开始时间晚则本条数据不进行爬取，放到下次再爬
                    continue
                if self.last_time >= start_time:
                    # 已经更新到历史数据 触发终止条件
                    result['data']['next_offset'] = -1
                select_or_insert(session, Battle, id=obj.get('battle_id'),defaults=battle_schema)
        except Exception as e:
            print(e)
        session.close()
        if result['data']['next_offset'] != -1:
            logging.info(f"""当前用户：{user.name} 当前页码：{result['data']['next_offset'] / 10}""")
            yield self.request(area_id=area_id, slol_id=slol_id, offset=result['data']['next_offset'])
        else:
            logging.info(f"""当前用户：{slol_id} 结束""")
