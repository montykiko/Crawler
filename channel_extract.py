from bs4 import BeautifulSoup
import requests,time

start_url = 'http://hz.58.com/sale.shtml'
url_host = 'http://hz.58.com'
def get_channel_urls(url):
    wb_data = requests.get(start_url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    links = soup.select('li.ym-tab > span.dlb > a')
    for link in links:
        page_url = url_host +  (str(link.get('href')))
        print (page_url)

# get_channel_urls(start_url)

channel_list = '''
    http://hz.58.com/shouji/
    http://hz.58.com/tongxunyw/
    http://hz.58.com/danche/
    http://hz.58.com/zixingche/
    http://hz.58.com/diannao/
    http://hz.58.com/shuma/
    http://hz.58.com/jiadian/
    http://hz.58.com/ershoujiaju/
    http://hz.58.com/bangong/
    http://hz.58.com/shebei.shtml
    http://hz.58.com/yingyou/
    http://hz.58.com/fushi/
    http://hz.58.com/meirong/
    http://hz.58.com/yishu/
    http://hz.58.com/tushu/
    http://hz.58.com/wenti/
    http://hz.58.com/chengren/
    http://hz.58.comNone
'''