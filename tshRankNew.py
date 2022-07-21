import requests
r1 = requests.get(
    "https://api.live.bilibili.com/activity/v1/Template/getRankList?act_id=2125&assist_num=5&rank_type=master&sub_type=gold_all&page=1&page_size=20")
r2 = requests.get(
    "https://api.live.bilibili.com/activity/v1/Template/getRankList?act_id=2125&assist_num=5&rank_type=master&sub_type=gold_all&page=2&page_size=20")
d1 = r1.json()
d2 = r2.json()

for xoxData in d1['data']['list']:
    print(str(xoxData['rank'])+" " +
          xoxData['uname']+" " +
          str(xoxData['score'])+" " ,end="")
    for userData in xoxData['assist_list']:
        print(userData['uname']+" " +
        str(userData['score'])+" ",end="")
    print()

for xoxData in d2['data']['list']:
    print(str(xoxData['rank'])+" " +
          xoxData['uname']+" " +
          str(xoxData['score'])+" " ,end="")
    for userData in xoxData['assist_list']:
        print(userData['uname']+" " +
        str(userData['score'])+" ",end="")
    print()

sum = 0
for xoxData in d1['data']['list']:
    sum += xoxData['score']

for xoxData in d2['data']['list']:
    sum += xoxData['score']

print("总收入："+str(sum))
