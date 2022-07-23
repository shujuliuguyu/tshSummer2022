import requests
import time
url1 = "https://api.live.bilibili.com/activity/v1/Template/getRankList?act_id=2125&assist_num=1&rank_type=user&sub_type=gold_all&page="
url2 = "&page_size=20"
rList = []

for i in range(1, 11):
    r = requests.get(url1+str(i)+url2)
    rList.append(r)

dList = []
for i in range(0, 10):
    dList.append(rList[i].json())

sum = 0

for i in range(0, 10):
    for j in range(0, 20):
        print(str(dList[i]['data']['list'][j]['rank'])+" " +
              dList[i]['data']['list'][j]['uname']+" " +
              str(dList[i]['data']['list'][j]['score']))
        sum += dList[i]['data']['list'][j]['score']

print("Top200贡献总计："+str(sum))
print("制表时间："+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
