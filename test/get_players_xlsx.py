import requests
import re
import pandas
from lxml import etree


def get_teams():
    na_list = list()
    url = 'http://www.espn.com/nba/teams'
    r = requests.get(url).text
    res = etree.HTML(r)
    href_list = res.xpath('//section[@class="ContentList mt4 ContentList--NoBorder"]//section[@class="ContentList__Item"]//div[@class="pl3"]/a/@href')
    for href in list(set(href_list))[:2]:
        url = 'http://www.espn.com/nba/team/roster/_' + href.split('_')[-1]
        print(url)
        r = requests.get(url).text
        r = etree.HTML(r)
        name_list = r.xpath('.//td[@class="sortcell"]')
        for i in name_list:
            name = i.xpath('./a/text()')[0]
            id = i.xpath('./a/@href')[0].split('/')[-2]
            print(name, id)
            data_dict = dict()
            data_dict['nba_name'] = name
            data_dict['id'] = id
            na_list.append(data_dict)

    df = pandas.DataFrame(na_list)
    df.to_excel('nba_name_new.xlsx')


def run():
    get_teams()


if __name__ == '__main__':
    run()