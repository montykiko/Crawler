from bs4 import BeautifulSoup
import requests,time,re
import pymongo

client = pymongo.MongoClient('localhost',27017)
tongcheng = client['tongcheng']
url_list = tongcheng['url_list']
item_info = tongcheng['item_info']
#spider 1
def get_links_from(channel,pages,who_sells = 0):
    #http://hz.58.com/shouji/0/pn2/
    list_view = '{}{}/pn{}/'.format(channel,str(who_sells),str(pages))
    wb_data = requests.get(list_view)
    time.sleep(2)
    soup = BeautifulSoup(wb_data.text,'lxml')
    links = soup.select('td.t > a.t')
    if soup.find('td','t'):
        for link in links:
            item_link = link.get('href').split('?')[0]
            if bool(re.search('jump',item_link)):
                pass
            else:
                url_list.insert_one({'url':item_link})
                print (item_link)
                get_item_info(item_link)
    else:
        pass
        #Nothing!

def get_item_info(url):
    if bool(re.search('short',str(url))):
        pass
    else:
        wb_data = requests.get(url)
        soup = BeautifulSoup(wb_data.text,'lxml')
        # no_longer_exist = '404' in soup.find('script', type='text/javascript').get('src').split('/')
        # if no_longer_exist:
        #     pass
        # else:
        title = soup.select('h1.info_titile')[0].text
        price = soup.select('span.price_now > i')[0].text
        # date = soup.select('.time')[0].text
        # area = list(soup.select('span.c_25d')[0].stripped_strings) if soup.find_all('span','c_25d') else None
        area = soup.select('div.palce_li > span > i')[0].text
        name = soup.select('p.personal_name')[0].text
        item_info.insert_one({'title':title,'price':price,'area':area,'name':name})
        print ({'title':title,'price':price,'area':area,'name':name})




#get_item_info('http://zhuanzhuan.58.com/detail/887229653780725769z.shtml')

#get_links_from('http://hz.58.com/shouji/',1)


#观察404网页的构成特点
#url = 'http://hz.58.com/shouji/22660325905310x.shtml'
#wb_data = requests.get(url)
#soup = BeautifulSoup(wb_data.text,'lxml')
#print (soup.prettify())

