import scrapy
import json
import logging
import datetime
from wegame.data.model import Sesssion, Battle, update_or_create
from wegame.api import get_battle_list

class BattleListSpider(scrapy.Spider):
    name = 'battle_list'
    allowed_domains = ['wegame.com.cn']
    # start_urls = ['https://m.wegame.com.cn/api/mobile/lua/proxy/index/mwg_tft_proxy//get_total_tier_rank_list']

    def start_requests(self):
        yield self.request(290)

    def request(self, offset):
        return get_battle_list(
            callback=self.parse,
            body=json.dumps({
                "area_id": 9,
                "offset": offset,
                "filter_types": [],
                "slol_id": "b7y00g4",
                "topn": 0
            })
        )

    def parse(self, response):
        result = json.loads(response.text)
        body = json.loads(response.request.body)
        area_id = body.get('area_id')
        session = Sesssion()
        try:
            for obj in result['data']['battle_list']:
                battle_schema = {
                    'game_mode': obj.get('game_mode'),
                    'start_time': datetime.datetime.fromtimestamp(obj.get('start_time')),
                    'area_id': area_id
                }
                update_or_create(session, Battle, id=obj.get('battle_id'),defaults=battle_schema)
        except Exception as e:
            print(e)
        session.close()
        if result['data']['next_offset'] != -1:
            logging.info(f"""当前页码{result['data']['next_offset'] / 10}""")
            yield self.request(result['data']['next_offset'])
        else:
            logging.info(f"""当前服务器数据结束""")
