from bs4 import BeautifulSoup
info = []
with open(r'path') as wb_data:
    soup = BeautifulSoup(wb_data,'lxml')
    images = soup.select('body > div > div > div.col-md-9 > div > div > div > img')
    titles = soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4 > a')
    descs = soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > p')
    prices = soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4.pull-right')
    stars = soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p:nth-of-type(2)')
for image,title,desc,price,star in zip(images,titles,descs,prices,stars):
    data = {
        'image':image.get('src'),
        'title':title.get_text(),
        'desc':desc.get_text(),
        'price':price.get_text(),
        'star':len(star.find_all("span",class_="glyphicon glyphicon-star"))
    }
    info.append(data)
print (info)