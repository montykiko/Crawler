'''
@title : 调查旅游常见咨询问题，以携程为例
Created on 2017-08-22
@author : jixue
'''

import requests
from bs4 import BeautifulSoup

url = 'http://kefu.ctrip.com/'
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text,'lxml')
categories = soup.select('div.question_type > div > a')
link_list = []
cate_list = []
with open(r'focused_questions.txt','w',encoding='utf-8') as f:
    for category in categories:
        data = {
            'category':category.get_text(),
            'link':category.get('href')
        }
        link_list.append(data['link'])
        cate_list.append(data['category'])

    for url,cate in zip(link_list,cate_list):
        wb_data = requests.get(url)
        soup = BeautifulSoup(wb_data.text,'lxml')
        questions = soup.select('div.question_tabulation > ul > li > a')
        for question in questions:
            data = {
                'question':question.get_text(),
                'link':'http://help.ctrip.com/'+ question.get('href')
            }
            print (cate + "\t" + data['question'])
            f.write(cate + "\t" + data['question'] + "\n")



