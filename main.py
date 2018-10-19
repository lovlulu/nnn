import re
import time
from loger_ma import LoggerManager
import redis
import threading
from lxml import etree
import requests
import random
from cuo_list import data_list as cuo_data_list

from game_info import get_game_info
from game_stats import get_game_stats
from game_wenzi_zhibo import get_wenzi
from game_players import get_players_info
logger = LoggerManager.get('nba')
logger_url = LoggerManager.get('nba_url')

redis_c_12 = redis.Redis(host='localhost', port=6379, decode_responses=True, db=15)
redis_c_1 = redis.Redis(host='localhost', port=6379, decode_responses=True, db=0)  # 存放比赛了 URl quchong


def set_redis(key, data):
    redis_c_12.rpush(key, data)


def get_href(name):  # 点击处理
    h = {'Seattle': 'http://www.espn.com/nba/team/_/name/okc',
         'New Jersey': 'http://www.espn.com/nba/team/_/name/bkn',
         'New Orleans': 'http://www.espn.com/nba/team/_/name/no',
         'Charlotte': 'http://www.espn.com/nba/team/_/name/cha'
    }
    return h[name]


def url_lt(u_l):
    u_list = list()
    u_list.append('www.espn.com/nba/hollinger/teamstats/_/year/2018')
    for u in u_l:
        if u not in u_list:
            u_list.append(u)
    return u_list


def get_key(key):  # 判断数据存在
    result = redis_c_12.keys()
    if key in result:
        return True
    else:
        return False


def get_url(key):
    result = redis_c_1.get(key)
    if result:
        return True
    else:
        redis_c_1.set(key, key)
        return False


def get_game_data(key, url):
    try:
        print(url)
        game_info = get_game_info(url)
        game_stats = get_game_stats(url)
        game_wenzi = get_wenzi(url)
        g_data = url.split('/')[-1] + '^^^' + game_info + '^^^' + game_stats + '^^^' + game_wenzi
        set_redis(key, g_data)
        print(g_data)
    except Exception as e:
        logger.info(e)
        logger.info(key)
        logger.info(url)


# def get_href_list(key, i, url):
#     result = get_key(key)
#     if not result:
#         if 'schedule' not in url:
#             print('出现错误连接--',url)
#             url = 'http://www.espn.com/nba/team/schedule/_' + url.split('_')[1]
#         url_result = ''
#         if not url_result:
#             # players_in = get_players_info(url)
#             headers = {
#                 "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
#             }
#             response = requests.get(url, headers=headers)
#             data = response.text
#             # set_redis(key, i)
#             # set_redis(key, players_in)
#             href_list = re.findall(r'class="score"><a href="(.*?)"', data)  # 该赛季 进行的所有比赛
#             print(url,'赛季比赛数量---',len(href_list))
#             if href_list:
#                 for url in href_list:
#                     threading.Thread(target=get_game_data, args=(key, url)).start()
#                     time.sleep(0.2)
#             else:
#                 logger_url.info(key)
#                 logger_url.info(url)
#     else:
#         print('数据存在')


# def get_game():
#         da = ['2016^^Minnesota^^2', 'http://www.espn.com/nba/team/schedule/_/name/min/year/2016/seasontype/2']
#         i = '1'
#         key = da[0]
#         href_n = da[1]  # 常规赛
#
#         print(key)
#         get_href_list(key, i, href_n)
#         time.sleep(1)


if __name__ == '__main__':
    da = ['2005^^Sacramento^^3', '//www.espn.com/nba/recap/_/id/250429023']
    key = da[0]
    url = da[1]  # 常规赛
    # get_game_data(key, url)
    pass
