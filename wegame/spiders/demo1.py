import scrapy
import json
from wegame.data.model import Sesssion, User

class Demo1Spider(scrapy.Spider):
    name = 'demo1'
    allowed_domains = ['wegame.com.cn']
    # start_urls = ['https://m.wegame.com.cn/api/mobile/lua/proxy/index/mwg_tft_proxy//get_total_tier_rank_list']

    def start_requests(self):
        headers = {
            'host': 'm.wegame.com.cn',
            'accept': 'application/json',
            'content-type':	'application/json; charset=utf-8',
            'User-Agent': 'okhttp/3.11.0'
        }
        yield scrapy.Request(
            method='POST',
            cookies={
                'app_id': '10001',
                'tgp_id': '27580710',
                'tgp_ticket': '517163FA7D97936823827C48AB99344A062166E349F4426682C85795B5E6CB709408366B91C3B4B82CCE65A171E45A97B6B2BE86ABA07A9D001A9E7D82CA8E30B1A5EDC990AD9C9C2F580D005A41DC2C2941F17EC8230BA91A1E1CB5ED3847E1EF9B1CCF86B516F5877407972B62B98143C7FADDF1905EC07FF1354294F73197',
                'platform': 'qq',
                'account': '1052036710',
                'skey': 'MkscVEBnSz',
                'mac': '92f2b852ec1bf9dd',
                'machine_type': 'OPPO+R17+Pro',
                'channel_number': '10111',
                'app_version': '1050503002',
                'client_type': '601'
            },
            url='https://m.wegame.com.cn/api/mobile/lua/proxy/index/mwg_tft_proxy//get_total_tier_rank_list',
            headers=headers,
            callback=self.parse,
            body=json.dumps({
                "area_id": 1,
                "offset": 20
            })
        )

    def parse(self, response):
        result = json.loads(response.text)
        session = Sesssion()
        try:
            for obj in result['data']['player_list']:
                session.add(User(slol_id=obj.get("slol_id", '') ,name=obj.get("name", '') ,level=obj.get("level", '') ,ranking=obj.get("ranking", '') ,league_points=obj.get("league_points", '') ,rank=obj.get("rank", '') ,icon_id=obj.get("icon_id", '') ,tier=obj.get("tier", '') ))
                session.commit()
        except Exception as e:
            print(e)
        session.close()
        pass
