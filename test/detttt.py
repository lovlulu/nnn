import time

import redis
error_list = ['http://www.espn.com/nba/player/stats/_/id/3415/dj-augustin',
              'http://www.espn.com/nba/player/stats/_/id/4016/hasheem-thabeet',
              'http://www.espn.com/nba/player/stats/_/id/831/wally-szczerbiak',
              'http://www.espn.com/nba/player/stats/_/id/2528210/tim-hardaway-jr',
              'http://www.espn.com/nba/player/stats/_/id/2004/willie-green',
              'http://www.espn.com/nba/player/stats/_/id/3930/cartier-martin',
              'http://www.espn.com/nba/player/stats/_/id/396/anthony-johnson',
              'http://www.espn.com/nba/player/stats/_/id/881/antoine-walker',
              'http://www.espn.com/nba/player/stats/_/id/808/deshawn-stevenson',
              'http://www.espn.com/nba/player/stats/_/id/2968439/aron-baynes',
              'http://www.espn.com/nba/player/stats/_/id/2784/wayne-simien',
              'http://www.espn.com/nba/player/stats/_/id/1777/ronald-murray',
              'http://www.espn.com/nba/player/stats/_/id/556/brad-miller',
              'http://www.espn.com/nba/player/stats/_/id/1016/vladimir-radmanovic',
              'http://www.espn.com/nba/player/stats/_/id/2456/andres-nocioni',
              'http://www.espn.com/nba/player/stats/_/id/2793/von-wafer',
              'http://www.espn.com/nba/player/stats/_/id/501/karl-malone',
              'http://www.espn.com/nba/player/stats/_/id/2367/tony-allen',
              'http://www.espn.com/nba/player/stats/_/id/259/lawrence-funderburke',
              'http://www.espn.com/nba/player/stats/_/id/1731/chris-wilcox',
              'http://www.espn.com/nba/player/stats/_/id/627/olumide-oyedeji',
              'http://www.espn.com/nba/player/stats/_/id/519/tony-massenburg',
              'http://www.espn.com/nba/player/stats/_/id/2389/al-jefferson',
              'http://www.espn.com/nba/player/stats/_/id/1028/rodney-white',
              'http://www.espn.com/nba/player/stats/_/id/1024/jamaal-tinsley',
              'http://www.espn.com/nba/player/stats/_/id/660/eric-piatkowski',
              'http://www.espn.com/nba/player/stats/_/id/767/ansu-sesay',
              'http://www.espn.com/nba/player/stats/_/id/3440/darnell-jackson',
              'http://www.espn.com/nba/player/stats/_/id/2/tariq-abdul-wahad',
              'http://www.espn.com/nba/player/stats/_/id/249/greg-foster',
              'http://www.espn.com/nba/player/stats/_/id/3048/yakhouba-diawara',
              'http://www.espn.com/nba/player/stats/_/id/810/michael-stewart',
              'http://www.espn.com/nba/player/stats/_/id/4305/ish-smith',
              'http://www.espn.com/nba/player/stats/_/id/664/scot-pollard',
              'http://www.espn.com/nba/player/stats/_/id/988/jarron-collins',
              'http://www.espn.com/nba/player/stats/_/id/3478/hamed-haddadi',
              'http://www.espn.com/nba/player/stats/_/id/1783/tamar-slay',
              'http://www.espn.com/nba/player/stats/_/id/4237/john-wall',
              'http://www.espn.com/nba/player/stats/_/id/6580/bradley-beal',
              'http://www.espn.com/nba/player/stats/_/id/1042/charles-smith',
              'http://www.espn.com/nba/player/stats/_/id/1019/jeryl-sasser',
              'http://www.espn.com/nba/player/stats/_/id/882/samaki-walker',
              'http://www.espn.com/nba/player/stats/_/id/3994/jordan-hill',
              'http://www.espn.com/nba/player/stats/_/id/2368/rafael-araujo',
              'http://www.espn.com/nba/player/stats/_/id/2754/channing-frye',
              'http://www.espn.com/nba/player/stats/_/id/2578239/pat-connaughton',
              'http://www.espn.com/nba/player/stats/_/id/250/jeff-foster',
              'http://www.espn.com/nba/player/stats/_/id/3024/jj-redick',
              'http://www.espn.com/nba/player/stats/_/id/491/george-lynch',
              'http://www.espn.com/nba/player/stats/_/id/4269/nemanja-bjelica',
              'http://www.espn.com/nba/player/stats/_/id/6635/chris-copeland',
              'http://www.espn.com/nba/player/stats/_/id/674/vitaly-potapenko',
              'http://www.espn.com/nba/player/stats/_/id/6641/brian-roberts',
              'http://www.espn.com/nba/player/stats/_/id/682/joel-przybilla',
              'http://www.espn.com/nba/player/stats/_/id/824/bruno-sundov',
              'http://www.espn.com/nba/player/stats/_/id/2805/fabricio-oberto',
              'http://www.espn.com/nba/player/stats/_/id/439/travis-knight',
              'http://www.espn.com/nba/player/stats/_/id/818/rod-strickland',
              'http://www.espn.com/nba/player/stats/_/id/2995/rodney-carney',
              'http://www.espn.com/nba/player/stats/_/id/515/kenyon-martin',
              'http://www.espn.com/nba/player/stats/_/id/2383/david-harrison',
              'http://www.espn.com/nba/player/stats/_/id/24/darrell-armstrong',
              'http://www.espn.com/nba/player/stats/_/id/1013/troy-murphy',
              'http://www.espn.com/nba/player/stats/_/id/3450/oj-mayo',
              'http://www.espn.com/nba/player/stats/_/id/6598/perry-jones',
              'http://www.espn.com/nba/player/stats/_/id/3179/randolph-morris']

redis_cli_1 = redis.Redis(host='localhost', port=6379, decode_responses=True, db=1)
redis_cli = redis.Redis(host='localhost', port=6379, decode_responses=True, db=2)
print(len(error_list))
for key in error_list:
    arrayList = redis_cli.lrange(key, 0, 10000)
    # print(arrayList)
    # time.sleep(1)
    for i in arrayList:
        redis_cli_1.rpush(key, i)
        time.sleep(0.2)

# redis_cli.delete('a')

