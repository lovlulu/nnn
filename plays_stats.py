import time

import requests
import json
from lxml import etree
import redis
# redis_cli_13 = redis.Redis(host='23.91.97.81', port=6379, password='xiao123456', db=13)


def set_redis(key, data):
    print(data)
    # redis_cli_13.rpush(key.replace('/seasontype/3',''), data)


def get_players_stats(url):
    if 'seasontype' in url:
        print('正在采集季后赛')
    else:
        print('正在采集常规赛数据')
    headers = {
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.text
        res = etree.HTML(data)

        try:
            name = res.xpath('//div[@class="main-headshot"]/img/@alt')[0]  # 姓名
            touxiang = res.xpath('//div[@class="main-headshot"]/img/@src')[0]  # 头像链接

            weizhi = res.xpath('//ul[@class="general-info"]//li[1]/text()')[0]  # 球衣号 位置
            shenggao = res.xpath('//ul[@class="general-info"]//li[2]/text()')[0]  # 身高 体重
            try:
                team_name = res.xpath('//ul[@class="general-info"]//li[3]/a/text()')[0]  # 所在球队
            except:
                team_name = '-'

            d_t_li_2 = res.xpath('//ul[@class="player-metadata floatleft"]//li')
            born = d_t_li_2[0].xpath('./text()')[0]  # 出生地和日期
            drafted = d_t_li_2[1].xpath('./text()')[0]  # 选秀顺位
            college = d_t_li_2[2].xpath('./text()')[0]  # 大学
            try:
                experience = d_t_li_2[3].xpath('./text()')[0]  # 待在NBA的时间
            except:
                experience = '-'
            jiben_xinxi = name+'^^'+touxiang+'^^'+weizhi+'^^'+shenggao+'^^'+team_name+'^^'+born+'^^'+drafted+'^^'+college+'^^'+experience

            data_list = res.xpath('//div[@class="mod-container mod-table mod-player-stats"]/div[@class="mod-content"]')
            d_li_1 = data_list[0].xpath('.//tr[@class="oddrow"]|.//tr[@class="evenrow"]')  # POSTSEASON AVERAGES 平均
            data1_t = ''
            for d_t in d_li_1:  # 具体数据
                season = d_t.xpath('.//td[1]/text()')[0]  # 赛季
                team = d_t.xpath('.//td[2]//li[@class="team-name"]/a/text()|.//td[2]//li[@class="team-name"]/text()')[0]  # 队伍名称
                gp = d_t.xpath('.//td[3]/text()')[0]  # 总场数
                gs = d_t.xpath('.//td[4]/text()')[0]  # 首发
                min_t = d_t.xpath('.//td[5]/text()')[0]  # 出场时间
                fgm_a = d_t.xpath('.//td[6]/text()')[0]  # 命中出手
                fg = d_t.xpath('.//td[7]/text()')[0]  # 命中率
                pm_a = d_t.xpath('.//td[8]/text()')[0]  # 三分命中——出手
                p_3 = d_t.xpath('.//td[9]/text()')[0]  # 三分命中率
                ftm_a = d_t.xpath('.//td[10]/text()')[0]  # 罚球命中--出手
                ft = d_t.xpath('.//td[11]/text()')[0]  # 罚球命中率
                o_r = d_t.xpath('.//td[12]/text()')[0]  # 进攻篮板
                d_r = d_t.xpath('.//td[13]/text()')[0]  # 防守篮板
                reb = d_t.xpath('.//td[14]/text()')[0]  # 总篮板
                ast = d_t.xpath('.//td[15]/text()')[0]  # 助攻
                blk = d_t.xpath('.//td[16]/text()')[0]  # 盖帽
                stl = d_t.xpath('.//td[17]/text()')[0]  # 抢断
                pf = d_t.xpath('.//td[18]/text()')[0]  # 个人犯规
                t_o = d_t.xpath('.//td[19]/text()')[0]  # 失误
                pts = d_t.xpath('.//td[20]/text()')[0]  # 得分
                data1 = season+'^^'+team+'^^'+gp+'^^'+gs+'^^'+min_t+'^^'+fgm_a+'^^'+fg+'^^'+pm_a+'^^'+p_3+'^^'+ftm_a+'^^'+ft+'^^'+o_r+'^^'+d_r+'^^'+reb+'^^'+ast+'^^'+blk+'^^'+stl+'^^'+pf+'^^'+t_o+'^^'+pts
                data1_t += data1 + '&&'

            career_1 = data_list[0].xpath('.//tr[@class="total"]')[0]  # 计算平均值
            gp = career_1.xpath('.//td[2]/text()')[0]
            gs = career_1.xpath('.//td[3]/text()')[0]
            min_t = career_1.xpath('.//td[4]/text()')[0]
            fgm_a = career_1.xpath('.//td[5]/text()')[0]
            fg = career_1.xpath('.//td[6]/text()')[0]
            pm_a = career_1.xpath('.//td[7]/text()')[0]
            p_3 = career_1.xpath('.//td[8]/text()')[0]
            ftm_a = career_1.xpath('.//td[9]/text()')[0]
            ft = career_1.xpath('.//td[10]/text()')[0]
            o_r = career_1.xpath('.//td[11]/text()')[0]
            d_r = career_1.xpath('.//td[12]/text()')[0]
            reb = career_1.xpath('.//td[13]/text()')[0]
            ast = career_1.xpath('.//td[14]/text()')[0]
            blk = career_1.xpath('.//td[15]/text()')[0]
            stl = career_1.xpath('.//td[16]/text()')[0]
            pf = career_1.xpath('.//td[17]/text()')[0]
            t_o = career_1.xpath('.//td[18]/text()')[0]
            pts = career_1.xpath('.//td[19]/text()')[0]
            data1_tt = data1_t +'^&^'+ gp+'^^'+gs+'^^'+min_t+'^^'+fgm_a+'^^'+fg+'^^'+pm_a+'^^'+p_3+'^^'+ftm_a+'^^'+ft+'^^'+o_r+'^^'+d_r+'^^'+reb+'^^'+ast+'^^'+blk+'^^'+stl+'^^'+pf+'^^'+t_o+'^^'+pts

            data2_t = ''
            d_li_2 = data_list[1].xpath('.//tr[@class="oddrow"]|.//tr[@class="evenrow"]')  # POSTSEASON TOTALS 总计
            for d_t in d_li_2:  # 具体数据
                season = d_t.xpath('.//td[1]/text()')[0]  # 赛季
                team = d_t.xpath('.//td[2]//li[@class="team-name"]/a/text()|.//td[2]//li[@class="team-name"]/text()')[0]  # 队伍名称
                fgm_a = d_t.xpath('.//td[3]/text()')[0]
                fg = d_t.xpath('.//td[4]/text()')[0]
                pm_a = d_t.xpath('.//td[5]/text()')[0]
                p_3 = d_t.xpath('.//td[6]/text()')[0]
                ftm_a = d_t.xpath('.//td[7]/text()')[0]
                ft = d_t.xpath('.//td[8]/text()')[0]
                o_r = d_t.xpath('.//td[9]/text()')[0]
                d_r = d_t.xpath('.//td[10]/text()')[0]
                reb = d_t.xpath('.//td[11]/text()')[0]
                ast = d_t.xpath('.//td[12]/text()')[0]
                blk = d_t.xpath('.//td[13]/text()')[0]
                stl = d_t.xpath('.//td[14]/text()')[0]
                pf = d_t.xpath('.//td[15]/text()')[0]
                t_o = d_t.xpath('.//td[16]/text()')[0]
                pts = d_t.xpath('.//td[17]/text()')[0]
                data2 = season+'^^'+team+'^^'+ fgm_a+'^^'+fg+'^^'+ pm_a+'^^'+ p_3+'^^'+ftm_a+'^^'+ft+'^^'+o_r+'^^'+d_r+'^^'+reb+'^^'+ast+'^^'+blk+'^^'+stl+'^^'+pf+'^^'+t_o+'^^'+pts
                data2_t += data2 + '&&'

            career_2 = data_list[1].xpath('.//tr[@class="total"]')[0]  # 计算平均值
            fgm_a = career_2.xpath('.//td[2]/text()')[0]
            fg = career_2.xpath('.//td[3]/text()')[0]
            pm_a = career_2.xpath('.//td[4]/text()')[0]
            p_3 = career_2.xpath('.//td[5]/text()')[0]
            ftm_a = career_2.xpath('.//td[6]/text()')[0]
            ft = career_2.xpath('.//td[7]/text()')[0]
            o_r = career_2.xpath('.//td[8]/text()')[0]
            d_r = career_2.xpath('.//td[9]/text()')[0]
            reb = career_2.xpath('.//td[10]/text()')[0]
            ast = career_2.xpath('.//td[11]/text()')[0]
            blk = career_2.xpath('.//td[12]/text()')[0]
            stl = career_2.xpath('.//td[13]/text()')[0]
            pf = career_2.xpath('.//td[14]/text()')[0]
            t_o = career_2.xpath('.//td[15]/text()')[0]
            pts = career_2.xpath('.//td[16]/text()')[0]
            data2_tt = data2_t + '^&^' + fgm_a+'^^'+ fg+'^^'+ pm_a+'^^'+ p_3+'^^'+ftm_a+'^^'+ ft+'^^'+ o_r+'^^'+ d_r+'^^'+ reb+'^^' + ast+'^^'+blk+'^^'+stl+'^^'+pf+'^^'+ t_o+'^^'+pts

            data3_t = ''
            d_li_3 = data_list[2].xpath('.//tr[@class="oddrow"]|.//tr[@class="evenrow"]')  # 杂项 总计
            for d_t in d_li_3:  # 具体数据
                season = d_t.xpath('.//td[1]/text()')[0]  # 赛季
                team = d_t.xpath('.//td[2]//li[@class="team-name"]/a/text()|.//td[2]//li[@class="team-name"]/text()')[0]  # 队伍名称
                dbldbl = d_t.xpath('.//td[3]/text()')[0]
                tridbl = d_t.xpath('.//td[4]/text()')[0]
                d_q = d_t.xpath('.//td[5]/text()')[0]
                eject = d_t.xpath('.//td[6]/text()')[0]
                tech = d_t.xpath('.//td[7]/text()')[0]
                flag = d_t.xpath('.//td[8]/text()')[0]
                ast_to = d_t.xpath('.//td[9]/text()')[0]
                stl_to = d_t.xpath('.//td[10]/text()')[0]
                rat = d_t.xpath('.//td[11]/text()')[0]
                sceff = d_t.xpath('.//td[12]/text()')[0]
                sheff = d_t.xpath('.//td[13]/text()')[0]
                data3 = season+'^^'+team+'^^'+dbldbl+'^^'+tridbl+'^^'+d_q+'^^'+eject+'^^'+tech+'^^'+ flag+'^^'+ast_to+'^^'+stl_to+'^^'+rat+'^^'+sceff+'^^'+sheff
                data3_t += data3 + '&&'

            career_3 = data_list[2].xpath('.//tr[@class="total"]')[0]  # 计算平均值
            dbldbl = career_3.xpath('.//td[2]/text()')[0]
            tridbl = career_3.xpath('.//td[3]/text()')[0]
            d_q = career_3.xpath('.//td[4]/text()')[0]
            eject = career_3.xpath('.//td[5]/text()')[0]
            tech = career_3.xpath('.//td[6]/text()')[0]
            flag = career_3.xpath('.//td[7]/text()')[0]
            ast_to = career_3.xpath('.//td[8]/text()')[0]
            stl_to = career_3.xpath('.//td[9]/text()')[0]
            rat = career_3.xpath('.//td[10]/text()')[0]
            sceff = career_3.xpath('.//td[11]/text()')[0]
            sheff = career_3.xpath('.//td[12]/text()')[0]
            data3_tt = data3_t + '^&^' +dbldbl+'^^'+tridbl+'^^' + d_q+'^^'+eject+'^^'+tech+'^^'+flag+'^^'+ast_to+'^^'+stl_to+'^^'+rat+'^^'+ sceff+'^^'+sheff
            da_tt = data1_tt + "####" + data2_tt + "####" + data3_tt
            set_data = jiben_xinxi+'^##^'+da_tt
            if 'seasontype/3' in url:
                set_redis(url, "3"+set_data)
            else:
                set_redis(url, "2" + set_data)
        except Exception as e:
            print('球员没有赛季信息--', url)
    else:
        pass


def get_players_href():
    redis_cli = redis.Redis(host='localhost', port=6379, decode_responses=True, db=1)  # 存储球员的信息 用于去重
    keys_list = redis_cli.keys()
    for key in keys_list:
        print(key)
        arrayList = redis_cli.lrange(key, 0, 10000)
        print(arrayList[0])
        time.sleep(100)
        # for i in arrayList:
        #     redis_c_xiao_1.rpush(key, i)
        #     time.sleep(0.2)


def get_fen_lei(url):
    uu = url.split('/')[-2:]
    url_2 = 'http://www.espn.com/nba/player/stats/_/id/'+uu[0]+'/'+uu[1]  # 常规赛
    url_3 = 'http://www.espn.com/nba/player/stats/_/id/'+uu[0]+'/seasontype/3/'+uu[1]  # 季后赛
    get_players_stats(url_2)
    get_players_stats(url_3)


if __name__ == '__main__':
    get_players_href()
    # url = 'http://www.espn.com/nba/player/stats/_/id/2004/willie-green'
    # get_fen_lei(url)
