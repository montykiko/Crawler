from bs4 import BeautifulSoup
import requests
url ='http://hz.xiaozhu.com/fangzi/4326629013.html'
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text,'lxml')
title = soup.select('div.pho_info > h4 > em')[0].text
address = soup.select('div.pho_info > p > span.pr5')[0].text
price  = soup.select('div#pricePart > div.day_l > span')[0].text
image = soup.select('img#curBigImage')[0].get('src')
host_image = soup.select('div.member_pic > a > img')[0].get('src')
gender = soup.select('h6 > span')[0].get('class')[0]
name = soup.select('a.lorder_name')[0].text

def print_gender(class_name):
    if class_name == "member_girl_ico":
        return "女"
    elif class_name == "member_boy_ico":
        return "男"
    else:
        return "None"

data = {
    'title':title,
    'address':address.strip(),
    'price':price,
    'image':image,
    'host_image':host_image,
    'name':name,
    'gender':print_gender(gender)
}

print (data)
