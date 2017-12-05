from bs4 import BeautifulSoup
import requests,time
import pymongo

client = pymongo.MongoClient('localhost',27017)
xiaozhu = client['xiaozhu']
fangzi  = xiaozhu['fangzi']

urls = ['http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(str(i)) for i in range(3)]

def get_page(url):
    wb_data = requests.get(url)
    time.sleep(2)
    soup = BeautifulSoup(wb_data.text,'lxml')
    titles = soup.select('a > span.result_title.hiddenTxt')
    prices = soup.select('span.result_price > i')
    image_fangs = soup.select('a.resule_img_a > img.lodgeunitpic')
    image_lords = soup.select('a > img.landlordimage')
    descs = soup.select('em.hiddenTxt')


    for title,price,image_fang,image_lord,desc in zip(titles,prices,image_fangs,image_lords,descs):
        data = {
            'title':title.get_text(),
            'image_fang':image_fang.get('lazy_src'),
            'image_lord':image_lord.get('lazy_src'),
            'price':int(price.get_text()),
            'desc':desc.get_text().strip()
        }
        fangzi.insert_one(data)
    print ('Done!')


# for url in urls:
#     get_page(url)
#
# for item in fangzi.find():
#     if item['price'] >=500:
#         print (item)

for item in fangzi.find({'price':{'$gte':500}}):
    print (item)
