
data_list = []
with open('nba_url_info.log','r') as f:
    da_list = f.readlines()
    for i in da_list:
        da = i.split('INFO')[-1].strip()
        data_list.append(da)

b = [data_list[i:i+2] for i in range(0,len(data_list),2)]
print(b)

