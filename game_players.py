import random
import time

import redis
import requests
import json
from lxml import etree

def get_ip():
    redis_zheng = redis.Redis(host='118.31.221.53', port=6379, password='zheng123666', db=0)  # 代理
    ip_list = str(redis_zheng.get('ips_pools'), encoding="utf-8").split(';')
    ip = random.choice(ip_list)
    proxy_temp = {"http": ip}
    return proxy_temp


def get_players_info(href):
    game_id = href.split('name/')[-1].split('/')[0]
    # 比赛信息
    url = 'http://www.espn.com/nba/team/roster/_/name/' + game_id
    headers = {
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }
    response = requests.get(url, headers=headers)
    data = response.text
    res = etree.HTML(data)
    tr_list = res.xpath('.//table[@class="tablehead"]//tr')[2:-1]
    data_t = ''
    for tr in tr_list:
        num = tr.xpath('.//td[1]/text()')[0]
        name = tr.xpath('.//td[2]/text()|.//td[2]/a/text()')[0]
        h = tr.xpath('.//td[2]/a/@href')[0]
        try:
            pos = tr.xpath('.//td[3]/text()')[0]
            if len(pos) == 1:
                pos = '-'
        except:
            pos = '-'
        try:
            age = tr.xpath('.//td[4]/text()')[0]
            if len(age) == 1:
                age = '-'
        except:
            age = '-'
        try:
            ht = tr.xpath('.//td[5]/text()')[0]
            if len(ht) == 1:
                ht = '-'
        except:
            ht = '-'
        try:
            wt = tr.xpath('.//td[6]/text()')[0]
            if len(wt) == 1:
                wt = '-'
        except:
            wt = '-'
        try:
            coll = tr.xpath('.//td[7]/text()')[0]
            if len(coll) == 1:
                coll = '-'
        except:
            coll = '-'
        try:
            salary = tr.xpath('.//td[8]/text()')[0]
            if len(salary) == 1:
                salary = '-'
        except:
            salary = '-'
        data_p = num + '^^' + name + '^^' + h + '^^' + pos + '^^' + age + '^^' + ht + '^^' + wt + '^^' + coll + '^^' + salary
        data_t += data_p + '&&'
    return data_t


if __name__ == '__main__':
    href = '//www.espn.com/nba/boxscore/_/id/400978765'
    get_players_info(href)



