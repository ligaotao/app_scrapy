import scrapy
import json

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
                'tgp_ticket': '087A274DEAEAA17D130E98CAF6594556EB9476A8C19D75FF3A9E464702D292322CDA9EB5A9B762D62AED242192E860BB864C4A27B0E6EABEA89BF1C38DCA5D07E9DBC1AC6F1D328F8FD0F0880B46DC20CF613B161D8E76EF0F226AD7FA7D5AE778F7D44EB264A2A0AEF18858E2973D3DF70976DB66AC0B43577FF6CBA9A233B0',
                'platform': 'qq',
                'account': '1052036710',
                'skey': 'MQTl0Lrrcg',
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
        print(response)
        pass
