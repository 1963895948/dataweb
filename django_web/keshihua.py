import pymongo
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy

#北京，上海，长沙，武汉，广州，成都
client = pymongo.MongoClient('localhost', 27017)#连接数据库

zufang_data = client['city58']#58数据库
bj_info_58 = zufang_data['bjzufang_detail']#连接表格

sh_info_58 = zufang_data['shzufang_detail']

cs_info_58 = zufang_data['cszufang_detail']

wh_info_58 = zufang_data['whzufang_detail']

gz_info_58 = zufang_data['gzzufang_detail']

cd_info_58 = zufang_data['cdzufang_detail']


zufang_data = client['beihe']#连接贝壳
bj_info_beihe = zufang_data['bjzufang_detail']

sh_info_beihe = zufang_data['shzufang_detail']

cs_info_beihe = zufang_data['cszufang_detail']

wh_info_beihe = zufang_data['whzufang_detail']

gz_info_beihe = zufang_data['gzzufang_detail']

cd_info_beihe = zufang_data['cdzufang_detail']


######################  58同城

###################################################################################################################上海
def sum_sh_58():#上海总共有多少数据
    a=0
    for i in sh_info_58.find():
        if(i['house']):
            a=a+1
    sum_58_sh = a
    return sum_58_sh

def type_sh_58():
    a=0
    others=0
    fangzitype_list=[]
    fangzitype_data=[]
    b=[]
    fangzitype_dict={}
    for i in sh_info_58.find():
        if(i['house']):
            #print(i["house"])
            a=a+1
            #print(i["house"]["type"][0:7])
            fangzitype_list.append(i["house"]["type"][0:6])
            #print(i["house"]["decoration"][3:7])
    #print(a)

    fangzitype = list(set(fangzitype_list))
    print(a)
    print(fangzitype)
    for i in fangzitype:#统计各类型房子数
        if(fangzitype_list.count(i)>100):
            b.append(i)
            fangzitype_data.append(fangzitype_list.count(i))
            others=others+fangzitype_list.count(i)

    other = a-others
    fangzitype_dict["type"] = b
    fangzitype_dict["values"]=fangzitype_data
    fangzitype_dict["type"].append("其他")
    fangzitype_dict["values"].append(other)
    print(fangzitype_dict)


    return fangzitype_dict


def price_sh_type_58():
    price_tpye_dict = {}
    price_tpye_dict["500"]=0
    price_tpye_dict["1000"]=0
    price_tpye_dict["1500"]=0
    price_tpye_dict["2000"]=0
    price_tpye_dict["2500"]=0
    price_tpye_dict["3000"]=0
    price_tpye_dict["9999"]=0
    for i in sh_info_58.find():
        if(i['house']):
            if(int(i["price"])<500):
                price_tpye_dict["500"]=price_tpye_dict["500"]+1
            elif(500<int(i["price"])<1000):
                price_tpye_dict["1000"] = price_tpye_dict["1000"] + 1
            elif (1000 < int(i["price"]) < 1500):
                price_tpye_dict["1500"] = price_tpye_dict["1500"] + 1
            elif (1500 < int(i["price"]) < 2000):
                price_tpye_dict["2000"] = price_tpye_dict["2000"] + 1
            elif (2000 < int(i["price"]) < 2500):
                price_tpye_dict["2500"] = price_tpye_dict["2500"] + 1
            elif (2500 < int(i["price"]) < 3000):
                price_tpye_dict["3000"] = price_tpye_dict["3000"] + 1
            else:
                price_tpye_dict["9999"] = price_tpye_dict["9999"] + 1
    print(price_tpye_dict)
    price_tpye_dict_58={}
    price_tpye_dict_58["type"]=[]
    price_tpye_dict_58["values"]=[]
    for i_key,i_values in price_tpye_dict.items():
        price_tpye_dict_58["type"].append(i_key)
        price_tpye_dict_58["values"].append(i_values)

    print(price_tpye_dict_58)
    return price_tpye_dict_58

def pay_sh_method_58():
    pay_method_list=[]
    pay_method_dict={}
    a=0
    for i in sh_info_58.find():
        if(i['house']):
            pay_method_list.append(i["pay_method"])
            a = a+1

    pay_method_index = list(set(pay_method_list))

    for i in pay_method_index:
        pay_method_dict[i] = pay_method_list.count(i)

    print(a)
    print(pay_method_dict)

    method_tpye_dict_58={}
    method_tpye_dict_58["type"]=[]
    method_tpye_dict_58["values"]=[]
    for i_key,i_values in pay_method_dict.items():
        method_tpye_dict_58["type"].append(i_key)
        method_tpye_dict_58["values"].append(i_values)

    print(method_tpye_dict_58)
    return method_tpye_dict_58


def rigion_sh_58():
    rigion_list = []
    rigion_dict = {}
    a = 0
    for i in sh_info_58.find():
        if (i['house']):
            rigion_list.append(i["rigion"].split()[0])
            a=a+1
            #print(i["rigion"].split()[0])

    rigion_list_index = list(set(rigion_list))
    for i in rigion_list_index:
        rigion_dict[i] = rigion_list.count(i)

    print(a)
    print(rigion_dict)

    rigion_tpye_dict_58 = {}
    rigion_tpye_dict_58["type"] = []
    rigion_tpye_dict_58["values"] = []
    for i_key, i_values in rigion_dict.items():
        rigion_tpye_dict_58["type"].append(i_key)
        rigion_tpye_dict_58["values"].append(i_values)

    print(rigion_tpye_dict_58)
    return rigion_tpye_dict_58

def time_sh_58():
    time_dict={}
    time_dict["1"]=0
    time_dict["2"] = 0
    time_dict["3"] = 0
    time_dict["4"] = 0
    time_dict["5"] = 0
    time_dict["6"] = 0
    for i in sh_info_58.find():
        if (int(i["time"])==1):
            time_dict["1"]=time_dict["1"]+1
        if (int(i["time"]) == 2 ):
            time_dict["2"] = time_dict["2"] + 1
        if (int(i["time"]) == 3):
            time_dict["3"] = time_dict["3"] + 1
        if (int(i["time"]) == 4):
            time_dict["4"] = time_dict["4"] + 1
        if (int(i["time"]) == 5):
            time_dict["5"] = time_dict["5"] + 1
        if (int(i["time"]) == 6):
            time_dict["6"] = time_dict["6"] + 1

    time_tpye_dict_58 = {}
    time_tpye_dict_58["type"] = []
    time_tpye_dict_58["values"] = []
    for i_key, i_values in time_dict.items():
        time_tpye_dict_58["type"].append(i_key)
        time_tpye_dict_58["values"].append(i_values)

    print(time_tpye_dict_58)
    return time_tpye_dict_58


def rigion_price_sh_58():
    rigion_list = []
    rigion_dict = {}
    a = 0
    for i in sh_info_58.find():
        if (i['house']):
            rigion_list.append(i["rigion"].split()[0])
            a = a + 1
            # print(i["rigion"].split()[0])

    rigion_list_index = list(set(rigion_list))
    for i in rigion_list_index:
        rigion_dict[i] = rigion_list.count(i)

    print(a)
    print(rigion_dict)


    data_dict={}
    data_dict["type"]=[]
    data_dict["values"] = []
    for i_key,i_values in rigion_dict.items():
        data = 0
        for j in sh_info_58.find():
            if(j["rigion"].split()[0]==i_key):
                data = data+int(j["price"])
        data_dict["type"].append(i_key)
        data_dict["values"].append(round(data/i_values,1))

    print(data_dict)












############################################################################################gz
def sum_gz_58():#广州总共有多少数据
    a=0
    for i in gz_info_58.find():
        if(i['house']):
            a=a+1
    sum_58_gz = a
    return sum_58_gz

def type_gz_58():
    a=0
    others=0
    fangzitype_list=[]
    fangzitype_data=[]
    b=[]
    fangzitype_dict={}
    for i in gz_info_58.find():
        if(i['house']):
            #print(i["house"])
            a=a+1
            #print(i["house"]["type"][0:7])
            fangzitype_list.append(i["house"]["type"][0:6])
            #print(i["house"]["decoration"][3:7])
    #print(a)

    fangzitype = list(set(fangzitype_list))
    print(a)
    print(fangzitype)
    for i in fangzitype:#统计各类型房子数
        if(fangzitype_list.count(i)>100):
            b.append(i)
            fangzitype_data.append(fangzitype_list.count(i))
            others=others+fangzitype_list.count(i)

    other = a-others
    fangzitype_dict["type"] = b
    fangzitype_dict["values"]=fangzitype_data
    fangzitype_dict["type"].append("其他")
    fangzitype_dict["values"].append(other)
    print(fangzitype_dict)


    return fangzitype_dict


def price_gz_type_58():
    price_tpye_dict = {}
    price_tpye_dict["500"]=0
    price_tpye_dict["1000"]=0
    price_tpye_dict["1500"]=0
    price_tpye_dict["2000"]=0
    price_tpye_dict["2500"]=0
    price_tpye_dict["3000"]=0
    price_tpye_dict["9999"]=0
    for i in gz_info_58.find():
        if(i['house']):
            if(int(i["price"])<500):
                price_tpye_dict["500"]=price_tpye_dict["500"]+1
            elif(500<int(i["price"])<1000):
                price_tpye_dict["1000"] = price_tpye_dict["1000"] + 1
            elif (1000 < int(i["price"]) < 1500):
                price_tpye_dict["1500"] = price_tpye_dict["1500"] + 1
            elif (1500 < int(i["price"]) < 2000):
                price_tpye_dict["2000"] = price_tpye_dict["2000"] + 1
            elif (2000 < int(i["price"]) < 2500):
                price_tpye_dict["2500"] = price_tpye_dict["2500"] + 1
            elif (2500 < int(i["price"]) < 3000):
                price_tpye_dict["3000"] = price_tpye_dict["3000"] + 1
            else:
                price_tpye_dict["9999"] = price_tpye_dict["9999"] + 1
    print(price_tpye_dict)
    price_tpye_dict_58={}
    price_tpye_dict_58["type"]=[]
    price_tpye_dict_58["values"]=[]
    for i_key,i_values in price_tpye_dict.items():
        price_tpye_dict_58["type"].append(i_key)
        price_tpye_dict_58["values"].append(i_values)

    print(price_tpye_dict_58)
    return price_tpye_dict_58

def pay_gz_method_58():
    pay_method_list=[]
    pay_method_dict={}
    a=0
    for i in gz_info_58.find():
        if(i['house']):
            pay_method_list.append(i["pay_method"])
            a = a+1

    pay_method_index = list(set(pay_method_list))

    for i in pay_method_index:
        pay_method_dict[i] = pay_method_list.count(i)

    print(a)
    print(pay_method_dict)

    method_tpye_dict_58={}
    method_tpye_dict_58["type"]=[]
    method_tpye_dict_58["values"]=[]
    for i_key,i_values in pay_method_dict.items():
        method_tpye_dict_58["type"].append(i_key)
        method_tpye_dict_58["values"].append(i_values)

    print(method_tpye_dict_58)
    return method_tpye_dict_58


def rigion_gz_58():
    rigion_list = []
    rigion_dict = {}
    a = 0
    for i in gz_info_58.find():
        if (i['house']):
            rigion_list.append(i["rigion"].split()[0])
            a=a+1
            #print(i["rigion"].split()[0])

    rigion_list_index = list(set(rigion_list))
    for i in rigion_list_index:
        rigion_dict[i] = rigion_list.count(i)

    print(a)
    print(rigion_dict)

    rigion_tpye_dict_58 = {}
    rigion_tpye_dict_58["type"] = []
    rigion_tpye_dict_58["values"] = []
    for i_key, i_values in rigion_dict.items():
        rigion_tpye_dict_58["type"].append(i_key)
        rigion_tpye_dict_58["values"].append(i_values)

    print(rigion_tpye_dict_58)
    return rigion_dict

def time_gz_58():
    time_dict={}
    time_dict["1"]=0
    time_dict["2"] = 0
    time_dict["3"] = 0
    time_dict["4"] = 0
    time_dict["5"] = 0
    time_dict["6"] = 0
    for i in gz_info_58.find():
        if (int(i["time"])==1):
            time_dict["1"]=time_dict["1"]+1
        if (int(i["time"]) == 2 ):
            time_dict["2"] = time_dict["2"] + 1
        if (int(i["time"]) == 3):
            time_dict["3"] = time_dict["3"] + 1
        if (int(i["time"]) == 4):
            time_dict["4"] = time_dict["4"] + 1
        if (int(i["time"]) == 5):
            time_dict["5"] = time_dict["5"] + 1
        if (int(i["time"]) == 6):
            time_dict["6"] = time_dict["6"] + 1

    time_tpye_dict_58 = {}
    time_tpye_dict_58["type"] = []
    time_tpye_dict_58["values"] = []
    for i_key, i_values in time_dict.items():
        time_tpye_dict_58["type"].append(i_key)
        time_tpye_dict_58["values"].append(i_values)

    print(time_tpye_dict_58)
    return time_tpye_dict_58


def rigion_price_gz_58():
    rigion_list = []
    rigion_dict = {}
    a = 0
    for i in gz_info_58.find():
        if (i['house']):
            rigion_list.append(i["rigion"].split()[0])
            a = a + 1
            # print(i["rigion"].split()[0])

    rigion_list_index = list(set(rigion_list))
    for i in rigion_list_index:
        rigion_dict[i] = rigion_list.count(i)

    print(a)
    print(rigion_dict)


    data_dict={}
    data_dict["type"]=[]
    data_dict["values"] = []
    for i_key,i_values in rigion_dict.items():
        data = 0
        for j in gz_info_58.find():
            if(j["rigion"].split()[0]==i_key):
                data = data+int(j["price"])
        data_dict["type"].append(i_key)
        data_dict["values"].append(round(data/i_values,1))

    print(data_dict)





#####bj
def sum_bj_58():#北京总共有多少数据
    a=0
    for i in bj_info_58.find():
        if(i['house']):
            a=a+1
    sum_58_bj = a
    return sum_58_bj

def type_bj_58():
    a=0
    others=0
    fangzitype_list=[]
    fangzitype_data=[]
    b=[]
    fangzitype_dict={}
    for i in bj_info_58.find():
        if(i['house']):
            #print(i["house"])
            a=a+1
            #print(i["house"]["type"][0:7])
            fangzitype_list.append(i["house"]["type"][0:6])
            #print(i["house"]["decoration"][3:7])
    #print(a)

    fangzitype = list(set(fangzitype_list))
    print(a)
    print(fangzitype)
    for i in fangzitype:#统计各类型房子数
        if(fangzitype_list.count(i)>100):
            b.append(i)
            fangzitype_data.append(fangzitype_list.count(i))
            others=others+fangzitype_list.count(i)

    other = a-others
    fangzitype_dict["type"] = b
    fangzitype_dict["values"]=fangzitype_data
    fangzitype_dict["type"].append("其他")
    fangzitype_dict["values"].append(other)
    print(fangzitype_dict)


    return fangzitype_dict


def price_bj_type_58():
    price_tpye_dict = {}
    price_tpye_dict["500"]=0
    price_tpye_dict["1000"]=0
    price_tpye_dict["1500"]=0
    price_tpye_dict["2000"]=0
    price_tpye_dict["2500"]=0
    price_tpye_dict["3000"]=0
    price_tpye_dict["9999"]=0
    for i in bj_info_58.find():
        if(i['house']):
            if(int(i["price"])<500):
                price_tpye_dict["500"]=price_tpye_dict["500"]+1
            elif(500<int(i["price"])<1000):
                price_tpye_dict["1000"] = price_tpye_dict["1000"] + 1
            elif (1000 < int(i["price"]) < 1500):
                price_tpye_dict["1500"] = price_tpye_dict["1500"] + 1
            elif (1500 < int(i["price"]) < 2000):
                price_tpye_dict["2000"] = price_tpye_dict["2000"] + 1
            elif (2000 < int(i["price"]) < 2500):
                price_tpye_dict["2500"] = price_tpye_dict["2500"] + 1
            elif (2500 < int(i["price"]) < 3000):
                price_tpye_dict["3000"] = price_tpye_dict["3000"] + 1
            else:
                price_tpye_dict["9999"] = price_tpye_dict["9999"] + 1
    print(price_tpye_dict)
    price_tpye_dict_58={}
    price_tpye_dict_58["type"]=[]
    price_tpye_dict_58["values"]=[]
    for i_key,i_values in price_tpye_dict.items():
        price_tpye_dict_58["type"].append(i_key)
        price_tpye_dict_58["values"].append(i_values)

    print(price_tpye_dict_58)
    return price_tpye_dict_58

def pay_bj_method_58():
    pay_method_list=[]
    pay_method_dict={}
    a=0
    for i in bj_info_58.find():
        if(i['house']):
            pay_method_list.append(i["pay_method"])
            a = a+1

    pay_method_index = list(set(pay_method_list))

    for i in pay_method_index:
        pay_method_dict[i] = pay_method_list.count(i)

    print(a)
    print(pay_method_dict)

    method_tpye_dict_58={}
    method_tpye_dict_58["type"]=[]
    method_tpye_dict_58["values"]=[]
    for i_key,i_values in pay_method_dict.items():
        method_tpye_dict_58["type"].append(i_key)
        method_tpye_dict_58["values"].append(i_values)

    print(method_tpye_dict_58)
    return method_tpye_dict_58


def rigion_bj_58():
    rigion_list = []
    rigion_dict = {}
    a = 0
    for i in bj_info_58.find():
        if (i['house']):
            rigion_list.append(i["rigion"].split()[0])
            a=a+1
            #print(i["rigion"].split()[0])

    rigion_list_index = list(set(rigion_list))
    for i in rigion_list_index:
        rigion_dict[i] = rigion_list.count(i)

    print(a)
    print(rigion_dict)

    rigion_tpye_dict_58 = {}
    rigion_tpye_dict_58["type"] = []
    rigion_tpye_dict_58["values"] = []
    for i_key, i_values in rigion_dict.items():
        rigion_tpye_dict_58["type"].append(i_key)
        rigion_tpye_dict_58["values"].append(i_values)

    print(rigion_tpye_dict_58)
    return rigion_dict

def time_bj_58():
    time_dict={}
    time_dict["1"]=0
    time_dict["2"] = 0
    time_dict["3"] = 0
    time_dict["4"] = 0
    time_dict["5"] = 0
    time_dict["6"] = 0
    for i in bj_info_58.find():
        if (int(i["time"])==1):
            time_dict["1"]=time_dict["1"]+1
        if (int(i["time"]) == 2 ):
            time_dict["2"] = time_dict["2"] + 1
        if (int(i["time"]) == 3):
            time_dict["3"] = time_dict["3"] + 1
        if (int(i["time"]) == 4):
            time_dict["4"] = time_dict["4"] + 1
        if (int(i["time"]) == 5):
            time_dict["5"] = time_dict["5"] + 1
        if (int(i["time"]) == 6):
            time_dict["6"] = time_dict["6"] + 1

    time_tpye_dict_58 = {}
    time_tpye_dict_58["type"] = []
    time_tpye_dict_58["values"] = []
    for i_key, i_values in time_dict.items():
        time_tpye_dict_58["type"].append(i_key)
        time_tpye_dict_58["values"].append(i_values)

    print(time_tpye_dict_58)
    return time_tpye_dict_58


def rigion_price_bj_58():
    rigion_list = []
    rigion_dict = {}
    a = 0
    for i in bj_info_58.find():
        if (i['house']):
            rigion_list.append(i["rigion"].split()[0])
            a = a + 1
            # print(i["rigion"].split()[0])

    rigion_list_index = list(set(rigion_list))
    for i in rigion_list_index:
        rigion_dict[i] = rigion_list.count(i)

    print(a)
    print(rigion_dict)


    data_dict={}
    data_dict["type"]=[]
    data_dict["values"] = []
    for i_key,i_values in rigion_dict.items():
        data = 0
        for j in bj_info_58.find():
            if(j["rigion"].split()[0]==i_key):
                data = data+int(j["price"])
        data_dict["type"].append(i_key)
        data_dict["values"].append(round(data/i_values,1))

    print(data_dict)







################################################################################cs
def sum_cs_58():#长沙总共有多少数据
    a=0
    for i in cs_info_58.find():
        if(i['house']):
            a=a+1
    sum_58_cs = a
    return sum_58_cs

def type_cs_58():
    a=0
    others=0
    fangzitype_list=[]
    fangzitype_data=[]
    b=[]
    fangzitype_dict={}
    for i in cs_info_58.find():
        if(i['house']):
            #print(i["house"])
            a=a+1
            #print(i["house"]["type"][0:7])
            fangzitype_list.append(i["house"]["type"][0:6])
            #print(i["house"]["decoration"][3:7])
    #print(a)

    fangzitype = list(set(fangzitype_list))
    print(a)
    print(fangzitype)
    for i in fangzitype:#统计各类型房子数
        if(fangzitype_list.count(i)>100):
            b.append(i)
            fangzitype_data.append(fangzitype_list.count(i))
            others=others+fangzitype_list.count(i)

    other = a-others
    fangzitype_dict["type"] = b
    fangzitype_dict["values"]=fangzitype_data
    fangzitype_dict["type"].append("其他")
    fangzitype_dict["values"].append(other)
    print(fangzitype_dict)


    return fangzitype_dict


def price_cs_type_58():
    price_tpye_dict = {}
    price_tpye_dict["500"]=0
    price_tpye_dict["1000"]=0
    price_tpye_dict["1500"]=0
    price_tpye_dict["2000"]=0
    price_tpye_dict["2500"]=0
    price_tpye_dict["3000"]=0
    price_tpye_dict["9999"]=0
    for i in cs_info_58.find():
        if(i['house']):
            if(int(i["price"])<500):
                price_tpye_dict["500"]=price_tpye_dict["500"]+1
            elif(500<int(i["price"])<1000):
                price_tpye_dict["1000"] = price_tpye_dict["1000"] + 1
            elif (1000 < int(i["price"]) < 1500):
                price_tpye_dict["1500"] = price_tpye_dict["1500"] + 1
            elif (1500 < int(i["price"]) < 2000):
                price_tpye_dict["2000"] = price_tpye_dict["2000"] + 1
            elif (2000 < int(i["price"]) < 2500):
                price_tpye_dict["2500"] = price_tpye_dict["2500"] + 1
            elif (2500 < int(i["price"]) < 3000):
                price_tpye_dict["3000"] = price_tpye_dict["3000"] + 1
            else:
                price_tpye_dict["9999"] = price_tpye_dict["9999"] + 1
    print(price_tpye_dict)
    price_tpye_dict_58={}
    price_tpye_dict_58["type"]=[]
    price_tpye_dict_58["values"]=[]
    for i_key,i_values in price_tpye_dict.items():
        price_tpye_dict_58["type"].append(i_key)
        price_tpye_dict_58["values"].append(i_values)

    print(price_tpye_dict_58)
    return price_tpye_dict_58

def pay_cs_method_58():
    pay_method_list=[]
    pay_method_dict={}
    a=0
    for i in cs_info_58.find():
        if(i['house']):
            pay_method_list.append(i["pay_method"])
            a = a+1

    pay_method_index = list(set(pay_method_list))

    for i in pay_method_index:
        pay_method_dict[i] = pay_method_list.count(i)

    print(a)
    print(pay_method_dict)

    method_tpye_dict_58={}
    method_tpye_dict_58["type"]=[]
    method_tpye_dict_58["values"]=[]
    for i_key,i_values in pay_method_dict.items():
        method_tpye_dict_58["type"].append(i_key)
        method_tpye_dict_58["values"].append(i_values)

    print(method_tpye_dict_58)
    return method_tpye_dict_58


def rigion_cs_58():
    rigion_list = []
    rigion_dict = {}
    a = 0
    for i in cs_info_58.find():
        if (i['house']):
            rigion_list.append(i["rigion"].split()[0])
            a=a+1
            #print(i["rigion"].split()[0])

    rigion_list_index = list(set(rigion_list))
    for i in rigion_list_index:
        rigion_dict[i] = rigion_list.count(i)

    print(a)
    print(rigion_dict)

    rigion_tpye_dict_58 = {}
    rigion_tpye_dict_58["type"] = []
    rigion_tpye_dict_58["values"] = []
    for i_key, i_values in rigion_dict.items():
        rigion_tpye_dict_58["type"].append(i_key)
        rigion_tpye_dict_58["values"].append(i_values)

    print(rigion_tpye_dict_58)
    return rigion_dict

def time_cs_58():
    time_dict={}
    time_dict["1"]=0
    time_dict["2"] = 0
    time_dict["3"] = 0
    time_dict["4"] = 0
    time_dict["5"] = 0
    time_dict["6"] = 0
    for i in gz_info_58.find():
        if (int(i["time"])==1):
            time_dict["1"]=time_dict["1"]+1
        if (int(i["time"]) == 2 ):
            time_dict["2"] = time_dict["2"] + 1
        if (int(i["time"]) == 3):
            time_dict["3"] = time_dict["3"] + 1
        if (int(i["time"]) == 4):
            time_dict["4"] = time_dict["4"] + 1
        if (int(i["time"]) == 5):
            time_dict["5"] = time_dict["5"] + 1
        if (int(i["time"]) == 6):
            time_dict["6"] = time_dict["6"] + 1

    time_tpye_dict_58 = {}
    time_tpye_dict_58["type"] = []
    time_tpye_dict_58["values"] = []
    for i_key, i_values in time_dict.items():
        time_tpye_dict_58["type"].append(i_key)
        time_tpye_dict_58["values"].append(i_values)

    print(time_tpye_dict_58)
    return time_tpye_dict_58


def rigion_price_cs_58():
    rigion_list = []
    rigion_dict = {}
    a = 0
    for i in cs_info_58.find():
        if (i['house']):
            rigion_list.append(i["rigion"].split()[0])
            a = a + 1
            # print(i["rigion"].split()[0])

    rigion_list_index = list(set(rigion_list))
    for i in rigion_list_index:
        rigion_dict[i] = rigion_list.count(i)

    print(a)
    print(rigion_dict)


    data_dict={}
    data_dict["type"]=[]
    data_dict["values"] = []
    for i_key,i_values in rigion_dict.items():
        data = 0
        for j in cs_info_58.find():
            if(j["rigion"].split()[0]==i_key):
                data = data+int(j["price"])
        data_dict["type"].append(i_key)
        data_dict["values"].append(round(data/i_values,1))

    print(data_dict)








##################################################################wh
def sum_wh_58():#武汉总共有多少数据
    a=0
    for i in wh_info_58.find():
        if(i['house']):
            a=a+1
    sum_58_wh = a
    return sum_58_wh

def type_wh_58():
    a=0
    others=0
    fangzitype_list=[]
    fangzitype_data=[]
    b=[]
    fangzitype_dict={}
    for i in wh_info_58.find():
        if(i['house']):
            #print(i["house"])
            a=a+1
            #print(i["house"]["type"][0:7])
            fangzitype_list.append(i["house"]["type"][0:6])
            #print(i["house"]["decoration"][3:7])
    #print(a)

    fangzitype = list(set(fangzitype_list))
    print(a)
    print(fangzitype)
    for i in fangzitype:#统计各类型房子数
        if(fangzitype_list.count(i)>100):
            b.append(i)
            fangzitype_data.append(fangzitype_list.count(i))
            others=others+fangzitype_list.count(i)

    other = a-others
    fangzitype_dict["type"] = b
    fangzitype_dict["values"]=fangzitype_data
    fangzitype_dict["type"].append("其他")
    fangzitype_dict["values"].append(other)
    print(fangzitype_dict)


    return fangzitype_dict


def price_wh_type_58():
    price_tpye_dict = {}
    price_tpye_dict["500"]=0
    price_tpye_dict["1000"]=0
    price_tpye_dict["1500"]=0
    price_tpye_dict["2000"]=0
    price_tpye_dict["2500"]=0
    price_tpye_dict["3000"]=0
    price_tpye_dict["9999"]=0
    for i in wh_info_58.find():
        if(i['house']):
            if(int(i["price"])<500):
                price_tpye_dict["500"]=price_tpye_dict["500"]+1
            elif(500<int(i["price"])<1000):
                price_tpye_dict["1000"] = price_tpye_dict["1000"] + 1
            elif (1000 < int(i["price"]) < 1500):
                price_tpye_dict["1500"] = price_tpye_dict["1500"] + 1
            elif (1500 < int(i["price"]) < 2000):
                price_tpye_dict["2000"] = price_tpye_dict["2000"] + 1
            elif (2000 < int(i["price"]) < 2500):
                price_tpye_dict["2500"] = price_tpye_dict["2500"] + 1
            elif (2500 < int(i["price"]) < 3000):
                price_tpye_dict["3000"] = price_tpye_dict["3000"] + 1
            else:
                price_tpye_dict["9999"] = price_tpye_dict["9999"] + 1
    print(price_tpye_dict)
    price_tpye_dict_58={}
    price_tpye_dict_58["type"]=[]
    price_tpye_dict_58["values"]=[]
    for i_key,i_values in price_tpye_dict.items():
        price_tpye_dict_58["type"].append(i_key)
        price_tpye_dict_58["values"].append(i_values)

    print(price_tpye_dict_58)
    return price_tpye_dict_58

def pay_wh_method_58():
    pay_method_list=[]
    pay_method_dict={}
    a=0
    for i in wh_info_58.find():
        if(i['house']):
            pay_method_list.append(i["pay_method"])
            a = a+1

    pay_method_index = list(set(pay_method_list))

    for i in pay_method_index:
        pay_method_dict[i] = pay_method_list.count(i)

    print(a)
    print(pay_method_dict)

    method_tpye_dict_58={}
    method_tpye_dict_58["type"]=[]
    method_tpye_dict_58["values"]=[]
    for i_key,i_values in pay_method_dict.items():
        method_tpye_dict_58["type"].append(i_key)
        method_tpye_dict_58["values"].append(i_values)

    print(method_tpye_dict_58)
    return method_tpye_dict_58


def rigion_wh_58():
    rigion_list = []
    rigion_dict = {}
    a = 0
    for i in wh_info_58.find():
        if (i['house']):
            rigion_list.append(i["rigion"].split()[0])
            a=a+1
            #print(i["rigion"].split()[0])

    rigion_list_index = list(set(rigion_list))
    for i in rigion_list_index:
        rigion_dict[i] = rigion_list.count(i)

    print(a)
    print(rigion_dict)

    rigion_tpye_dict_58 = {}
    rigion_tpye_dict_58["type"] = []
    rigion_tpye_dict_58["values"] = []
    for i_key, i_values in rigion_dict.items():
        rigion_tpye_dict_58["type"].append(i_key)
        rigion_tpye_dict_58["values"].append(i_values)

    print(rigion_tpye_dict_58)
    return rigion_dict

def time_wh_58():
    time_dict={}
    time_dict["1"]=0
    time_dict["2"] = 0
    time_dict["3"] = 0
    time_dict["4"] = 0
    time_dict["5"] = 0
    time_dict["6"] = 0
    for i in wh_info_58.find():
        if (int(i["time"])==1):
            time_dict["1"]=time_dict["1"]+1
        if (int(i["time"]) == 2 ):
            time_dict["2"] = time_dict["2"] + 1
        if (int(i["time"]) == 3):
            time_dict["3"] = time_dict["3"] + 1
        if (int(i["time"]) == 4):
            time_dict["4"] = time_dict["4"] + 1
        if (int(i["time"]) == 5):
            time_dict["5"] = time_dict["5"] + 1
        if (int(i["time"]) == 6):
            time_dict["6"] = time_dict["6"] + 1

    time_tpye_dict_58 = {}
    time_tpye_dict_58["type"] = []
    time_tpye_dict_58["values"] = []
    for i_key, i_values in time_dict.items():
        time_tpye_dict_58["type"].append(i_key)
        time_tpye_dict_58["values"].append(i_values)

    print(time_tpye_dict_58)
    return time_tpye_dict_58


def rigion_price_wh_58():
    rigion_list = []
    rigion_dict = {}
    a = 0
    for i in wh_info_58.find():
        if (i['house']):
            rigion_list.append(i["rigion"].split()[0])
            a = a + 1
            # print(i["rigion"].split()[0])

    rigion_list_index = list(set(rigion_list))
    for i in rigion_list_index:
        rigion_dict[i] = rigion_list.count(i)

    print(a)
    print(rigion_dict)


    data_dict={}
    data_dict["type"]=[]
    data_dict["values"] = []
    for i_key,i_values in rigion_dict.items():
        data = 0
        for j in wh_info_58.find():
            if(j["rigion"].split()[0]==i_key):
                data = data+int(j["price"])
        data_dict["type"].append(i_key)
        data_dict["values"].append(round(data/i_values,1))

    print(data_dict)






#############################################################################cd
def sum_cd_58():#武汉总共有多少数据
    a=0
    for i in cd_info_58.find():
        if(i['house']):
            a=a+1
    sum_58_cd = a
    return sum_58_cd

def type_cd_58():
    a=0
    others=0
    fangzitype_list=[]
    fangzitype_data=[]
    b=[]
    fangzitype_dict={}
    for i in cd_info_58.find():
        if(i['house']):
            #print(i["house"])
            a=a+1
            #print(i["house"]["type"][0:7])
            fangzitype_list.append(i["house"]["type"][0:6])
            #print(i["house"]["decoration"][3:7])
    #print(a)

    fangzitype = list(set(fangzitype_list))
    print(a)
    print(fangzitype)
    for i in fangzitype:#统计各类型房子数
        if(fangzitype_list.count(i)>100):
            b.append(i)
            fangzitype_data.append(fangzitype_list.count(i))
            others=others+fangzitype_list.count(i)

    other = a-others
    fangzitype_dict["type"] = b
    fangzitype_dict["values"]=fangzitype_data
    fangzitype_dict["type"].append("其他")
    fangzitype_dict["values"].append(other)
    print(fangzitype_dict)


    return fangzitype_dict


def price_cd_type_58():
    price_tpye_dict = {}
    price_tpye_dict["500"]=0
    price_tpye_dict["1000"]=0
    price_tpye_dict["1500"]=0
    price_tpye_dict["2000"]=0
    price_tpye_dict["2500"]=0
    price_tpye_dict["3000"]=0
    price_tpye_dict["9999"]=0
    for i in cd_info_58.find():
        if(i['house']):
            if(int(i["price"])<500):
                price_tpye_dict["500"]=price_tpye_dict["500"]+1
            elif(500<int(i["price"])<1000):
                price_tpye_dict["1000"] = price_tpye_dict["1000"] + 1
            elif (1000 < int(i["price"]) < 1500):
                price_tpye_dict["1500"] = price_tpye_dict["1500"] + 1
            elif (1500 < int(i["price"]) < 2000):
                price_tpye_dict["2000"] = price_tpye_dict["2000"] + 1
            elif (2000 < int(i["price"]) < 2500):
                price_tpye_dict["2500"] = price_tpye_dict["2500"] + 1
            elif (2500 < int(i["price"]) < 3000):
                price_tpye_dict["3000"] = price_tpye_dict["3000"] + 1
            else:
                price_tpye_dict["9999"] = price_tpye_dict["9999"] + 1
    print(price_tpye_dict)
    price_tpye_dict_58={}
    price_tpye_dict_58["type"]=[]
    price_tpye_dict_58["values"]=[]
    for i_key,i_values in price_tpye_dict.items():
        price_tpye_dict_58["type"].append(i_key)
        price_tpye_dict_58["values"].append(i_values)

    print(price_tpye_dict_58)
    return price_tpye_dict_58



def pay_cd_method_58():
    pay_method_list=[]
    pay_method_dict={}
    a=0
    for i in cd_info_58.find():
        if(i['house']):
            pay_method_list.append(i["pay_method"])
            a = a+1

    pay_method_index = list(set(pay_method_list))

    for i in pay_method_index:
        pay_method_dict[i] = pay_method_list.count(i)

    print(a)
    print(pay_method_dict)

    method_tpye_dict_58={}
    method_tpye_dict_58["type"]=[]
    method_tpye_dict_58["values"]=[]
    for i_key,i_values in pay_method_dict.items():
        method_tpye_dict_58["type"].append(i_key)
        method_tpye_dict_58["values"].append(i_values)

    print(method_tpye_dict_58)
    return method_tpye_dict_58


def rigion_cd_58():
    rigion_list = []
    rigion_dict = {}
    a = 0
    for i in gz_info_58.find():
        if (i['house']):
            rigion_list.append(i["rigion"].split()[0])
            a=a+1
            #print(i["rigion"].split()[0])

    rigion_list_index = list(set(rigion_list))
    for i in rigion_list_index:
        rigion_dict[i] = rigion_list.count(i)

    print(a)
    print(rigion_dict)

    rigion_tpye_dict_58 = {}
    rigion_tpye_dict_58["type"] = []
    rigion_tpye_dict_58["values"] = []
    for i_key, i_values in rigion_dict.items():
        rigion_tpye_dict_58["type"].append(i_key)
        rigion_tpye_dict_58["values"].append(i_values)

    print(rigion_tpye_dict_58)
    return rigion_dict

def time_cd_58():
    time_dict={}
    time_dict["1"]=0
    time_dict["2"] = 0
    time_dict["3"] = 0
    time_dict["4"] = 0
    time_dict["5"] = 0
    time_dict["6"] = 0
    for i in gz_info_58.find():
        if (int(i["time"])==1):
            time_dict["1"]=time_dict["1"]+1
        if (int(i["time"]) == 2 ):
            time_dict["2"] = time_dict["2"] + 1
        if (int(i["time"]) == 3):
            time_dict["3"] = time_dict["3"] + 1
        if (int(i["time"]) == 4):
            time_dict["4"] = time_dict["4"] + 1
        if (int(i["time"]) == 5):
            time_dict["5"] = time_dict["5"] + 1
        if (int(i["time"]) == 6):
            time_dict["6"] = time_dict["6"] + 1

    time_tpye_dict_58 = {}
    time_tpye_dict_58["type"] = []
    time_tpye_dict_58["values"] = []
    for i_key, i_values in time_dict.items():
        time_tpye_dict_58["type"].append(i_key)
        time_tpye_dict_58["values"].append(i_values)

    print(time_tpye_dict_58)
    return time_tpye_dict_58


def rigion_price_cd_58():
    rigion_list = []
    rigion_dict = {}
    a = 0
    for i in cd_info_58.find():
        if (i['house']):
            rigion_list.append(i["rigion"].split()[0])
            a = a + 1
            # print(i["rigion"].split()[0])

    rigion_list_index = list(set(rigion_list))
    for i in rigion_list_index:
        rigion_dict[i] = rigion_list.count(i)

    print(a)
    print(rigion_dict)


    data_dict={}
    data_dict["type"]=[]
    data_dict["values"] = []
    for i_key,i_values in rigion_dict.items():
        data = 0
        for j in cd_info_58.find():
            if(j["rigion"].split()[0]==i_key):
                data = data+int(j["price"])
        data_dict["type"].append(i_key)
        data_dict["values"].append(round(data/i_values,1))

    print(data_dict)






###################################################################################################################上海
def sum_sh_beihe():#上海总共有多少数据
    a=0
    for i in sh_info_beihe.find():
        if(i['house']):
            a=a+1
    sum_58_sh = a
    return sum_58_sh

def type_sh_beihe():
    a=0
    others=0
    fangzitype_list=[]
    fangzitype_data=[]
    b=[]
    fangzitype_dict={}
    for i in sh_info_beihe.find():
        if(i['house']):
            #print(i["house"])
            a=a+1
            #print(i["house"]["type"][0:7])
            fangzitype_list.append(i["house"]["type"][0:6])
            #print(i["house"]["decoration"][3:7])
    #print(a)

    fangzitype = list(set(fangzitype_list))
    print(a)
    print(fangzitype)
    for i in fangzitype:#统计各类型房子数
        if(fangzitype_list.count(i)>100):
            b.append(i)
            fangzitype_data.append(fangzitype_list.count(i))
            others=others+fangzitype_list.count(i)

    other = a-others
    fangzitype_dict["type"] = b
    fangzitype_dict["values"]=fangzitype_data
    fangzitype_dict["type"].append("其他")
    fangzitype_dict["values"].append(other)
    print(fangzitype_dict)


    return fangzitype_dict


def price_sh_type_beihe():
    price_tpye_dict = {}
    price_tpye_dict["500"]=0
    price_tpye_dict["1000"]=0
    price_tpye_dict["1500"]=0
    price_tpye_dict["2000"]=0
    price_tpye_dict["2500"]=0
    price_tpye_dict["3000"]=0
    price_tpye_dict["9999"]=0
    for i in sh_info_beihe.find():
        if(i['house']):
            if(int(i["price"])<500):
                price_tpye_dict["500"]=price_tpye_dict["500"]+1
            elif(500<int(i["price"])<1000):
                price_tpye_dict["1000"] = price_tpye_dict["1000"] + 1
            elif (1000 < int(i["price"]) < 1500):
                price_tpye_dict["1500"] = price_tpye_dict["1500"] + 1
            elif (1500 < int(i["price"]) < 2000):
                price_tpye_dict["2000"] = price_tpye_dict["2000"] + 1
            elif (2000 < int(i["price"]) < 2500):
                price_tpye_dict["2500"] = price_tpye_dict["2500"] + 1
            elif (2500 < int(i["price"]) < 3000):
                price_tpye_dict["3000"] = price_tpye_dict["3000"] + 1
            else:
                price_tpye_dict["9999"] = price_tpye_dict["9999"] + 1
    print(price_tpye_dict)
    price_tpye_dict_58={}
    price_tpye_dict_58["type"]=[]
    price_tpye_dict_58["values"]=[]
    for i_key,i_values in price_tpye_dict.items():
        price_tpye_dict_58["type"].append(i_key)
        price_tpye_dict_58["values"].append(i_values)

    print(price_tpye_dict_58)
    return price_tpye_dict_58

def pay_sh_method_beihe():
    pay_method_list=[]
    pay_method_dict={}
    a=0
    for i in sh_info_beihe.find():
        if(i['house']):
            pay_method_list.append(i["pay_method"])
            a = a+1

    pay_method_index = list(set(pay_method_list))

    for i in pay_method_index:
        pay_method_dict[i] = pay_method_list.count(i)

    print(a)
    print(pay_method_dict)

    method_tpye_dict_58={}
    method_tpye_dict_58["type"]=[]
    method_tpye_dict_58["values"]=[]
    for i_key,i_values in pay_method_dict.items():
        method_tpye_dict_58["type"].append(i_key)
        method_tpye_dict_58["values"].append(i_values)

    print(method_tpye_dict_58)
    return method_tpye_dict_58


def rigion_sh_beihe():
    rigion_list = []
    rigion_dict = {}
    a = 0
    for i in sh_info_beihe.find():
        if (i['house']):
            rigion_list.append(i["rigion"].split()[0])
            a=a+1
            #print(i["rigion"].split()[0])

    rigion_list_index = list(set(rigion_list))
    for i in rigion_list_index:
        rigion_dict[i] = rigion_list.count(i)

    print(a)
    print(rigion_dict)

    rigion_tpye_dict_58 = {}
    rigion_tpye_dict_58["type"] = []
    rigion_tpye_dict_58["values"] = []
    for i_key, i_values in rigion_dict.items():
        rigion_tpye_dict_58["type"].append(i_key)
        rigion_tpye_dict_58["values"].append(i_values)

    print(rigion_tpye_dict_58)
    return rigion_tpye_dict_58

def time_sh_beihe():
    time_dict={}
    time_dict["1"]=0
    time_dict["2"] = 0
    time_dict["3"] = 0
    time_dict["4"] = 0
    time_dict["5"] = 0
    time_dict["6"] = 0
    for i in sh_info_beihe.find():
        if (int(i["time"])==1):
            time_dict["1"]=time_dict["1"]+1
        if (int(i["time"]) == 2 ):
            time_dict["2"] = time_dict["2"] + 1
        if (int(i["time"]) == 3):
            time_dict["3"] = time_dict["3"] + 1
        if (int(i["time"]) == 4):
            time_dict["4"] = time_dict["4"] + 1
        if (int(i["time"]) == 5):
            time_dict["5"] = time_dict["5"] + 1
        if (int(i["time"]) == 6):
            time_dict["6"] = time_dict["6"] + 1

    time_tpye_dict_58 = {}
    time_tpye_dict_58["type"] = []
    time_tpye_dict_58["values"] = []
    for i_key, i_values in time_dict.items():
        time_tpye_dict_58["type"].append(i_key)
        time_tpye_dict_58["values"].append(i_values)

    print(time_tpye_dict_58)
    return time_tpye_dict_58


def rigion_price_sh_beihe():
    rigion_list = []
    rigion_dict = {}
    a = 0
    for i in sh_info_beihe.find():
        if (i['house']):
            rigion_list.append(i["rigion"].split()[0])
            a = a + 1
            # print(i["rigion"].split()[0])

    rigion_list_index = list(set(rigion_list))
    for i in rigion_list_index:
        rigion_dict[i] = rigion_list.count(i)

    print(a)
    print(rigion_dict)


    data_dict={}
    data_dict["type"]=[]
    data_dict["values"] = []
    for i_key,i_values in rigion_dict.items():
        data = 0
        for j in sh_info_beihe.find():
            if(j["rigion"].split()[0]==i_key):
                data = data+int(j["price"])
        data_dict["type"].append(i_key)
        data_dict["values"].append(round(data/i_values,1))

    print(data_dict)












############################################################################################gz
def sum_gz_beihe():#广州总共有多少数据
    a=0
    for i in beihe_info_58.find():
        if(i['house']):
            a=a+1
    sum_58_gz = a
    return sum_58_gz


def type_gz_beihe():
    a=0
    others=0
    fangzitype_list=[]
    fangzitype_data=[]
    b=[]
    fangzitype_dict={}
    for i in gz_info_beihe.find():
        if(i['house']):
            #print(i["house"])
            a=a+1
            #print(i["house"]["type"][0:7])
            fangzitype_list.append(i["house"]["type"][0:6])
            #print(i["house"]["decoration"][3:7])
    #print(a)

    fangzitype = list(set(fangzitype_list))
    print(a)
    print(fangzitype)
    for i in fangzitype:#统计各类型房子数
        if(fangzitype_list.count(i)>100):
            b.append(i)
            fangzitype_data.append(fangzitype_list.count(i))
            others=others+fangzitype_list.count(i)

    other = a-others
    fangzitype_dict["type"] = b
    fangzitype_dict["values"]=fangzitype_data
    fangzitype_dict["type"].append("其他")
    fangzitype_dict["values"].append(other)
    print(fangzitype_dict)


    return fangzitype_dict


def price_gz_type_beihe():
    price_tpye_dict = {}
    price_tpye_dict["500"]=0
    price_tpye_dict["1000"]=0
    price_tpye_dict["1500"]=0
    price_tpye_dict["2000"]=0
    price_tpye_dict["2500"]=0
    price_tpye_dict["3000"]=0
    price_tpye_dict["9999"]=0
    for i in gz_info_beihe.find():
        if(i['house']):
            if(int(i["price"])<500):
                price_tpye_dict["500"]=price_tpye_dict["500"]+1
            elif(500<int(i["price"])<1000):
                price_tpye_dict["1000"] = price_tpye_dict["1000"] + 1
            elif (1000 < int(i["price"]) < 1500):
                price_tpye_dict["1500"] = price_tpye_dict["1500"] + 1
            elif (1500 < int(i["price"]) < 2000):
                price_tpye_dict["2000"] = price_tpye_dict["2000"] + 1
            elif (2000 < int(i["price"]) < 2500):
                price_tpye_dict["2500"] = price_tpye_dict["2500"] + 1
            elif (2500 < int(i["price"]) < 3000):
                price_tpye_dict["3000"] = price_tpye_dict["3000"] + 1
            else:
                price_tpye_dict["9999"] = price_tpye_dict["9999"] + 1
    print(price_tpye_dict)
    price_tpye_dict_58={}
    price_tpye_dict_58["type"]=[]
    price_tpye_dict_58["values"]=[]
    for i_key,i_values in price_tpye_dict.items():
        price_tpye_dict_58["type"].append(i_key)
        price_tpye_dict_58["values"].append(i_values)

    print(price_tpye_dict_58)
    return price_tpye_dict_58

def pay_gz_method_beihe():
    pay_method_list=[]
    pay_method_dict={}
    a=0
    for i in gz_info_beihe.find():
        if(i['house']):
            pay_method_list.append(i["pay_method"])
            a = a+1

    pay_method_index = list(set(pay_method_list))

    for i in pay_method_index:
        pay_method_dict[i] = pay_method_list.count(i)

    print(a)
    print(pay_method_dict)

    method_tpye_dict_58={}
    method_tpye_dict_58["type"]=[]
    method_tpye_dict_58["values"]=[]
    for i_key,i_values in pay_method_dict.items():
        method_tpye_dict_58["type"].append(i_key)
        method_tpye_dict_58["values"].append(i_values)

    print(method_tpye_dict_58)
    return method_tpye_dict_58


def rigion_gz_beihe():
    rigion_list = []
    rigion_dict = {}
    a = 0
    for i in gz_info_beihe.find():
        if (i['house']):
            rigion_list.append(i["rigion"].split()[0])
            a=a+1
            #print(i["rigion"].split()[0])

    rigion_list_index = list(set(rigion_list))
    for i in rigion_list_index:
        rigion_dict[i] = rigion_list.count(i)

    print(a)
    print(rigion_dict)

    rigion_tpye_dict_58 = {}
    rigion_tpye_dict_58["type"] = []
    rigion_tpye_dict_58["values"] = []
    for i_key, i_values in rigion_dict.items():
        rigion_tpye_dict_58["type"].append(i_key)
        rigion_tpye_dict_58["values"].append(i_values)

    print(rigion_tpye_dict_58)
    return rigion_dict

def time_gz_beihe():
    time_dict={}
    time_dict["1"]=0
    time_dict["2"] = 0
    time_dict["3"] = 0
    time_dict["4"] = 0
    time_dict["5"] = 0
    time_dict["6"] = 0
    for i in gz_info_beihe.find():
        if (int(i["time"])==1):
            time_dict["1"]=time_dict["1"]+1
        if (int(i["time"]) == 2 ):
            time_dict["2"] = time_dict["2"] + 1
        if (int(i["time"]) == 3):
            time_dict["3"] = time_dict["3"] + 1
        if (int(i["time"]) == 4):
            time_dict["4"] = time_dict["4"] + 1
        if (int(i["time"]) == 5):
            time_dict["5"] = time_dict["5"] + 1
        if (int(i["time"]) == 6):
            time_dict["6"] = time_dict["6"] + 1

    time_tpye_dict_58 = {}
    time_tpye_dict_58["type"] = []
    time_tpye_dict_58["values"] = []
    for i_key, i_values in time_dict.items():
        time_tpye_dict_58["type"].append(i_key)
        time_tpye_dict_58["values"].append(i_values)

    print(time_tpye_dict_58)
    return time_tpye_dict_58


def rigion_price_gz_beihe():
    rigion_list = []
    rigion_dict = {}
    a = 0
    for i in gz_info_beihe.find():
        if (i['house']):
            rigion_list.append(i["rigion"].split()[0])
            a = a + 1
            # print(i["rigion"].split()[0])

    rigion_list_index = list(set(rigion_list))
    for i in rigion_list_index:
        rigion_dict[i] = rigion_list.count(i)

    print(a)
    print(rigion_dict)


    data_dict={}
    data_dict["type"]=[]
    data_dict["values"] = []
    for i_key,i_values in rigion_dict.items():
        data = 0
        for j in gz_info_beihe.find():
            if(j["rigion"].split()[0]==i_key):
                data = data+int(j["price"])
        data_dict["type"].append(i_key)
        data_dict["values"].append(round(data/i_values,1))

    print(data_dict)





#####bj
def sum_bj_beihe():#北京总共有多少数据
    a=0
    for i in bj_info_beihe.find():
        if(i['house']):
            a=a+1
    sum_58_bj = a
    return sum_58_bj

def type_bj_beihe():
    a=0
    others=0
    fangzitype_list=[]
    fangzitype_data=[]
    b=[]
    fangzitype_dict={}
    for i in bj_info_beihe.find():
        if(i['house']):
            #print(i["house"])
            a=a+1
            #print(i["house"]["type"][0:7])
            fangzitype_list.append(i["house"]["type"][0:6])
            #print(i["house"]["decoration"][3:7])
    #print(a)

    fangzitype = list(set(fangzitype_list))
    print(a)
    print(fangzitype)
    for i in fangzitype:#统计各类型房子数
        if(fangzitype_list.count(i)>100):
            b.append(i)
            fangzitype_data.append(fangzitype_list.count(i))
            others=others+fangzitype_list.count(i)

    other = a-others
    fangzitype_dict["type"] = b
    fangzitype_dict["values"]=fangzitype_data
    fangzitype_dict["type"].append("其他")
    fangzitype_dict["values"].append(other)
    print(fangzitype_dict)


    return fangzitype_dict


def price_bj_type_beihe():
    price_tpye_dict = {}
    price_tpye_dict["500"]=0
    price_tpye_dict["1000"]=0
    price_tpye_dict["1500"]=0
    price_tpye_dict["2000"]=0
    price_tpye_dict["2500"]=0
    price_tpye_dict["3000"]=0
    price_tpye_dict["9999"]=0
    for i in bj_info_beihe.find():
        if(i['house']):
            if(int(i["price"])<500):
                price_tpye_dict["500"]=price_tpye_dict["500"]+1
            elif(500<int(i["price"])<1000):
                price_tpye_dict["1000"] = price_tpye_dict["1000"] + 1
            elif (1000 < int(i["price"]) < 1500):
                price_tpye_dict["1500"] = price_tpye_dict["1500"] + 1
            elif (1500 < int(i["price"]) < 2000):
                price_tpye_dict["2000"] = price_tpye_dict["2000"] + 1
            elif (2000 < int(i["price"]) < 2500):
                price_tpye_dict["2500"] = price_tpye_dict["2500"] + 1
            elif (2500 < int(i["price"]) < 3000):
                price_tpye_dict["3000"] = price_tpye_dict["3000"] + 1
            else:
                price_tpye_dict["9999"] = price_tpye_dict["9999"] + 1
    print(price_tpye_dict)
    price_tpye_dict_58={}
    price_tpye_dict_58["type"]=[]
    price_tpye_dict_58["values"]=[]
    for i_key,i_values in price_tpye_dict.items():
        price_tpye_dict_58["type"].append(i_key)
        price_tpye_dict_58["values"].append(i_values)

    print(price_tpye_dict_58)
    return price_tpye_dict_58

def pay_bj_method_beihe():
    pay_method_list=[]
    pay_method_dict={}
    a=0
    for i in bj_info_beihe.find():
        if(i['house']):
            pay_method_list.append(i["pay_method"])
            a = a+1

    pay_method_index = list(set(pay_method_list))

    for i in pay_method_index:
        pay_method_dict[i] = pay_method_list.count(i)

    print(a)
    print(pay_method_dict)

    method_tpye_dict_58={}
    method_tpye_dict_58["type"]=[]
    method_tpye_dict_58["values"]=[]
    for i_key,i_values in pay_method_dict.items():
        method_tpye_dict_58["type"].append(i_key)
        method_tpye_dict_58["values"].append(i_values)

    print(method_tpye_dict_58)
    return method_tpye_dict_58


def rigion_bj_beihe():
    rigion_list = []
    rigion_dict = {}
    a = 0
    for i in bj_info_beihe.find():
        if (i['house']):
            rigion_list.append(i["rigion"].split()[0])
            a=a+1
            #print(i["rigion"].split()[0])

    rigion_list_index = list(set(rigion_list))
    for i in rigion_list_index:
        rigion_dict[i] = rigion_list.count(i)

    print(a)
    print(rigion_dict)

    rigion_tpye_dict_58 = {}
    rigion_tpye_dict_58["type"] = []
    rigion_tpye_dict_58["values"] = []
    for i_key, i_values in rigion_dict.items():
        rigion_tpye_dict_58["type"].append(i_key)
        rigion_tpye_dict_58["values"].append(i_values)

    print(rigion_tpye_dict_58)
    return rigion_dict

def time_bj_beihe():
    time_dict={}
    time_dict["1"]=0
    time_dict["2"] = 0
    time_dict["3"] = 0
    time_dict["4"] = 0
    time_dict["5"] = 0
    time_dict["6"] = 0
    for i in bj_info_beihe.find():
        if (int(i["time"])==1):
            time_dict["1"]=time_dict["1"]+1
        if (int(i["time"]) == 2 ):
            time_dict["2"] = time_dict["2"] + 1
        if (int(i["time"]) == 3):
            time_dict["3"] = time_dict["3"] + 1
        if (int(i["time"]) == 4):
            time_dict["4"] = time_dict["4"] + 1
        if (int(i["time"]) == 5):
            time_dict["5"] = time_dict["5"] + 1
        if (int(i["time"]) == 6):
            time_dict["6"] = time_dict["6"] + 1

    time_tpye_dict_58 = {}
    time_tpye_dict_58["type"] = []
    time_tpye_dict_58["values"] = []
    for i_key, i_values in time_dict.items():
        time_tpye_dict_58["type"].append(i_key)
        time_tpye_dict_58["values"].append(i_values)

    print(time_tpye_dict_58)
    return time_tpye_dict_58


def rigion_price_bj_beihe():
    rigion_list = []
    rigion_dict = {}
    a = 0
    for i in bj_info_beihe.find():
        if (i['house']):
            rigion_list.append(i["rigion"].split()[0])
            a = a + 1
            # print(i["rigion"].split()[0])

    rigion_list_index = list(set(rigion_list))
    for i in rigion_list_index:
        rigion_dict[i] = rigion_list.count(i)

    print(a)
    print(rigion_dict)


    data_dict={}
    data_dict["type"]=[]
    data_dict["values"] = []
    for i_key,i_values in rigion_dict.items():
        data = 0
        for j in bj_info_beihe.find():
            if(j["rigion"].split()[0]==i_key):
                data = data+int(j["price"])
        data_dict["type"].append(i_key)
        data_dict["values"].append(round(data/i_values,1))

    print(data_dict)







################################################################################cs
def sum_cs_beihe():#长沙总共有多少数据
    a=0
    for i in cs_info_beihe.find():
        if(i['house']):
            a=a+1
    sum_58_cs = a
    return sum_58_cs

def type_cs_beihe():
    a=0
    others=0
    fangzitype_list=[]
    fangzitype_data=[]
    b=[]
    fangzitype_dict={}
    for i in cs_info_beihe.find():
        if(i['house']):
            #print(i["house"])
            a=a+1
            #print(i["house"]["type"][0:7])
            fangzitype_list.append(i["house"]["type"][0:6])
            #print(i["house"]["decoration"][3:7])
    #print(a)

    fangzitype = list(set(fangzitype_list))
    print(a)
    print(fangzitype)
    for i in fangzitype:#统计各类型房子数
        if(fangzitype_list.count(i)>100):
            b.append(i)
            fangzitype_data.append(fangzitype_list.count(i))
            others=others+fangzitype_list.count(i)

    other = a-others
    fangzitype_dict["type"] = b
    fangzitype_dict["values"]=fangzitype_data
    fangzitype_dict["type"].append("其他")
    fangzitype_dict["values"].append(other)
    print(fangzitype_dict)


    return fangzitype_dict


def price_cs_type_beihe():
    price_tpye_dict = {}
    price_tpye_dict["500"]=0
    price_tpye_dict["1000"]=0
    price_tpye_dict["1500"]=0
    price_tpye_dict["2000"]=0
    price_tpye_dict["2500"]=0
    price_tpye_dict["3000"]=0
    price_tpye_dict["9999"]=0
    for i in cs_info_beihe.find():
        if(i['house']):
            if(int(i["price"])<500):
                price_tpye_dict["500"]=price_tpye_dict["500"]+1
            elif(500<int(i["price"])<1000):
                price_tpye_dict["1000"] = price_tpye_dict["1000"] + 1
            elif (1000 < int(i["price"]) < 1500):
                price_tpye_dict["1500"] = price_tpye_dict["1500"] + 1
            elif (1500 < int(i["price"]) < 2000):
                price_tpye_dict["2000"] = price_tpye_dict["2000"] + 1
            elif (2000 < int(i["price"]) < 2500):
                price_tpye_dict["2500"] = price_tpye_dict["2500"] + 1
            elif (2500 < int(i["price"]) < 3000):
                price_tpye_dict["3000"] = price_tpye_dict["3000"] + 1
            else:
                price_tpye_dict["9999"] = price_tpye_dict["9999"] + 1
    print(price_tpye_dict)
    price_tpye_dict_58={}
    price_tpye_dict_58["type"]=[]
    price_tpye_dict_58["values"]=[]
    for i_key,i_values in price_tpye_dict.items():
        price_tpye_dict_58["type"].append(i_key)
        price_tpye_dict_58["values"].append(i_values)

    print(price_tpye_dict_58)
    return price_tpye_dict_58

def pay_cs_method_beihe():
    pay_method_list=[]
    pay_method_dict={}
    a=0
    for i in cs_info_beihe.find():
        if(i['house']):
            pay_method_list.append(i["pay_method"])
            a = a+1

    pay_method_index = list(set(pay_method_list))

    for i in pay_method_index:
        pay_method_dict[i] = pay_method_list.count(i)

    print(a)
    print(pay_method_dict)

    method_tpye_dict_58={}
    method_tpye_dict_58["type"]=[]
    method_tpye_dict_58["values"]=[]
    for i_key,i_values in pay_method_dict.items():
        method_tpye_dict_58["type"].append(i_key)
        method_tpye_dict_58["values"].append(i_values)

    print(method_tpye_dict_58)
    return method_tpye_dict_58


def rigion_cs_beihe():
    rigion_list = []
    rigion_dict = {}
    a = 0
    for i in cs_info_beihe.find():
        if (i['house']):
            rigion_list.append(i["rigion"].split()[0])
            a=a+1
            #print(i["rigion"].split()[0])

    rigion_list_index = list(set(rigion_list))
    for i in rigion_list_index:
        rigion_dict[i] = rigion_list.count(i)

    print(a)
    print(rigion_dict)

    rigion_tpye_dict_58 = {}
    rigion_tpye_dict_58["type"] = []
    rigion_tpye_dict_58["values"] = []
    for i_key, i_values in rigion_dict.items():
        rigion_tpye_dict_58["type"].append(i_key)
        rigion_tpye_dict_58["values"].append(i_values)

    print(rigion_tpye_dict_58)
    return rigion_dict

def time_cs_beihe():
    time_dict={}
    time_dict["1"]=0
    time_dict["2"] = 0
    time_dict["3"] = 0
    time_dict["4"] = 0
    time_dict["5"] = 0
    time_dict["6"] = 0
    for i in gz_info_beihe.find():
        if (int(i["time"])==1):
            time_dict["1"]=time_dict["1"]+1
        if (int(i["time"]) == 2 ):
            time_dict["2"] = time_dict["2"] + 1
        if (int(i["time"]) == 3):
            time_dict["3"] = time_dict["3"] + 1
        if (int(i["time"]) == 4):
            time_dict["4"] = time_dict["4"] + 1
        if (int(i["time"]) == 5):
            time_dict["5"] = time_dict["5"] + 1
        if (int(i["time"]) == 6):
            time_dict["6"] = time_dict["6"] + 1

    time_tpye_dict_58 = {}
    time_tpye_dict_58["type"] = []
    time_tpye_dict_58["values"] = []
    for i_key, i_values in time_dict.items():
        time_tpye_dict_58["type"].append(i_key)
        time_tpye_dict_58["values"].append(i_values)

    print(time_tpye_dict_58)
    return time_tpye_dict_58


def rigion_price_cs_beihe():
    rigion_list = []
    rigion_dict = {}
    a = 0
    for i in cs_info_beihe.find():
        if (i['house']):
            rigion_list.append(i["rigion"].split()[0])
            a = a + 1
            # print(i["rigion"].split()[0])

    rigion_list_index = list(set(rigion_list))
    for i in rigion_list_index:
        rigion_dict[i] = rigion_list.count(i)

    print(a)
    print(rigion_dict)


    data_dict={}
    data_dict["type"]=[]
    data_dict["values"] = []
    for i_key,i_values in rigion_dict.items():
        data = 0
        for j in cs_info_beihe.find():
            if(j["rigion"].split()[0]==i_key):
                data = data+int(j["price"])
        data_dict["type"].append(i_key)
        data_dict["values"].append(round(data/i_values,1))

    print(data_dict)








##################################################################wh
def sum_wh_beihe():#武汉总共有多少数据
    a=0
    for i in wh_info_beihe.find():
        if(i['house']):
            a=a+1
    sum_58_wh = a
    return sum_58_wh

def type_wh_beihe():
    a=0
    others=0
    fangzitype_list=[]
    fangzitype_data=[]
    b=[]
    fangzitype_dict={}
    for i in wh_info_beihe.find():
        if(i['house']):
            #print(i["house"])
            a=a+1
            #print(i["house"]["type"][0:7])
            fangzitype_list.append(i["house"]["type"][0:6])
            #print(i["house"]["decoration"][3:7])
    #print(a)

    fangzitype = list(set(fangzitype_list))
    print(a)
    print(fangzitype)
    for i in fangzitype:#统计各类型房子数
        if(fangzitype_list.count(i)>100):
            b.append(i)
            fangzitype_data.append(fangzitype_list.count(i))
            others=others+fangzitype_list.count(i)

    other = a-others
    fangzitype_dict["type"] = b
    fangzitype_dict["values"]=fangzitype_data
    fangzitype_dict["type"].append("其他")
    fangzitype_dict["values"].append(other)
    print(fangzitype_dict)


    return fangzitype_dict


def price_wh_type_beihe():
    price_tpye_dict = {}
    price_tpye_dict["500"]=0
    price_tpye_dict["1000"]=0
    price_tpye_dict["1500"]=0
    price_tpye_dict["2000"]=0
    price_tpye_dict["2500"]=0
    price_tpye_dict["3000"]=0
    price_tpye_dict["9999"]=0
    for i in wh_info_beihe.find():
        if(i['house']):
            if(int(i["price"])<500):
                price_tpye_dict["500"]=price_tpye_dict["500"]+1
            elif(500<int(i["price"])<1000):
                price_tpye_dict["1000"] = price_tpye_dict["1000"] + 1
            elif (1000 < int(i["price"]) < 1500):
                price_tpye_dict["1500"] = price_tpye_dict["1500"] + 1
            elif (1500 < int(i["price"]) < 2000):
                price_tpye_dict["2000"] = price_tpye_dict["2000"] + 1
            elif (2000 < int(i["price"]) < 2500):
                price_tpye_dict["2500"] = price_tpye_dict["2500"] + 1
            elif (2500 < int(i["price"]) < 3000):
                price_tpye_dict["3000"] = price_tpye_dict["3000"] + 1
            else:
                price_tpye_dict["9999"] = price_tpye_dict["9999"] + 1
    print(price_tpye_dict)
    price_tpye_dict_58={}
    price_tpye_dict_58["type"]=[]
    price_tpye_dict_58["values"]=[]
    for i_key,i_values in price_tpye_dict.items():
        price_tpye_dict_58["type"].append(i_key)
        price_tpye_dict_58["values"].append(i_values)

    print(price_tpye_dict_58)
    return price_tpye_dict_58

def pay_wh_method_beihe():
    pay_method_list=[]
    pay_method_dict={}
    a=0
    for i in wh_info_beihe.find():
        if(i['house']):
            pay_method_list.append(i["pay_method"])
            a = a+1

    pay_method_index = list(set(pay_method_list))

    for i in pay_method_index:
        pay_method_dict[i] = pay_method_list.count(i)

    print(a)
    print(pay_method_dict)

    method_tpye_dict_58={}
    method_tpye_dict_58["type"]=[]
    method_tpye_dict_58["values"]=[]
    for i_key,i_values in pay_method_dict.items():
        method_tpye_dict_58["type"].append(i_key)
        method_tpye_dict_58["values"].append(i_values)

    print(method_tpye_dict_58)
    return method_tpye_dict_58


def rigion_wh_beihe():
    rigion_list = []
    rigion_dict = {}
    a = 0
    for i in wh_info_beihe.find():
        if (i['house']):
            rigion_list.append(i["rigion"].split()[0])
            a=a+1
            #print(i["rigion"].split()[0])

    rigion_list_index = list(set(rigion_list))
    for i in rigion_list_index:
        rigion_dict[i] = rigion_list.count(i)

    print(a)
    print(rigion_dict)

    rigion_tpye_dict_58 = {}
    rigion_tpye_dict_58["type"] = []
    rigion_tpye_dict_58["values"] = []
    for i_key, i_values in rigion_dict.items():
        rigion_tpye_dict_58["type"].append(i_key)
        rigion_tpye_dict_58["values"].append(i_values)

    print(rigion_tpye_dict_58)
    return rigion_dict

def time_wh_beihe():
    time_dict={}
    time_dict["1"]=0
    time_dict["2"] = 0
    time_dict["3"] = 0
    time_dict["4"] = 0
    time_dict["5"] = 0
    time_dict["6"] = 0
    for i in wh_info_beihe.find():
        if (int(i["time"])==1):
            time_dict["1"]=time_dict["1"]+1
        if (int(i["time"]) == 2 ):
            time_dict["2"] = time_dict["2"] + 1
        if (int(i["time"]) == 3):
            time_dict["3"] = time_dict["3"] + 1
        if (int(i["time"]) == 4):
            time_dict["4"] = time_dict["4"] + 1
        if (int(i["time"]) == 5):
            time_dict["5"] = time_dict["5"] + 1
        if (int(i["time"]) == 6):
            time_dict["6"] = time_dict["6"] + 1

    time_tpye_dict_58 = {}
    time_tpye_dict_58["type"] = []
    time_tpye_dict_58["values"] = []
    for i_key, i_values in time_dict.items():
        time_tpye_dict_58["type"].append(i_key)
        time_tpye_dict_58["values"].append(i_values)

    print(time_tpye_dict_58)
    return time_tpye_dict_58


def rigion_price_wh_beihe():
    rigion_list = []
    rigion_dict = {}
    a = 0
    for i in wh_info_beihe.find():
        if (i['house']):
            rigion_list.append(i["rigion"].split()[0])
            a = a + 1
            # print(i["rigion"].split()[0])

    rigion_list_index = list(set(rigion_list))
    for i in rigion_list_index:
        rigion_dict[i] = rigion_list.count(i)

    print(a)
    print(rigion_dict)


    data_dict={}
    data_dict["type"]=[]
    data_dict["values"] = []
    for i_key,i_values in rigion_dict.items():
        data = 0
        for j in wh_info_beihe.find():
            if(j["rigion"].split()[0]==i_key):
                data = data+int(j["price"])
        data_dict["type"].append(i_key)
        data_dict["values"].append(round(data/i_values,1))

    print(data_dict)






#############################################################################cd
def sum_cd_beihe():#武汉总共有多少数据
    a=0
    for i in cd_info_beihe.find():
        if(i['house']):
            a=a+1
    sum_58_cd = a
    return sum_58_cd

def type_cd_beihe():
    a=0
    others=0
    fangzitype_list=[]
    fangzitype_data=[]
    b=[]
    fangzitype_dict={}
    for i in cd_info_beihe.find():
        if(i['house']):
            #print(i["house"])
            a=a+1
            #print(i["house"]["type"][0:7])
            fangzitype_list.append(i["house"]["type"][0:6])
            #print(i["house"]["decoration"][3:7])
    #print(a)

    fangzitype = list(set(fangzitype_list))
    print(a)
    print(fangzitype)
    for i in fangzitype:#统计各类型房子数
        if(fangzitype_list.count(i)>100):
            b.append(i)
            fangzitype_data.append(fangzitype_list.count(i))
            others=others+fangzitype_list.count(i)

    other = a-others
    fangzitype_dict["type"] = b
    fangzitype_dict["values"]=fangzitype_data
    fangzitype_dict["type"].append("其他")
    fangzitype_dict["values"].append(other)
    print(fangzitype_dict)


    return fangzitype_dict


def price_cd_type_beihe():
    price_tpye_dict = {}
    price_tpye_dict["500"]=0
    price_tpye_dict["1000"]=0
    price_tpye_dict["1500"]=0
    price_tpye_dict["2000"]=0
    price_tpye_dict["2500"]=0
    price_tpye_dict["3000"]=0
    price_tpye_dict["9999"]=0
    for i in cd_info_beihe.find():
        if(i['house']):
            if(int(i["price"])<500):
                price_tpye_dict["500"]=price_tpye_dict["500"]+1
            elif(500<int(i["price"])<1000):
                price_tpye_dict["1000"] = price_tpye_dict["1000"] + 1
            elif (1000 < int(i["price"]) < 1500):
                price_tpye_dict["1500"] = price_tpye_dict["1500"] + 1
            elif (1500 < int(i["price"]) < 2000):
                price_tpye_dict["2000"] = price_tpye_dict["2000"] + 1
            elif (2000 < int(i["price"]) < 2500):
                price_tpye_dict["2500"] = price_tpye_dict["2500"] + 1
            elif (2500 < int(i["price"]) < 3000):
                price_tpye_dict["3000"] = price_tpye_dict["3000"] + 1
            else:
                price_tpye_dict["9999"] = price_tpye_dict["9999"] + 1
    print(price_tpye_dict)
    price_tpye_dict_58={}
    price_tpye_dict_58["type"]=[]
    price_tpye_dict_58["values"]=[]
    for i_key,i_values in price_tpye_dict.items():
        price_tpye_dict_58["type"].append(i_key)
        price_tpye_dict_58["values"].append(i_values)

    print(price_tpye_dict_58)
    return price_tpye_dict_58



def pay_cd_method_beihe():
    pay_method_list=[]
    pay_method_dict={}
    a=0
    for i in cd_info_beihe.find():
        if(i['house']):
            pay_method_list.append(i["pay_method"])
            a = a+1

    pay_method_index = list(set(pay_method_list))

    for i in pay_method_index:
        pay_method_dict[i] = pay_method_list.count(i)

    print(a)
    print(pay_method_dict)

    method_tpye_dict_58={}
    method_tpye_dict_58["type"]=[]
    method_tpye_dict_58["values"]=[]
    for i_key,i_values in pay_method_dict.items():
        method_tpye_dict_58["type"].append(i_key)
        method_tpye_dict_58["values"].append(i_values)

    print(method_tpye_dict_58)
    return method_tpye_dict_58


def rigion_cd_beihe():
    rigion_list = []
    rigion_dict = {}
    a = 0
    for i in gz_info_beihe.find():
        if (i['house']):
            rigion_list.append(i["rigion"].split()[0])
            a=a+1
            #print(i["rigion"].split()[0])

    rigion_list_index = list(set(rigion_list))
    for i in rigion_list_index:
        rigion_dict[i] = rigion_list.count(i)

    print(a)
    print(rigion_dict)

    rigion_tpye_dict_58 = {}
    rigion_tpye_dict_58["type"] = []
    rigion_tpye_dict_58["values"] = []
    for i_key, i_values in rigion_dict.items():
        rigion_tpye_dict_58["type"].append(i_key)
        rigion_tpye_dict_58["values"].append(i_values)

    print(rigion_tpye_dict_58)
    return rigion_dict

def time_cd_beihe():
    time_dict={}
    time_dict["1"]=0
    time_dict["2"] = 0
    time_dict["3"] = 0
    time_dict["4"] = 0
    time_dict["5"] = 0
    time_dict["6"] = 0
    for i in gz_info_beihe.find():
        if (int(i["time"])==1):
            time_dict["1"]=time_dict["1"]+1
        if (int(i["time"]) == 2 ):
            time_dict["2"] = time_dict["2"] + 1
        if (int(i["time"]) == 3):
            time_dict["3"] = time_dict["3"] + 1
        if (int(i["time"]) == 4):
            time_dict["4"] = time_dict["4"] + 1
        if (int(i["time"]) == 5):
            time_dict["5"] = time_dict["5"] + 1
        if (int(i["time"]) == 6):
            time_dict["6"] = time_dict["6"] + 1

    time_tpye_dict_58 = {}
    time_tpye_dict_58["type"] = []
    time_tpye_dict_58["values"] = []
    for i_key, i_values in time_dict.items():
        time_tpye_dict_58["type"].append(i_key)
        time_tpye_dict_58["values"].append(i_values)

    print(time_tpye_dict_58)
    return time_tpye_dict_58


def rigion_price_cd_beihe():
    rigion_list = []
    rigion_dict = {}
    a = 0
    for i in cd_info_beihe.find():
        if (i['house']):
            rigion_list.append(i["rigion"].split()[0])
            a = a + 1
            # print(i["rigion"].split()[0])

    rigion_list_index = list(set(rigion_list))
    for i in rigion_list_index:
        rigion_dict[i] = rigion_list.count(i)

    print(a)
    print(rigion_dict)


    data_dict={}
    data_dict["type"]=[]
    data_dict["values"] = []
    for i_key,i_values in rigion_dict.items():
        data = 0
        for j in cd_info_beihe.find():
            if(j["rigion"].split()[0]==i_key):
                data = data+int(j["price"])
        data_dict["type"].append(i_key)
        data_dict["values"].append(round(data/i_values,1))

    print(data_dict)





########################matlib画图

if __name__ == '__main__':
    pay_cs_method_58()
    pay_cs_method_beihe()
