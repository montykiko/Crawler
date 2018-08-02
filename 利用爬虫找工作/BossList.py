import requests,re,time
from bs4 import BeautifulSoup

def get_position_results(url):
    ab_urls ='https://www.zhipin.com'
    headers = {
                'Cookie':'lastCity=101210100; JSESSIONID=""; __c=1533020202; __g=-; __l=l=%2Fwww.zhipin.com%2F&r=https%3A%2F%2Fwww.google.com%2F; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1532073970,1532323266,1532326685,1533020202; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1533021779; __a=15341501.1528789420.1532323266.1533020202.44.5.24.44; toUrl=https%3A%2F%2Fwww.zhipin.com%2Fc101210100%2Fh_101210100%2F%3Fquery%3D%25E6%2595%25B0%25E6%258D%25AE%25E6%258C%2596%25E6%258E%2598%26page%3D2',
                'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
                }    
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text,'lxml')
    job_title = soup.select('div[class="job-title"]')
    job_salary = soup.select('span[class="red"]')
    job_info = soup.select('div.info-primary > p')
    company = soup.select('div.company-text > h3.name > a')
    company_info = soup.select('div.company-text > p')
    publish_time = soup.select('div.info-publis > p')
    details = soup.select('div.info-primary > h3.name > a')
    
    position_results = []
    for title,salary,info,comp,comp_info,time,detail in zip(job_title,job_salary,job_info,company,company_info,publish_time,details):
        title = title.get_text()
        salary = salary.get_text()
        job_info = info.get_text()
        company = comp.get_text()
        company_info = comp_info.get_text()
        publish_time = time.get_text()
        job_url = ab_urls + detail.get('href')
        lst = [title,salary,job_info,company,company_info,publish_time,job_url]
        position_results.append(lst)
    return position_results

def main():
    position = "数据挖掘&机器学习"   
    urls = ["https://www.zhipin.com/c101210100/h_101210100/?query={0}&page={1}".format(position,page) for page in range(1,11)]
    with open('D:/zhipin/zhipin.txt','a+',encoding='utf-8') as f:
        title_lst = ["职位名称","薪资范围","学历要求","公司名称","公司情况","发布时间","职位链接"]
        title_string = '\t'.join(title_lst) + '\n'
        f.write(title_string)
        
        for url in urls:
            time.sleep(10)
            print(url)
            position_results = get_position_results(url)
            for detail in position_results:
                f.write('\t'.join(detail) + '\n')
                    
if __name__ == '__main__':
    main()  