
from django.shortcuts import render

from django.http import FileResponse

from django_web import keshihua
from django_web.models import *
import xlsxwriter
import xlrd
import os
import pymongo
from django_web.testpng import *
from django.core.files.uploadedfile import InMemoryUploadedFile



def index(request):
    return render(request,'index.html')


def bj(request):
    data_bj={}
    data = keshihua.type_bj_58()
    data1=keshihua.type_bj_beihe()
    data2=keshihua.type_bj_beihe()
    print(data1["type"])
    data_bj={'type':data["type"], 'values':data["values"],
                   'type_bj_58':data1["type"],'values_bj_58':data1["values"],
                   }
    data_bj["price_bj_type_58"]=keshihua.price_bj_type_58()["type"]
    data_bj["price_bj_values_58"] = keshihua.price_bj_type_58()["values"]

    data_bj["price_bj_type_beihe"] = keshihua.price_bj_type_beihe()["type"]
    data_bj["price_bj_values_beihe"] = keshihua.price_bj_type_beihe()["values"]

    data_bj["pay_bj_method_58"] = keshihua.pay_bj_method_58()["type"]
    data_bj["pay_bj_method_58_vlaues"] = keshihua.pay_bj_method_58()["values"]

    data_bj["pay_bj_method_beihe"] = keshihua.pay_bj_method_beihe()["type"]
    data_bj["pay_bj_method_beihe_vlaues"] = keshihua.pay_bj_method_beihe()["values"]

    data_bj["time_bj_58"] = keshihua.time_bj_58()["type"]
    data_bj["time_bj_58_vlaues"] = keshihua.time_sh_58()["values"]

    data_bj["time_bj_beihe"] = keshihua.time_bj_beihe()["type"]
    data_bj["time_bj_behei_vlaues"] = keshihua.time_bj_beihe()["values"]


    return render(request,'bj.html',data_bj)

def sh(request):
    data = keshihua.type_sh_58()
    data1 = keshihua.type_sh_beihe()
    data2 = keshihua.type_sh_beihe()
    print(data1["type"])
    data_bj = {'type': data["type"], 'values': data["values"],
               'type_bj_58': data1["type"], 'values_bj_58': data1["values"],
               }
    data_bj["price_bj_type_58"] = keshihua.price_sh_type_58()["type"]
    data_bj["price_bj_values_58"] = keshihua.price_sh_type_58()["values"]

    data_bj["price_bj_type_beihe"] = keshihua.price_sh_type_beihe()["type"]
    data_bj["price_bj_values_beihe"] = keshihua.price_sh_type_beihe()["values"]

    data_bj["pay_bj_method_58"] = keshihua.pay_sh_method_58()["type"]
    data_bj["pay_bj_method_58_vlaues"] = keshihua.pay_sh_method_58()["values"]

    data_bj["pay_bj_method_beihe"] = keshihua.pay_sh_method_beihe()["type"]
    data_bj["pay_bj_method_beihe_vlaues"] = keshihua.pay_sh_method_beihe()["values"]

    data_bj["time_bj_58"] = keshihua.time_sh_58()["type"]
    data_bj["time_bj_58_vlaues"] = keshihua.time_sh_58()["values"]

    data_bj["time_bj_beihe"] = keshihua.time_sh_beihe()["type"]
    data_bj["time_bj_behei_vlaues"] = keshihua.time_sh_beihe()["values"]

    return render(request, 'sh.html', data_bj)

def gz(request):
    data = keshihua.type_gz_58()
    data1 = keshihua.type_gz_beihe()
    print(data1["type"])
    data_bj = {'type': data["type"], 'values': data["values"],
               'type_bj_58': data1["type"], 'values_bj_58': data1["values"],
               }
    data_bj["price_bj_type_58"] = keshihua.price_gz_type_58()["type"]
    data_bj["price_bj_values_58"] = keshihua.price_gz_type_58()["values"]

    data_bj["price_bj_type_beihe"] = keshihua.price_gz_type_beihe()["type"]
    data_bj["price_bj_values_beihe"] = keshihua.price_gz_type_beihe()["values"]

    data_bj["pay_bj_method_58"] = keshihua.pay_gz_method_58()["type"]
    data_bj["pay_bj_method_58_vlaues"] = keshihua.pay_gz_method_58()["values"]

    data_bj["pay_bj_method_beihe"] = keshihua.pay_gz_method_beihe()["type"]
    data_bj["pay_bj_method_beihe_vlaues"] = keshihua.pay_gz_method_beihe()["values"]

    data_bj["time_bj_58"] = keshihua.time_gz_58()["type"]
    data_bj["time_bj_58_vlaues"] = keshihua.time_gz_58()["values"]

    data_bj["time_bj_beihe"] = keshihua.time_gz_beihe()["type"]
    data_bj["time_bj_behei_vlaues"] = keshihua.time_gz_beihe()["values"]

    return render(request, 'gz.html', data_bj)


def cs(request):

    data = keshihua.type_cs_58()
    data1 = keshihua.type_cs_beihe()
    data2 = keshihua.type_bj_beihe()
    print(data1["type"])
    data_bj = {'type': data["type"], 'values': data["values"],
               'type_bj_58': data1["type"], 'values_bj_58': data1["values"],
               }
    data_bj["price_bj_type_58"] = keshihua.price_cs_type_58()["type"]
    data_bj["price_bj_values_58"] = keshihua.price_cs_type_58()["values"]

    data_bj["price_bj_type_beihe"] = keshihua.price_cs_type_beihe()["type"]
    data_bj["price_bj_values_beihe"] = keshihua.price_cs_type_beihe()["values"]

    data_bj["pay_bj_method_58"] = keshihua.pay_cs_method_58()["type"]
    data_bj["pay_bj_method_58_vlaues"] = keshihua.pay_cs_method_58()["values"]

    data_bj["pay_bj_method_beihe"] = keshihua.pay_cs_method_beihe()["type"]
    data_bj["pay_bj_method_beihe_vlaues"] = keshihua.pay_cs_method_beihe()["values"]

    data_bj["time_bj_58"] = keshihua.time_cs_58()["type"]
    data_bj["time_bj_58_vlaues"] = keshihua.time_cs_58()["values"]

    data_bj["time_bj_beihe"] = keshihua.time_cs_beihe()["type"]
    data_bj["time_bj_behei_vlaues"] = keshihua.time_cs_beihe()["values"]

    return render(request, 'cs.html', data_bj)


def wh(request):
    data = keshihua.type_wh_58()
    data1 = keshihua.type_wh_beihe()
    data2 = keshihua.type_wh_beihe()
    print(data1["type"])
    data_bj = {'type': data["type"], 'values': data["values"],
               'type_bj_58': data1["type"], 'values_bj_58': data1["values"],
               }
    data_bj["price_bj_type_58"] = keshihua.price_wh_type_58()["type"]
    data_bj["price_bj_values_58"] = keshihua.price_wh_type_58()["values"]

    data_bj["price_bj_type_beihe"] = keshihua.price_wh_type_beihe()["type"]
    data_bj["price_bj_values_beihe"] = keshihua.price_wh_type_beihe()["values"]

    data_bj["pay_bj_method_58"] = keshihua.pay_wh_method_58()["type"]
    data_bj["pay_bj_method_58_vlaues"] = keshihua.pay_wh_method_58()["values"]

    data_bj["pay_bj_method_beihe"] = keshihua.pay_wh_method_beihe()["type"]
    data_bj["pay_bj_method_beihe_vlaues"] = keshihua.pay_wh_method_beihe()["values"]

    data_bj["time_bj_58"] = keshihua.time_wh_58()["type"]
    data_bj["time_bj_58_vlaues"] = keshihua.time_wh_58()["values"]

    data_bj["time_bj_beihe"] = keshihua.time_wh_beihe()["type"]
    data_bj["time_bj_behei_vlaues"] = keshihua.time_wh_beihe()["values"]

    return render(request, 'wh.html', data_bj)

def cd(request):
    data = keshihua.type_cd_58()
    data1 = keshihua.type_cd_beihe()
    data2 = keshihua.type_cd_beihe()
    print(data1["type"])
    data_bj = {'type': data["type"], 'values': data["values"],
               'type_bj_58': data1["type"], 'values_bj_58': data1["values"],
               }
    data_bj["price_bj_type_58"] = keshihua.price_cd_type_58()["type"]
    data_bj["price_bj_values_58"] = keshihua.price_cd_type_58()["values"]

    data_bj["price_bj_type_beihe"] = keshihua.price_cd_type_beihe()["type"]
    data_bj["price_bj_values_beihe"] = keshihua.price_cd_type_beihe()["values"]

    data_bj["pay_bj_method_58"] = keshihua.pay_cd_method_58()["type"]
    data_bj["pay_bj_method_58_vlaues"] = keshihua.pay_cd_method_58()["values"]

    data_bj["pay_bj_method_beihe"] = keshihua.pay_cd_method_beihe()["type"]
    data_bj["pay_bj_method_beihe_vlaues"] = keshihua.pay_cd_method_beihe()["values"]

    data_bj["time_bj_58"] = keshihua.time_cd_58()["type"]
    data_bj["time_bj_58_vlaues"] = keshihua.time_cd_58()["values"]

    data_bj["time_bj_beihe"] = keshihua.time_cd_beihe()["type"]
    data_bj["time_bj_behei_vlaues"] = keshihua.time_cd_beihe()["values"]

    return render(request, 'cd.html', data_bj)


def updata(request):#上传
    if request.method=='POST':
        print(request.POST)
        file_obj=request.FILES.get("myFile")
        print(str(file_obj.name))
        file = os.path.splitext(str(file_obj.name))
        client = pymongo.MongoClient('localhost', 27017)
        ceshi = client.test

        if (file[1] == '.xlsx' or file[1] == '.xls'):
            with open(file_obj.name,"wb") as f:
                for line in file_obj:
                    f.write(line)

            print(file[1])
            workbook =xlrd.open_workbook(file_obj.name)
            sheet = workbook.sheet_by_index(0)
            nrows = sheet.nrows
            nocls = sheet.ncols
            print(nocls,nrows)

            for i in range(1,nrows):
                row  = sheet.row_values(i)
                item = {}
                item["price"] = row[1]
                item["pay_method"]=row[2]
                item["rental_mathod"]= row[3]
                item["geju"]= row[4]
                item["xiaoqu"]= row[5]
                item["rigion"]= row[6]
                item["address1"]= row[7]
                print(row)
                ceshi.test.insert(dict(item))
            return render(request,"updata.html")

        if (file[1] == '.png' or file[1] == '.jpg'):
            with open(file_obj.name,"wb") as f:
                for line in file_obj:
                    f.write(line)
            print(img_to_str(file_obj.name))
            return render(request,"updata.html")
    return render(request,"updata.html")


def download(request):
    return render(request,'download.html')



def download1(request):#下载
    sh = request.POST.get('sh')
    print(sh)
    client = pymongo.MongoClient('localhost', 27017)
    ceshi = client.city58
    a='bjzufang_detail'
    item_info = ceshi[a]
    workbook = xlsxwriter.Workbook('static/base_info.xlsx')
    worksheet = workbook.add_worksheet('sheet1')
    list = ['price', 'pay_method', 'rental_mathod','geju','xiaoqu','rigion','address1','title','tags','descrition']
    for k in range(len(list)):
        worksheet.write(0, k, list[k])

    price = []
    pay_method = []
    rental_mathod = []
    geju=[]
    xiaoqu=[]
    rigion=[]
    address1=[]
    title=[]
    tags=[]
    descrition=[]

    for i in item_info.find():
        price.append(i['price'])
        pay_method.append(i['rigion'])
        rental_mathod.append(i['rental_mathod'])
        geju.append(i['geju'])
        xiaoqu.append(i['xiaoqu'])
        rigion.append(i['rigion'])
        address1.append(i['address'])
        title.append(i['title'])
        tags.append(i['tags'])
        descrition.append(i['descrition'])

    worksheet.write_column('A2', price)
    worksheet.write_column('B2', pay_method)
    worksheet.write_column('C2', rental_mathod)
    worksheet.write_column('D2', geju)
    worksheet.write_column('E2', xiaoqu)
    worksheet.write_column('F2', rigion)
    worksheet.write_column('G2', address1)
    worksheet.write_column('H2', title)
    worksheet.write_column('I2', tags)
    worksheet.write_column('J2', descrition)
    workbook.close()
    file = open('static/base_info.xlsx', 'rb')
    response = FileResponse(file)
    return response

def login(request):#登陆
    if request.method == 'POST':
        name = request.POST.get('Username')
        password = request.POST.get('Password')
        print(name, password)
        client = pymongo.MongoClient('localhost', 27017)
        ceshi = client["Usr"]
        item_info = ceshi['usr']
        for i in item_info.find():
            if(name==i["name"] and password==i["password"]):
                a = '登陆成功'
                print(i)
                return render(request, 'index.html', {'values': a})

    return render(request,'login.html')

def rigister(request):#注册
    if request.method == 'POST':
        name = request.POST.get('Username')
        password = request.POST.get('Password')
        email = request.POST.get('Email')
        phone = request.POST.get('Phone')
        client = pymongo.MongoClient('localhost', 27017)
        ceshi = client["Usr"]
        table = ceshi["usr"]
        mydict = {"name": name, "password": password, "email": email,"phone":phone}
        print(mydict)
        x=table.insert_one(mydict)
        print(x)
        a = '注册成功'
        return render(request,'index.html',{'values':a})
    a = '注册失败'
    return render(request, 'login.html',{'values':a})