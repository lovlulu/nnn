# import redis
# redis_cli = redis.Redis(host='localhost', port=6379, decode_responses=True, db=15)  # 存储球员的信息 用于去重
# a = redis_cli.get('a')
# print(a)
import time


def anay_data(t1):
    t_n = int(t1.split("-")[0])
    t_m = int(t1.split("-")[1])
    t_d = int(t1.split("-")[2])
    if t_m in [1, 3, 5, 7, 8, 10, 12]:
        if t_d == 31:
            return str(t_n) + '-' + str(t_m+1) + '-' + '1'
        else:
            return str(t_n) + '-' + str(t_m) + '-' + str(t_d + 1)
    if t_m in [4, 6, 9, 11]:
        if t_d == 30:
            return str(t_n) + '-' + str(t_m + 1) + '-' + '1'
        else:
            return str(t_n) + '-' + str(t_m) + '-' + str(t_d + 1)
    if t_m == 2:
        if t_d == 28:
            return str(t_n) + '-' + str(t_m + 1) + '-' + '1'
        else:
            return str(t_n) + '-' + str(t_m) + '-' + str(t_d + 1)


def anay_time():
    game_time = '2017-10-01T00:30Z'
    t = game_time.split('T')
    t1 = t[0]
    t2 = int(t[1][:-1].split(":")[0]) + 8
    if t2 > 24:
        t2 = t2 - 24
        t1 = anay_data(t1)
    t2 = str(t2) + ":" + t[1][:-1].split(":")[1]
    b = t1 + ' ' + t2
    print(b)
    timeArray = time.strptime(b, "%Y-%m-%d %H:%M")  # 转为数组
    timestamp = time.mktime(timeArray)
    return int(timestamp)

if __name__ == '__main__':
    anay_time()
