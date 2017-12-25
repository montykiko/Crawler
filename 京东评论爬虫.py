import requests,json

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}

#获取对应型号产品的最大页码
def get_maxpage(num,productId,page):
    url = 'https://club.jd.com/comment/skuProductPageComments.action?callback=fetchJSON_comment98vv{}&productId={}&score=0&sortType=5&page={}&pageSize=10&isShadowSku=0&fold=1'.format(num,productId,page)
    s1 = requests.get(url,headers=headers).text.replace("fetchJSON_comment98vv{}(".format(num),"").replace(");","")
    d1 = json.loads(s1)
    maxpage = d1['productCommentSummary']['commentCount']//10
    return maxpage

#获取相关型号的评论
def get_comments(num,productId,page):
    maxpage = get_maxpage(num,productId,page)
    with open('nutpro_comments.txt','a+') as file:
        count = 0
        urls = ['https://club.jd.com/comment/skuProductPageComments.action?callback=fetchJSON_comment98vv{}&productId={}&score=0&sortType=5&page={}&pageSize=10&isShadowSku=0&fold=1'.format(num,productId,p) for p in range(1,maxpage)]
        for url in urls:
            result = requests.get(url,headers=headers).text.replace("fetchJSON_comment98vv{}(".format(num),"").replace(");","")
            r = json.loads(result)
            for c in r['comments']:
                line = c['creationTime']+ "\t" + c['nickname']+ "\t" +c['referenceName']+ "\t" + c['content'].replace("\n","").replace("\r","") + "\n"
                file.write(line)
                count += 1
                print ("Getting line:{}...".format(count))

'''
每个颜色每个规格的productID都是不同的，score是星级0-5，sortType是排序条件，
5是推荐排序，6是按时间排序（猜测），因此可以多条件的去请求，得到的结果再去重，写入本地txt文件即可，关于坚果pro手机评论
碳黑色  https://club.jd.com/comment/skuProductPageComments.action?callback=fetchJSON_comment98vv54866&productId=3867555&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1
碳128G  https://club.jd.com/comment/skuProductPageComments.action?callback=fetchJSON_comment98vv7352&productId=4432052&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1
浅金色  https://club.jd.com/comment/skuProductPageComments.action?callback=fetchJSON_comment98vv1388&productId=5282419&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1
浅128G  https://club.jd.com/comment/skuProductPageComments.action?callback=fetchJSON_comment98vv2002&productId=4086227&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1
巧克力  https://club.jd.com/comment/skuProductPageComments.action?callback=fetchJSON_comment98vv5332&productId=4086223&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1
巧128G https://club.jd.com/comment/skuProductPageComments.action?callback=fetchJSON_comment98vv876&productId=4086229&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1
酒红色  https://club.jd.com/comment/skuProductPageComments.action?callback=fetchJSON_comment98vv40073&productId=3867557&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1
酒128G https://club.jd.com/comment/skuProductPageComments.action?callback=fetchJSON_comment98vv5058&productId=4432056&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1
细红线  https://club.jd.com/comment/skuProductPageComments.action?callback=fetchJSON_comment98vv1345&productId=5424599&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1
细128G  https://club.jd.com/comment/skuProductPageComments.action?callback=fetchJSON_comment98vv30249&productId=4432058&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1
'''
# get_comments('54866','3867555','8')
# get_comments('1388','5282419','8')
# get_comments('5332','4086223','8')
# get_comments('40073','3867557','8')
# get_comments('1345','5424599','8')
# get_comments('7352','4432052','8')
# get_comments('2002','4086227','8')
# get_comments('876','4086229','8')
# get_comments('5058','4432056','8')
get_comments('30249','4432058','8')