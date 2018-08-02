# -*-coding:utf-8-*-
import json,requests,re
import time,os
import pandas as pd
from pandas import DataFrame
from bs4 import BeautifulSoup
from datetime import datetime

def get_job_description(url):
    '''获取JD和公司地址'''
    headers = {
        'Host': 'www.lagou.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'Cookie':'user_trace_token=20180625150727-40ba3b08-0db0-47e5-931d-cd245399df9e; _ga=GA1.2.7043482.1529910448; LGUID=20180625150728-6b9b8c60-7846-11e8-9759-5254005c3644; JSESSIONID=ABAAABAAAIAACBI486EC22E57607557B508B672B324E738; _gid=GA1.2.1910458859.1532916218; index_location_city=%E6%9D%AD%E5%B7%9E; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1532938518,1532938928,1532939321,1532943882; LGSID=20180731104834-375665e8-946c-11e8-ac0b-525400f775ce; PRE_UTM=; PRE_HOST=www.google.com; PRE_SITE=https%3A%2F%2Fwww.google.com%2F; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; TG-TRACK-CODE=search_code; SEARCH_ID=596da791739a455996ff0a597325e9fd; _gat=1; LGRID=20180731111708-350125a9-9470-11e8-ac0d-525400f775ce; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1533007028'
    }
    wb_data = requests.get(url,headers=headers)
    soup = BeautifulSoup(wb_data.text,'lxml')
    desc = soup.select('dd[class="job_bt"]')
    address = soup.select('dd[class="job-address clearfix"]')
    add_ = str(address[0])
    job_desc = str(desc[0])
    rule = re.compile(r'<[^>]+>') 
    result = rule.sub('',job_desc)
    add = rule.sub('',add_)
    return result,add

def merge_data(filePath):
    '''工作简介和JD描述数据merge'''
    df = pd.read_table(filePath,engine='python',encoding='utf-8')
    cond = df['工作性质']=='全职'
    df = df.loc[cond].copy()
    urls = df['职位链接'].tolist()
    dct = {}
    for url in urls:
        time.sleep(15)
        result,add = get_job_description(url)
        dct[url] = [result,add]
    data = pd.DataFrame.from_dict(dct,orient='index')
    data = data.reset_index()
    data.columns =['职位链接','职位描述','公司地址']
    new_df = df.merge(data,on='职位链接')
    new_df['职位描述'] = new_df['职位描述'].str.replace(r'职位描述','').str.replace('\n','').str.replace(r'工作职责','')
    new_df['职位描述'] = new_df['职位描述'].str.replace('：|岗位职责|职责描述','')
    new_df['公司地址'] = new_df['公司地址'].str.replace(r'工作地址|查看地图','')
    new_df['公司地址'] = new_df['公司地址'].str.replace(r'\s+','')
    new_df.to_excel('D:/lagou_{}.xlsx'.format(datetime.now().strftime('%Y%m%d')),index=False,encoding='gbk')

def main():
    filePath = 'D:/lagou.txt'
    merge_data(filePath)
    os.remove(filePath)

if __name__ == '__main__':
    main()