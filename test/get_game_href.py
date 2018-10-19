import time
import re
import requests
import json
from lxml import etree


def get_game_info():
    # 比赛信息
    url = 'http://www.espn.com/nba/team/schedule/_/name/ind/year/2003/seasontype/3'
    headers = {
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }
    response = requests.get(url, headers=headers)
    data = response.text
    # res = etree.HTML(data)
    href_list = re.findall(r'class="score"><a href="(.*?)"', data)
    print(href_list)


if __name__ == '__main__':
    get_game_info()

