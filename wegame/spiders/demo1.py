import scrapy
import json
from wegame.data.model import Sesssion, User, update_or_create

class Demo1Spider(scrapy.Spider):
    name = 'demo1'
    allowed_domains = ['wegame.com.cn']
    # start_urls = ['https://m.wegame.com.cn/api/mobile/lua/proxy/index/mwg_tft_proxy//get_total_tier_rank_list']

    def start_requests(self):
        yield self.reauest(0)

    def reauest(self, offset):
        LOLServer = """
            t: "艾欧尼亚  电信", v: "1", status: "1"
            t: "比尔吉沃特  网通", v: "2", status: "1"
            t: "祖安 电信", v: "3", status: "1"
            t: "诺克萨斯  电信", v: "4", status: "1"
            t: "德玛西亚 网通", v: "6", status: "1"
            t: "班德尔城 电信", v: "5", status: "1"
            t: "皮尔特沃夫 电信", v: "7", status: "1"
            t: "战争学院 电信", v: "8", status: "1"
            t: "弗雷尔卓德 网通", v: "9", status: "1"
            t: "巨神峰 电信", v: "10", status: "1"
            t: "雷瑟守备 电信", v: "11", status: "1"
            t: "无畏先锋 网通", v: "12", status: "1"
            t: "裁决之地 电信", v: "13", status: "1"
            t: "黑色玫瑰 电信", v: "14", status: "1"
            t: "暗影岛 电信", v: "15", status: "1"
            t: "钢铁烈阳 电信", v: "17", status: "1"
            t: "恕瑞玛 网通", v: "16", status: "1"
            t: "水晶之痕 电信", v: "18", status: "1"
            t: "教育网专区", v: "21", status: "1"
            t: "影流 电信", v: "22", status: "1"
            t: "守望之海 电信", v: "23", status: "1"
            t: "扭曲丛林 网通", v: "20", status: "1"
            t: "征服之海 电信", v: "24", status: "1"
            t: "卡拉曼达 电信", v: "25", status: "1"
            t: "皮城警备 电信", v: "27", status: "1"
            t: "巨龙之巢 网通", v: "26", status: "1"
            t: "男爵领域 全网络", v: "30", status: "1"
            t: "均衡教派", v: "19", status: "1"
            """
        headers = {
            'host': 'm.wegame.com.cn',
            'accept': 'application/json',
            'content-type':	'application/json; charset=utf-8',
            'User-Agent': 'okhttp/3.11.0'
        }
        return scrapy.Request(
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
                "area_id": 9,
                "offset": offset,
                "limit": 100
            })
        )

    def parse(self, response):
        result = json.loads(response.text)
        body = json.loads(response.request.body)
        session = Sesssion()
        try:
            for obj in result['data']['player_list']:
                obj['area_id'] = body['area_id']
                update_or_create(session, User, slol_id=obj.get('slol_id'),defaults=obj)
        except Exception as e:
            print(e)
        session.close()
        if result['data']['next_offset']:
            print(result['data']['next_offset'] / 20)
            yield self.reauest(result['data']['next_offset'])
