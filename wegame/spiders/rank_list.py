import scrapy
import json
import logging
from wegame.data.model import Sesssion, User, update_or_create
from wegame.api import get_user_rank_list

class RankListSpider(scrapy.Spider):
    name = 'rank_list'
    allowed_domains = ['wegame.com.cn']
    # start_urls = ['https://m.wegame.com.cn/api/mobile/lua/proxy/index/mwg_tft_proxy//get_total_tier_rank_list']

    def start_requests(self):
        yield self.reauest(500 * 20)

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

        return get_user_rank_list(
            callback=self.parse,
            body=json.dumps({
                "area_id": 9,
                "offset": offset
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
        if result['data']['next_offset'] != -1:
            logging.info(f"""当前页码{result['data']['next_offset'] / 20}""")
            yield self.reauest(result['data']['next_offset'])
        else:
            logging.info(f"""当前服务器数据结束""")
