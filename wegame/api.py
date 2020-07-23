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
        'tgp_ticket': '0999C9F177B2C870C5724899E1057E5D26DEAE34013BB8D9EE6A6A77952A982863B50C88AA17B594BA5E9D5B9AA08D6A8B8043445313BB1A7DDDA89576F4EB3ACDE78BF7F2064C89C6A5E6C521162B77EB19CE8BBEDCF5F1FD7B0DCA6FB394778078B40C3B3AC6C784ABB4A97C467C2E9140EC20E0D9DB7A78F6AE531ECC8F59',
        'platform': 'qq',
        'account': '1052036710',
        'skey': 'MMNwPP2l9F',
        'mac': '92f2b852ec1bf9dd',
        'machine_type': 'OPPO+R17+Pro',
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













