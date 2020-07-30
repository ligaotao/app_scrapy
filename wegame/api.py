from scrapy import Request

USER_RANK_LIST = 'https://m.wegame.com.cn/api/mobile/lua/proxy/index/mwg_tft_proxy//get_total_tier_rank_list'
USER_GAME_INFO = 'https://m.wegame.com.cn/api/mobile/lua/proxy/index/mwg_tft_proxy/get_user_game_info'
USER_BATTLE_LIST = 'https://m.wegame.com.cn/api/mobile/lua/proxy/index/mwg_tft_proxy//get_user_battle_list'
USER_BATTLE_DETAIL = 'https://m.wegame.com.cn/api/mobile/lua/proxy/index/mwg_tft_proxy/get_battle_detail'
CHESS_INFO = 'https://game.gtimg.cn/images/lol/act/img/tft/js/chess.js'
ITEMS_INFO = 'https://act.wegame.com.cn/rpc/Chess/Info/getAllEquipCompound?season=s3&uuid=fa06751e-a446-48cf-97ed-214de4afe7a0&appid=10001&g_tk=1595491786&sign=c36a25435b28dda30b709fbeba85c389'

COOKIES = {
        'app_id': '10001',
        'tgp_id': '27580710',
        'tgp_ticket': '58BBFA9DAC8B153245B5B2CB285A64D389E2A9D60B167AC9EB0DC8A17E566DA187E356AB0153804359E6B4748FAEE89697F5F485F49351ED4DC8292C1D6BE634D8B363CC6AAC541A31644F70539639BA8F755A7F6F698644BFB51161C74CDA29F236B881B0E2499AA91BA95847194FD9214B57C80AC7DC8108847BBE1524BD03',
        'platform': 'qq',
        'account': '1052036710',
        'skey': 'McqCNIjlLr',
        'mac': '92f2b852ec1bf9dd',
        'machine_type': 'MI+9',
        'channel_number': '10111',
        'app_version': '1050524013',
        'client_type': '601'
    }


def get_user_rank_list(**kwargs):
    """
      params  {
            "area_id": 1,
            "offset": 0
        }
    """
    return Request(
        method='POST',
        url=USER_RANK_LIST,
        cookies=COOKIES,
        headers = {
            'host': 'm.wegame.com.cn',
            'accept': 'application/json',
            'content-type':	'application/json; charset=utf-8',
            'User-Agent': 'okhttp/3.11.0'
        },
        **kwargs
    )

def get_battle_list(**kwargs):
    """
      params  {
        "area_id": 1,
        "filter_types": [],
        "offset": 0,
        "slol_id": "3xvLYmj0q3R",
        "topn": 0
    }
    """
    return Request(
        method='POST',
        url=USER_BATTLE_LIST,
        cookies=COOKIES,
        headers = {
            'host': 'm.wegame.com.cn',
            'accept': 'application/json',
            'content-type':	'application/json; charset=utf-8',
            'User-Agent': 'okhttp/3.11.0'
        },
        **kwargs
    )

def get_battle_detail(**kwargs):
    """
      params  {
            "area_id": 1,
            "battle_id": 5081765041,
            "slol_id": "3xvLYmj0q3R"
        }
    """
    return Request(
        method='POST',
        url=USER_BATTLE_DETAIL,
        cookies=COOKIES,
        headers = {
            'host': 'm.wegame.com.cn',
            'accept': 'application/json',
            'content-type':	'application/json; charset=utf-8',
            'User-Agent': 'okhttp/3.11.0'
        },
        **kwargs
    )


def get_chess_info(**kwargs):
    """
      params  {
            "area_id": 1,
            "battle_id": 5081765041,
            "slol_id": "3xvLYmj0q3R"
        }
    """
    return Request(
        method='GET',
        url=CHESS_INFO,
        headers = {
            'Referer': 'https://lol.qq.com/tft/',
            # 'accept': 'application/json',
            # 'content-type':	'application/x-javascript; charset=utf-8',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
        },
        **kwargs
    )

def get_items_info(**kwargs):
    return Request(
        method='GET',
        url=ITEMS_INFO,
        cookies=COOKIES,
        headers = {
            'host': 'm.wegame.com.cn',
            'accept': 'application/json',
            'content-type':	'application/json; charset=utf-8',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; OPPO R17 Pro Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 Hera(version/2.0.0) micromessenger'
        },
        **kwargs
    )













