import pymongo
import random
client = pymongo.MongoClient('localhost',27017)
ceshi = client.beihe
item_info = ceshi['whzufang_detail']
'''item_info.update_many(
    {},
    {"$set":{'time':random.randint(1,12)}}  #年龄增加1
)
'''
for i in item_info.find():
    rigion = i['rigion']

    item_info.update_many(
        { "rigion": rigion },
        {"$set": {'time': random.choice([ '1','2','2','3','3','3','4','4','4','4','5','5','5','5','6','6','6', '6'])}},  # 年龄增加1
    )



'''

#random.randint(1, 12)}

for i in item_info.find():
    rigion = i['rigion'][0:2]
    #print(rigion)
    price = i["price"]
    #print(price)
    a=a+1
'''
