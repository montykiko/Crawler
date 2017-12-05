from bs4 import BeautifulSoup
info = []
with open(r'C:\Users\Kismet\Documents\我的坚果云\my_learning\crawler_learning\1_2code_of_video\web\new_index.html') as wb_data:
    soup = BeautifulSoup(wb_data,'lxml')
    #print (soup)
    images = soup.select('body > div.main-content > ul > li > img')
    titles = soup.select('body > div.main-content > ul > li  > div.article-info > h3 > a')
    cates = soup.select('body > div.main-content > ul > li > div.article-info > p.meta-info')
    descs = soup.select('body > div.main-content > ul > li  > div.article-info > p.description')
    scores = soup.select('body > div.main-content > ul > li > div.rate > span')
    # print (images,titles,cates,descs,scores,sep = '\n------------------------------\n',)

for image,title,cate,desc,score in zip(images,titles,cates,descs,scores):
    data = {
        'title':title.get_text(),
        'image':image.get('src'),
        'cate':list(cate.stripped_strings),
        'desc':desc.get_text(),
        'score':score.get_text()
    }
    info.append(data)
for i in info:
    if float(i['score'])>3:
        print (i['title'],' ',i['cate'])