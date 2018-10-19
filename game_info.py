import time
import random
from user_g import user_agent
import redis
import requests
import json
from lxml import etree
redis_c_15 = redis.Redis(host='localhost', port=6379, decode_responses=True, db=15)


def get_ip():
    redis_zheng = redis.Redis(host='118.31.221.53', port=6379, password='zheng123666', db=0)  # 代理
    ip_list = str(redis_zheng.get('ips_pools'), encoding="utf-8").split(';')
    ip = random.choice(ip_list)
    proxy_temp = {"http": ip}
    return proxy_temp

def anay_data(t1):
    t_n = int(t1.split("-")[0])
    t_m = int(t1.split("-")[1])
    t_d = int(t1.split("-")[2])
    if t_m in [1, 3, 5, 7, 8, 10, 12]:
        if t_d == 31:
            if t_m == 12:
                return str(t_n+1) + '-' + str(1) + '-' + '1'
            return str(t_n) + '-' + str(t_m+1) + '-' + '1'
        else:
            return str(t_n) + '-' + str(t_m) + '-' + str(t_d + 1)
    if t_m in [4, 6, 9, 11]:
        if t_d == 30:
            return str(t_n) + '-' + str(t_m + 1) + '-' + '1'
        else:
            return str(t_n) + '-' + str(t_m) + '-' + str(t_d + 1)
    if t_m == 2:
        if t_n % 4 == 0:
            if t_d == 29:
                return str(t_n) + '-' + str(t_m + 1) + '-' + '1'
            else:
                return str(t_n) + '-' + str(t_m) + '-' + str(t_d + 1)
        else:
            if t_d == 28:
                return str(t_n) + '-' + str(t_m + 1) + '-' + '1'
            else:
                return str(t_n) + '-' + str(t_m) + '-' + str(t_d + 1)


def anay_time(game_time):
    t = game_time.split('T')
    t1 = t[0]
    t2 = int(t[1][:-1].split(":")[0]) + 8
    if t2 >= 24:
        t2 = t2 - 24
        t1 = anay_data(t1)
    t2 = str(t2) + ":" + t[1][:-1].split(":")[1]
    b = t1 + ' ' + t2
    timeArray = time.strptime(b, "%Y-%m-%d %H:%M")  # 转为数组
    timestamp = time.mktime(timeArray)
    return int(timestamp)


def get_game_info(href):
    game_id = href.split('/')[-1]
    # 比赛信息
    url = 'http://www.espn.com/nba/matchup?gameId=' + game_id
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
    }
    response = requests.get(url, headers=headers)
    data = response.text
    res = etree.HTML(data)
    t1 = res.xpath('//span[@data-behavior="date_time"]/@data-date')[0]
    try:
        game_time = anay_time(t1)
    except:
        game_time = 1111111111
        redis_c_15.set(game_id, url)
    try:
        changguang = res.xpath('//div[@class="caption-wrapper"]/text()|//div[@class="game-location"]/text()')[0].strip()  # 场馆
    except:
        changguang = '0'
    try:
        dizhi = res.xpath('//li[@class="icon-font-before icon-location-solid-before"]/text()')[0].strip()  # 地址
    except:
        dizhi = '0'
    try:
        ren_1 = res.xpath('//div[@class="game-info-note capacity"]/text()')[0].split(' ')[1]  # 到场人数
    except:
        ren_1 = '0'
    try:
        dao_lv = res.xpath('//span[@class="percentage"]/text()')[0]  # 到场率
    except:
        dao_lv = '0'
    try:
        ren_2 = res.xpath('//div[@class="game-info-note capacity"]/text()')[1].split(' ')[1]  # 可容纳人数
    except:
        ren_2 = '0'
    try:
        caipan = res.xpath('//span[@class="game-info-note__content"]/text()')[0]  # 裁判
    except:
        caipan = '0'
    game_info = str(game_time)+"^^"+changguang+'^^'+dizhi+'^^'+ren_1+'^^'+dao_lv+'^^'+ren_2+'^^'+caipan
    return game_info


if __name__ == '__main__':
    href = '//www.espn.com/nba/boxscore/_/id/400974438'
    get_game_info(href)



