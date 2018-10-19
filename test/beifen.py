import redis
import time

redis_c_1 = redis.Redis(host='localhost', port=6379, decode_responses=True, db=1)
redis_c_xiao_1 = redis.Redis(host='23.91.97.81', port=6379, password='xiao123456', db=1)

keys_list = redis_c_1.keys()
print(len(keys_list))

for key in keys_list:
    print(key)
    arrayList = redis_c_1.lrange(key, 0, 100000)
    for i in arrayList:
        redis_c_xiao_1.rpush(key, i)
        time.sleep(0.2)

