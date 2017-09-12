from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import requests
import os
import time
import re

if __name__ == '__main__':
    list_url = []
    for num in range(78,80):
        if num == 1:
            url = 'http://jandan.net/ooxx'
        else:
            url = 'http://jandan.net/ooxx/page-%d#comments' % num
        headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
        }
        req = requests.get(url = url,headers = headers)
        req.encoding = 'utf-8'
        html = req.text
        bf = BeautifulSoup(html, 'lxml')
        targets_url = bf.find_all(class_='view_img_link')

        for each in targets_url:
            list_url.append('http://'+each.get('href').replace('//',''))

    print(list_url)

    for target_url in list_url:

        filename = ''+str(time.localtime())+'.jpg'


        headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
        }
        img_req = requests.get(url = target_url,headers = headers)
        img_req.encoding = 'utf-8'
        img_html = img_req.text
        img_bf = BeautifulSoup(img_html, 'lxml')


        if 'images2' not in os.listdir():
            os.makedirs('images2')
        urlretrieve(url = target_url,filename = 'images2/'+ filename )
        time.sleep(1)

    print('下载完成！')