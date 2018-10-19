import random

import requests
import json
from lxml import etree
from translate import translate


def get_wenzi(href):
    game_id = href.split('/')[-1]
    # 比赛的文字直播部分
    url = 'http://www.espn.com/nba/playbyplay?gameId=' + game_id
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
    }
    response = requests.get(url, headers=headers)
    data = response.text
    res = etree.HTML(data)

    home_name = res.xpath('//div[@class="team home"]//span[@class="short-name"]/text()')[0]  # 主队名
    away_name = res.xpath('//div[@class="team away"]//span[@class="short-name"]/text()')[0]  # 客队名
    home_score = res.xpath('//div[@class="score icon-font-before"]/text()')[0]  # 主队得分
    away_score = res.xpath('//div[@class="score icon-font-after"]/text()')[0]  # 客队得分
    q_1 = res.xpath('//table[@id="linescore"]//td[2]/text()')
    q_2 = res.xpath('//table[@id="linescore"]//td[3]/text()')
    q_3 = res.xpath('//table[@id="linescore"]//td[4]/text()')
    q_4 = res.xpath('//table[@id="linescore"]//td[5]/text()')
    try:
        q_4_h = q_4[1]
    except:
        q_4_h = '-'
    try:
        q_4_a = q_4[0]
    except:
        q_4_a = '-'
    home_q_s = q_1[1] + '^^' + q_2[1] + '^^' + q_3[1] + '^^' + q_4_h + '^^' + home_score  # 小节的比分
    away_q_s = q_1[0] + '^^' + q_2[0] + '^^' + q_3[0] + '^^' + q_4_a + '^^' + away_score

    ss = home_name + '^^' + home_q_s + '^#^' + away_name + '^^' + away_q_s

    querter_list = res.xpath('//div[@id="gamepackage-play-by-play"]//li[@class="accordion-item"]')  # 4小节
    wen = ''
    for querter in querter_list:
        tr_list = querter.xpath('.//tr')[1:]
        te = ''
        for i in tr_list:
            time = i.xpath('./td[1]/text()')[0]  # 倒计时的时间
            try:
                logo = i.xpath('./td[2]/img/@src')[0]  # 队伍的logo
            except:
                logo = '-'
            text = i.xpath('./td[3]/text()')[0]  # 内容
            score = i.xpath('./td[4]/text()')[0]  # 比分
            text = translate(text)
            ttext = time+'^^'+logo+'^^'+text+'^^'+score
            te += ttext + '&&'
        wen += te + '###'
    return ss + '^###^' + wen


if __name__ == '__main__':
    href = '//www.espn.com/nba/boxscore/_/id/400974438'
    get_wenzi(href)


