from multiprocessing import Pool
from channel_extract import channel_list
from page_parsing import get_links_from
from page_parsing import get_item_info
import pymongo

client = pymongo.MongoClient('localhost',27017)
tongcheng = client['tongcheng']
url_list = tongcheng['url_list']
item_info = tongcheng['item_info']

def get_all_links_from(channel):
    for num in range(1,101):
        get_links_from(channel,num)

if __name__ == '__main__':
    #创建进程池
    pool = Pool()
    pool.map(get_all_links_from,channel_list.split())

#map函数
# def double(x):
#     return x*2
# print (list(map(double,[1,2,3,4])))