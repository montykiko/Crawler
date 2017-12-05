from bs4 import BeautifulSoup
import requests,time
import urllib.request

url = 'http://weheartit.com/inspirations/taylorswift'
path ='C:/Users/Kismet/Documents/我的坚果云/my_learning/crawler_learning/1_4answer_of_homework/photos/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
}
proxies = {"http": "http://221.202.251.217"}
def get_image_urls(url):
    img_urls = []
    wb_data = requests.get(url,proxies=proxies)
    soup = BeautifulSoup(wb_data.text,'lxml')
    images = soup.select('div > a > img.entry-thumbnail')
    for image in images:
        img_urls.append(image.get('src'))
    #print(img_urls)
    time.sleep(2)
    return img_urls

def download_image(url):
    urllib.request.urlretrieve(url,path+url.split("/")[-2]+url.split("/")[-1])
    print ("Done")

for url in get_image_urls(url):
    download_image(url)
