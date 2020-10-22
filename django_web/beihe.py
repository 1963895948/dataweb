from django.test import TestCase

# Create your tests here.
import requests
import re
import random
from io import BytesIO
from lxml import etree
import base64
import pymongo
from fontTools.ttLib import TTFont
from concurrent.futures import ProcessPoolExecutor
import sys
import time
import hashlib
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
_version = sys.version_info

is_python3 = (_version[0] == 3)

orderno = "ZF2020528970394tkQr"
secret = "de3617e60db14ddbb05b4238e2ce487e"

ip = "forward.xdaili.cn"
port = "80"

ip_port = ip + ":" + port

timestamp = str(int(time.time()))
string = ""
string = "orderno=" + orderno + "," + "secret=" + secret + "," + "timestamp=" + timestamp

if is_python3:
    string = string.encode()

md5_string = hashlib.md5(string).hexdigest()
sign = md5_string.upper()

#print(sign)
auth = "sign=" + sign + "&" + "orderno=" + orderno + "&" + "timestamp=" + timestamp

# 请求头
proxy = {"http": "http://" + ip_port, "https": "https://" + ip_port}
headers = {"Proxy-Authorization": auth, "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}

# 目标url
base_url = 'https://{city}.58.com/chuzu/pn{page}/'




def mongodb():
    """
    链接MongoDB数据库,并创建表和字段
    :return: db
    """
    client = pymongo.MongoClient(host='localhost', port=27017)
    db = client.beihe
    return db


def get_real_word(fake_word, html):
    """
    改方法解密爬取价格乱码问题
    :param fake_word:
    :param html:
    :return: 解密后的字符串
    """
    font_ttf = re.findall("charset=utf-8;base64,(.*?)'\)", html)[0]
    font = TTFont(BytesIO(base64.decodebytes(font_ttf.encode())))
    numbering = font.get('cmap').tables[0].ttFont.get('cmap').tables[0].cmap
    word_list = []
    for char in fake_word:
        decode_num = ord(char)
        if decode_num in numbering:
            num = numbering[decode_num]
            num = int(num[-2:]) - 1
            word_list.append(num)
        else:
            word_list.append(char)
    real_word = ''
    for num in word_list:
        real_word += str(num)
    return real_word


def get_index(url):
    """
    请求网页链接,返回结果数据（字节集数据）
    :param url:
    :return: response
    """
    print('正在抓取' + url)
    response = requests.get(url, headers=headers, proxies=proxy, verify=False,allow_redirects=False)
    if response.status_code == 200:
        return response
    else:
        print('抓取失败')


def parse_list(url,city):
    db = mongodb()  # 链接MongoDB
    html = get_index(url).text  # 将字节集数据转为文本型
    item = {}
    page = etree.HTML(html)  # lxml库对网页源码进行解析
    li = page.xpath('.//ul[@class="house-list"]//li')[0:-1]
    for each_li in li:
        title = each_li.xpath('.#content > div.content__article > div.content__list > div:nth-child(1) > div > p.content__list--item--title.twoline > a')[0].strip()
        item['title'] = get_real_word(title, html)
        item['src'] = each_li.xpath('.//div[@class="des"]/h2/a/@href')[0]
        price = each_li.xpath('document.querySelector("#content > div.content__article > div.content__list > div:nth-child(1) > div > p.content__list--item--des")')[0]
        item['price'] = get_real_word(price, html)
        type = each_li.xpath('//*[@id="content"]/div[1]/div[1]/div[1]/div/p[4]')[0]
        item['type'] = get_real_word(type, html)
        '''item['address'] = '/'.join(each_li.xpath('.//p[@class="add"]/a/text()'))
        print(item['address'])
        print(item)'''
        # 抓取内容入库
        db.zufang.insert(dict(item))
        # 随机进行休眠
        #time.sleep(random.random())
        #print(item)
        """
        以下代码非必要
        """
        if not 'https:' in item['src']:
            url = 'https:' + item['src'] + '?reform=pcfront'
        else:
            url = item['src']
        res_1 = get_index(url)
        try:
            parse_detail(res_1.text,title,city)
        except:
            print('爬取频繁，出现验证码')


def parse_detail(html,title,city):
    """
    进入详情页进行详细爬取
    :param html:
    :return:
    """
    db = mongodb()
    item = {}
    page = etree.HTML(html)
    price = page.xpath('//b[contains(@class, "f36")]/text()')
    # if price:
    item['price'] = get_real_word(price[0], html)
    item['pay_method'] = page.xpath('//div[contains(@class, "f16")]/span[2]/text()')[0]
    item['rental_mathod'] = page.xpath('//ul[@class="f14"]/li[1]/span[2]/text()')[0]
    house = page.xpath('//ul[@class="f14"]/li[2]/span[2]/text()')[0]
    house = get_real_word(house, html)
    item['house'] = {
        'type': house.split(' ')[0],
        'area': re.findall('卫.*?(\d+).*?平', house, re.S)[0],
        'decoration': house.split(' ')[-2],
    }
    #print(item)
    geju = page.xpath('//ul[@class="f14"]/li[3]/span[2]/text()')[0]
    item['geju'] = get_real_word(geju, html)
    item['xiaoqu'] = page.xpath('//ul[@class="f14"]/li[4]/span[2]/a/text()')[0]
    item['rigion'] = ''.join(page.xpath('//ul[@class="f14"]/li[5]/span[2]//text()')).replace(' ', '').strip()
    traffic = page.xpath('//ul[@class="f14"]/li[5]/em/text()')
    if traffic:
        item['traffic'] = traffic[0]
    item['address'] = page.xpath('//ul[@class="f14"]/li[6]/span[2]/text()')[0].strip()
    #/html/body/div[4]/div[2]/div[2]/div[1]/div[1]/ul/li[6]
    #/html/body/div[4]/div[2]/div[2]/div[1]/div[1]/ul/li[6]
    #body > div.main-wrap > div.house-basic-info > div.house-basic-right.fr > div.house-basic-desc > div.house-desc-item.fl.c_333 > ul > li:nth-child(6)

    item['tags'] = '/'.join(page.xpath('//ul[@class="introduce-item"]/li[1]/span[2]/em/text()'))
    item['descrition'] = ' '.join(page.xpath('//ul[@class="introduce-item"]/li[2]/span[2]//text()'))
    item["title"] = title
    imgs = page.xpath('//ul[@id="housePicList"]/li/images/@lazy_src')
    image = []
    for img in imgs:
        image.append(img)
        item['image'] = image
    print(item)
    if (city == 'bj'):
        db.bjzufang_detail.insert(dict(item))
    if (city == 'sh'):
        db.shzufang_detail.insert(dict(item))
    if (city == 'gz'):
        db.gzzufang_detail.insert(dict(item))
    if (city == 'cs'):
        db.cszufang_detail.insert(dict(item))
    if (city == 'cd'):
        db.cdzufang_detail.insert(dict(item))
    if (city == 'wh'):
        db.whzufang_detail.insert(dict(item))
    print("入库成功")


if __name__ == '__main__':
    city = input('请输入您要查询的城市（城市名称的首字母小写缩写）: ')
    max_page_num = input('请输入您要爬取的页数：')
    start = time.time()
    # 创建进程池
    pool = ProcessPoolExecutor()
    for page in range(1, int(max_page_num) + 1):
        url = base_url.format(city=city, page=page)
        # 提交执行的函数到线程池中
        pool.submit(parse_list, url,city)
    # 总运行时长
    print('耗时：', time.time() - start)
