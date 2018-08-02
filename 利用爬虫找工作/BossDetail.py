import requests, re, time
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime
import pymongo


def get_detail(url):    
    headers = {
            'Cookie':'lastCity=101210100; JSESSIONID=""; __c=1533020202; __g=-; __l=l=%2Fwww.zhipin.com%2F&r=https%3A%2F%2Fwww.google.com%2F; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1532073970,1532323266,1532326685,1533020202; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1533021779; __a=15341501.1528789420.1532323266.1533020202.44.5.24.44; toUrl=https%3A%2F%2Fwww.zhipin.com%2Fc101210100%2Fh_101210100%2F%3Fquery%3D%25E6%2595%25B0%25E6%258D%25AE%25E6%258C%2596%25E6%258E%2598%26page%3D2',
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
    info = {}
    try:
        response = requests.get(url,headers=headers)
        soup = BeautifulSoup(response.text,'lxml')
        jd = soup.select('div.job-sec > div.text')[0].get_text()
        add = soup.select('div.location-address')[0].get_text()
        info['url'] = url
        info['jd'] = jd
        info['add'] = add
        collection_1.insert_one(info)
    except IndexError:
        print("Data error...")
        pass

client = pymongo.MongoClient('localhost',27017)
mongo_1 = client['mongo_1']
collection_1 = mongo_1['collection_1']
db_url = [i['url'] for i in collection_1.find()]
x = set(db_url)

filepath = 'D:/zhipin/zhipin.txt'
df = pd.read_table(filepath,encoding='utf-8')
urls = df['职位链接'].tolist()
y = set(urls)
rest_of_urls = y - x

count = 0
for url in rest_of_urls:
    get_detail(url)
    print("正在爬取第{}页".format(count+1))
    count+= 1
    time.sleep(10)