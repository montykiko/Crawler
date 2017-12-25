# _*_ coding: utf-8 _*_
import requests
from bs4 import BeautifulSoup

def get_links(search_number,filename):
    base_url = 'http://***.73.**.171:21035'
    url = base_url + "/" + search_number
    print (url)
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    links = soup.select("pre > a")
    with open(filename,"a+") as f:
        for link in links:
            target = base_url+link.get('href')
            f.write(target + "\n")

get_links("8abb71f4-d380-11e7-b3a1-8885306f7028",r"./8abb71f4-d380-11e7-b3a1-8885306f7028/urls.txt")