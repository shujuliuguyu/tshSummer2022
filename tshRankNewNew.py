import requests
r1 = requests.get(
    "https://api.live.bilibili.com/activity/v1/Template/getRankList?act_id=2125&assist_num=5&rank_type=master&sub_type=gold_all&page=1&page_size=20")
r2 = requests.get(
    "https://api.live.bilibili.com/activity/v1/Template/getRankList?act_id=2125&assist_num=5&rank_type=master&sub_type=gold_all&page=2&page_size=20")
d1 = r1.json()
d2 = r2.json()
dAll=d1['data']['list']+d2['data']['list']

for xoxData in dAll:
    print(str(xoxData['rank'])+" " +
          xoxData['uname']+" " +
          str(xoxData['score'])+" " ,end="")
    for userData in xoxData['assist_list']:
        print(userData['uname']+" " +
        str(userData['score'])+" ",end="")
    print()

sum = 0
for xoxData in dAll:
    sum += xoxData['score']

print("总收入："+str(sum))
