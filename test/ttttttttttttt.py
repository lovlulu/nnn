import time

import redis


a_list = list()
redis_cli_1 = redis.Redis(host='localhost', port=6379, decode_responses=True, db=1)  # 存储球员的信息 用于去重
keys_list = redis_cli_1.keys()
print(len(keys_list))
for key in keys_list:
    arrayList = redis_cli_1.lrange(key, 0, 10000)
    data_0 = arrayList[0][0]
    if data_0 == '2' or data_0 == '3':
        print(key)
    # time.sleep(0.1)
#     for i in arrayList:
#         redis_cli_1.rpush(key, i)
#         time.sleep(0.2)
# print(a_list)
# # redis_cli.delete('a')
