from bs4 import BeautifulSoup
import requests,time

url = 'https://knewone.com/discover?page='
def get_page(url):

    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    images = soup.select('a.cover-inner > img')
    titles = soup.select('h4.title')
    fancies = soup.select('a > span.fanciers_count')
    links = soup.select('h4.title > a')

    for image,title,fancy,link in zip(images,titles,fancies,links):
        data = {
            'image':image.get('src'),
            'title':title.get_text(),
            'fancy':fancy.get_text(),
            'link':link.get('href')
        }
        print (data)

def get_more_page(start,end):
    for num in range(start,end):
        get_page(url+str(num))
        time.sleep(2)

get_more_page(1,10)