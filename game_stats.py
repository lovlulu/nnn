import requests
import json
import threading
from lxml import etree
from plays_stats import get_fen_lei
'''
队伍的技术统计
采集球员信息
'''


def get_players_stats(url):
    pass
    # threading.Thread(target=get_fen_lei, args=(url,)).start()  # 采集球员信息


def get_game_stats(href):
    # 队伍的技术统计
    game_id = href.split('/')[-1]
    url = 'http://www.espn.com/nba/boxscore?gameId=' + game_id
    headers = {
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }
    response = requests.get(url, headers=headers)
    data = response.text
    res = etree.HTML(data)
    total_stats_list = ''
    tbody_list = res.xpath('//div[@class="col column-one gamepackage-away-wrap"]//table[@class="mod-data"]//tbody')  # 客队
    stats_away_list = ''
    tr_list = tbody_list[0].xpath('.//tr')  # 首发阵容  away
    for tr in tr_list:
        if len(tr.xpath('./td')) != 2:
            name = tr.xpath('./td/a/span[1]/text()')[0]
            player_href = tr.xpath('./td/a/@href')[0]
            get_players_stats(player_href)
            min_t = tr.xpath('./td[2]/text()')[0]
            fg = tr.xpath('./td[3]/text()')[0]
            pt_3 = tr.xpath('./td[4]/text()')[0]
            ft = tr.xpath('./td[5]/text()')[0]
            oreb = tr.xpath('./td[6]/text()')[0]
            dreb = tr.xpath('./td[7]/text()')[0]
            reb = tr.xpath('./td[8]/text()')[0]
            ast = tr.xpath('./td[9]/text()')[0]
            stl = tr.xpath('./td[10]/text()')[0]
            blk = tr.xpath('./td[11]/text()')[0]
            t_o = tr.xpath('./td[12]/text()')[0]
            pf = tr.xpath('./td[13]/text()')[0]
            jia_jian = tr.xpath('./td[14]/text()')[0]
            pts = tr.xpath('./td[15]/text()')[0]
            plarer_s = name+'^^'+player_href+'^^'+min_t+'^^'+fg+'^^'+pt_3+'^^'+ft+'^^'+oreb+'^^'+dreb+'^^'+reb+'^^'+ast+'^^'+stl+'^^'+blk+'^^'+t_o+'^^'+pf+'^^'+jia_jian+'^^'+pts
        else:
            name = tr.xpath('./td/a/span[1]/text()')[0]
            player_href = tr.xpath('./td/a/@href')[0]
            get_players_stats(player_href)
            td_2 = tr.xpath('./td[2]/text()')[0]
            plarer_s = name + '^^' + player_href + "^^" + td_2
        stats_away_list += plarer_s + '&&'

    tr_list = tbody_list[1].xpath('.//tr')  # 替补阵容
    for tr in tr_list[:-2]:
        if len(tr.xpath('./td')) != 2:
            try:
                name = tr.xpath('./td/a/span[1]/text()')[0]
            except:
                name = False
            if name:
                player_href = tr.xpath('./td/a/@href')[0]
                get_players_stats(player_href)
                min_t = tr.xpath('./td[2]/text()')[0]
                fg = tr.xpath('./td[3]/text()')[0]
                pt_3 = tr.xpath('./td[4]/text()')[0]
                ft = tr.xpath('./td[5]/text()')[0]
                oreb = tr.xpath('./td[6]/text()')[0]
                dreb = tr.xpath('./td[7]/text()')[0]
                reb = tr.xpath('./td[8]/text()')[0]
                ast = tr.xpath('./td[9]/text()')[0]
                stl = tr.xpath('./td[10]/text()')[0]
                blk = tr.xpath('./td[11]/text()')[0]
                t_o = tr.xpath('./td[12]/text()')[0]
                pf = tr.xpath('./td[13]/text()')[0]
                jia_jian = tr.xpath('./td[14]/text()')[0]
                pts = tr.xpath('./td[15]/text()')[0]
                plarer_t = name+'^^'+player_href+'^^'+min_t+'^^'+fg+'^^'+pt_3+'^^'+ft+'^^'+oreb+'^^'+dreb+'^^'+reb+'^^'+ast+'^^'+stl+'^^'+blk+'^^'+t_o+'^^'+pf+'^^'+jia_jian+'^^'+pts
        else:
            name = tr.xpath('./td/a/span[1]/text()')[0]
            player_href = tr.xpath('./td/a/@href')[0]
            get_players_stats(player_href)
            td_2 = tr.xpath('./td[2]/text()')[0]
            plarer_t = name + '^^' + player_href + "^^" +td_2
        if name:
            stats_away_list += plarer_t + '&&'

    tt1 = tr_list[-2].xpath('./td[3]/text()')[0]
    tt2 = tr_list[-2].xpath('./td[4]/text()')[0]
    tt3 = tr_list[-2].xpath('./td[5]/text()')[0]
    tt4 = tr_list[-2].xpath('./td[6]/text()')[0]
    tt5 = tr_list[-2].xpath('./td[7]/text()')[0]
    tt6 = tr_list[-2].xpath('./td[8]/text()')[0]
    tt7 = tr_list[-2].xpath('./td[9]/text()')[0]
    tt8 = tr_list[-2].xpath('./td[10]/text()')[0]
    tt9 = tr_list[-2].xpath('./td[11]/text()')[0]
    tt10 = tr_list[-2].xpath('./td[12]/text()')[0]
    tt11 = tr_list[-2].xpath('./td[13]/text()')[0]
    tt12 = tr_list[-2].xpath('./td[15]/text()')[0]
    tt13 = tr_list[-1].xpath('./td[3]/text()')[0]
    tt14 = tr_list[-1].xpath('./td[4]/text()')[0]
    tt15 = tr_list[-1].xpath('./td[5]/text()')[0]
    team_s = tt1+'^^'+tt2+'^^'+tt3+'^^'+tt4+'^^'+tt5+'^^'+tt6+'^^'+tt7+'^^'+tt8+'^^'+tt9+'^^'+tt10+'^^'+tt11+'^^'+tt12+'^^'+tt13+'^^'+tt14+'^^'+tt15
    stats_away_list += team_s + '&&'
    total_stats_list += stats_away_list + '####'

    tbody_list = res.xpath('//div[@class="col column-two gamepackage-home-wrap"]//table[@class="mod-data"]//tbody')  # 主队
    stats_home_list = ''
    tr_list = tbody_list[0].xpath('.//tr')  # 首发阵容
    for tr in tr_list:
        if len(tr.xpath('./td')) != 2:
            name = tr.xpath('./td/a/span[1]/text()')[0]
            player_href = tr.xpath('./td/a/@href')[0]
            get_players_stats(player_href)
            min_t = tr.xpath('./td[2]/text()')[0]
            fg = tr.xpath('./td[3]/text()')[0]
            pt_3 = tr.xpath('./td[4]/text()')[0]
            ft = tr.xpath('./td[5]/text()')[0]
            oreb = tr.xpath('./td[6]/text()')[0]
            dreb = tr.xpath('./td[7]/text()')[0]
            reb = tr.xpath('./td[8]/text()')[0]
            ast = tr.xpath('./td[9]/text()')[0]
            stl = tr.xpath('./td[10]/text()')[0]
            blk = tr.xpath('./td[11]/text()')[0]
            t_o = tr.xpath('./td[12]/text()')[0]
            pf = tr.xpath('./td[13]/text()')[0]
            jia_jian = tr.xpath('./td[14]/text()')[0]
            pts = tr.xpath('./td[15]/text()')[0]
            plarer_s = name+'^^'+player_href+'^^'+min_t+'^^'+fg+'^^'+pt_3+'^^'+ft+'^^'+oreb+'^^'+dreb+'^^'+reb+'^^'+ast+'^^'+stl+'^^'+blk+'^^'+t_o+'^^'+pf+'^^'+jia_jian+'^^'+pts
        else:
            name = tr.xpath('./td/a/span[1]/text()')[0]
            player_href = tr.xpath('./td/a/@href')[0]
            get_players_stats(player_href)
            td_2 = tr.xpath('./td[2]/text()')[0]
            plarer_s = name + '^^' + player_href + "^^" + td_2
        stats_home_list += plarer_s + '&&'

    tr_list = tbody_list[1].xpath('.//tr')  # 替补阵容
    for tr in tr_list[:-2]:
        if len(tr.xpath('./td')) != 2:
            name = tr.xpath('./td/a/span[1]/text()')[0]
            player_href = tr.xpath('./td/a/@href')[0]
            get_players_stats(player_href)
            min_t = tr.xpath('./td[2]/text()')[0]
            fg = tr.xpath('./td[3]/text()')[0]
            pt_3 = tr.xpath('./td[4]/text()')[0]
            ft = tr.xpath('./td[5]/text()')[0]
            oreb = tr.xpath('./td[6]/text()')[0]
            dreb = tr.xpath('./td[7]/text()')[0]
            reb = tr.xpath('./td[8]/text()')[0]
            ast = tr.xpath('./td[9]/text()')[0]
            stl = tr.xpath('./td[10]/text()')[0]
            blk = tr.xpath('./td[11]/text()')[0]
            t_o = tr.xpath('./td[12]/text()')[0]
            pf = tr.xpath('./td[13]/text()')[0]
            jia_jian = tr.xpath('./td[14]/text()')[0]
            pts = tr.xpath('./td[15]/text()')[0]
            plarer_t = name+'^^'+player_href+'^^'+min_t+'^^'+fg+'^^'+pt_3+'^^'+ft+'^^'+oreb+'^^'+dreb+'^^'+reb+'^^'+ast+'^^'+stl+'^^'+blk+'^^'+t_o+'^^'+pf+'^^'+jia_jian+'^^'+pts
        else:
            name = tr.xpath('./td/a/span[1]/text()')[0]
            player_href = tr.xpath('./td/a/@href')[0]
            get_players_stats(player_href)
            td_2 = tr.xpath('./td[2]/text()')[0]
            plarer_t = name + '^^' + player_href + "^^" +td_2
        stats_home_list += plarer_t + '&&'

    tt1 = tr_list[-2].xpath('./td[3]/text()')[0]
    tt2 = tr_list[-2].xpath('./td[4]/text()')[0]
    tt3 = tr_list[-2].xpath('./td[5]/text()')[0]
    tt4 = tr_list[-2].xpath('./td[6]/text()')[0]
    tt5 = tr_list[-2].xpath('./td[7]/text()')[0]
    tt6 = tr_list[-2].xpath('./td[8]/text()')[0]
    tt7 = tr_list[-2].xpath('./td[9]/text()')[0]
    tt8 = tr_list[-2].xpath('./td[10]/text()')[0]
    tt9 = tr_list[-2].xpath('./td[11]/text()')[0]
    tt10 = tr_list[-2].xpath('./td[12]/text()')[0]
    tt11 = tr_list[-2].xpath('./td[13]/text()')[0]
    tt12 = tr_list[-2].xpath('./td[15]/text()')[0]
    tt13 = tr_list[-1].xpath('./td[3]/text()')[0]
    tt14 = tr_list[-1].xpath('./td[4]/text()')[0]
    tt15 = tr_list[-1].xpath('./td[5]/text()')[0]
    team_s = tt1+'^^'+tt2+'^^'+tt3+'^^'+tt4+'^^'+tt5+'^^'+tt6+'^^'+tt7+'^^'+tt8+'^^'+tt9+'^^'+tt10+'^^'+tt11+'^^'+tt12+'^^'+tt13+'^^'+tt14+'^^'+tt15
    stats_home_list += team_s + "&&"
    total_stats_list += stats_home_list
    return total_stats_list


if __name__ == '__main__':
    href = '//www.espn.com/nba/boxscore/_/id/250118010'
    get_game_stats(href)


