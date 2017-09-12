from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    for num in range(75,80):
        if num == 1:
            url = 'http://jandan.net/ooxx'
        else:
            url = 'http://jandan.net/ooxx/page-%d#comments' % num
        headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
        }
        req = requests.get( url,headers = headers)
        req.encoding = 'utf-8'
        html = req.text
        bf = BeautifulSoup(html, 'lxml')
        targets_url = bf.find_all(class_='view_img_link')
        list_url = []
        for each in targets_url:
            list_url.append(str(each.get('href')))
        print(list_url)