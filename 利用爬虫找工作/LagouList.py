# -*-coding:utf-8-*-
import json,requests,re
import time

def get_json_data(position,page):
    '''获取json数据'''
    url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E6%9D%AD%E5%B7%9E&needAddtionalResult=false'  
    data = {
        'first':'false',
        'pn':page,
        'kd':position
    }
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Host': 'www.lagou.com',
        'Referer': 'https://www.lagou.com/jobs/list_%E6%B4%BB%E5%8A%A8%E8%BF%90%E8%90%A5?labelWords=&fromSearch=true&suginput=',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie':'user_trace_token=20180625150727-40ba3b08-0db0-47e5-931d-cd245399df9e; _ga=GA1.2.7043482.1529910448; LGUID=20180625150728-6b9b8c60-7846-11e8-9759-5254005c3644; JSESSIONID=ABAAABAAAIAACBI486EC22E57607557B508B672B324E738; index_location_city=%E6%9D%AD%E5%B7%9E; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1532938928,1532939321,1532943882,1533109622; LGSID=20180801154703-14c1f3ee-955f-11e8-ac93-525400f775ce; PRE_UTM=; PRE_HOST=www.google.com; PRE_SITE=https%3A%2F%2Fwww.google.com%2F; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; _gid=GA1.2.1507531457.1533109622; TG-TRACK-CODE=index_search; _gat=1; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1533110586; LGRID=20180801160308-538065fd-9561-11e8-ac94-525400f775ce; SEARCH_ID=14a98ecaa56948b181b1c5cd8f151001',
        'X-Anit-Forge-Code':'0',
        'X-Anit-Forge-Token': 'None',
        'X-Requested-With': 'XMLHttpRequest'
        }
    response = requests.post(url,headers=headers,data=data,verify=False)
    return response.text

def get_max_pageNumber(position):
    '''获取最大页码'''
    result = get_json_data(position,'1')
    pageNumber = int(json.loads(result)['content']['positionResult']['totalCount']/15)
    return pageNumber

def get_positon_results(json_data):
    '''获取关注字段'''
    data = json.loads(json_data)
    if data['success'] == True:
        position_results = []
        positions = data['content']['positionResult']['result']
        for item in positions:
            companyShortName = item['companyShortName']
            companyFullName = item['companyFullName']
            companySize = item['companySize']
            positionName = item['positionName']
            workYear = item['workYear']
            salary = item['salary']
            industryField = item['industryField']
            financeStage = item['financeStage']
            createTime = item['createTime']
            education = item['education']
            district = item['district']
            positionId = item['positionId']
            jobNature = item['jobNature']
            positionAdvantage = item['positionAdvantage']
            positionUrl = 'https://www.lagou.com/jobs/' + str(positionId) + '.html'


            position_results.append([str(companyFullName),str(positionName),str(workYear),str(salary),str(industryField),str(financeStage),
                                     str(companyShortName),str(companySize),str(createTime),str(education),str(district),str(jobNature),
                                     str(positionAdvantage),str(positionId),str(positionUrl)])
        return position_results
    else:
        print ('Data error...')


def main():
    position = '活动运营'
    fileName = 'lagou_{}'.format(position)
    filePath = 'D:/' + fileName + '.txt'
    pageNumber = get_max_pageNumber(position)
    with open(filePath, 'a+',encoding='utf-8') as f:
        title = ['公司名称','职位名称','工作年限','薪资范围','行业','融资情况','公司简称','公司规模','发布时间','学历要求','地区','工作性质','职位优势','职位ID','职位链接']
        f.write('\t'.join(title) + '\n')
        for i in range(1,pageNumber + 1): 
            time.sleep(10)
            print ('开始爬第{}页...'.format(i))
            page_data = get_json_data(position,str(i))
            page_result = get_positon_results(page_data)
            for data in page_result:
                string = '\t'.join(data)
                print(string)
                f.write(string + '\n')
    
if __name__ == '__main__':
    main()
