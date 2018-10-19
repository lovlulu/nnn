import time


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
    print(b)
    timeArray = time.strptime(b, "%Y-%m-%d %H:%M")  # 转为数组
    timestamp = time.mktime(timeArray)
    print(int(timestamp))


if __name__ == '__main__':
    b = '2004-02-29T17:30Z'
    anay_time(b)