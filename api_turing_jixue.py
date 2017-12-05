import json
import requests


KEY = '******************'    # change to your API KEY
url = 'http://www.tuling123.com/openapi/api'

req_info = u'讲个故事'.encode('utf-8')


query = {'key': KEY, 'info': req_info}
headers = {'Content-type': 'text/html', 'charset': 'utf-8'}


# 方法一、用requests模块已get方式获取内容
r = requests.get(url, params=query, headers=headers)
res = r.text
print (json.loads(res).get('text').replace('<br>', '\n'))


# 方法二、用urllib和urllib2库获取内容
# data = urllib.urlencode(query)
# req = urllib2.Request(url, data)
# f = urllib2.urlopen(req).read()
# print json.loads(f).get('text').replace('<br>', '\n')