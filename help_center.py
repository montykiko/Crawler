'''
@title : 携程帮助中心问题分类快速导引
Create on 2017-08-22
@author : jixue
'''
import requests
from bs4 import BeautifulSoup

url = 'http://help.ctrip.com/'
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text,'lxml')
categories = soup.select('li.fast_guidance_list > h4')
with open(r'content.txt','w',encoding='utf-8') as f:
    cate_list = []
    for category in categories:
        cate_list.append(category.get_text())
    print (cate_list)
    guidances = soup.select('li.fast_guidance_list')
    for guide in guidances:
        f.write(guide.get_text())
        print (guide.get_text())








