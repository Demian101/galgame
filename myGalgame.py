import requests
from bs4 import BeautifulSoup
# import re
#url = 'https://www.mygalgame.com'  #/page/1/

headers = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
}
'''

def get_response(url):
    html = requests.get(url)
    soup = BeautifulSoup(html.text,'lxml')
#     print(soup)
    return soup

def onepage(soup):
    headers = {
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
    }
    textlist = set()
    # 获取文本信息
    for text in soup.find_all('span',attrs={'class':'animated_h1'}):
        textlist.add(text.string)
    
    #根据alt 这个特殊属性 ,获取图片信息
    i = 1
    for text in textlist:
        i = i + 1 
        url = soup.find('img',attrs={'alt':text})['src']
        print(url)
        r = requests.get(url)
        with open('D:/galgame/'+text+'.jpg','wb') as f:
            f.write(r.content)

'''
########################################

url = 'https://www.mygalgame.com'
print(type(url))
baseurl = 'https://www.mygalgame.com'

from selenium import webdriver
import time

# 生成页面 page/1 --- page/72
ilist = [x for x in range(1, 73)]
for i in ilist:
    url = baseurl+'/page/'+str(i)
    print("---------------------------------------------")
    print(url)
    print("---------------------------------------------")
    browser = webdriver.Chrome()
    browser.get(url)

    # 通过selenium 获取页面的源代码
    html = browser.page_source     

#    html = requests.get(url,headers = headers)
   
   # 对源代码进行序列化 
    soup = BeautifulSoup(html,'lxml')
#    print(soup)
	
	# 设一个 set() 组记录图片的名字, 并去重
    textlist = set()

    # 获取文本信息
    for text in soup.find_all('span',attrs={'class':'animated_h1'}):
        textlist.add(text.string)
    
    # 因为每一张图片 都有一个 alt属性, 属性名=图片名,所以我们根据这一点为
    # 图片命名 .
    for text in textlist:
        url = soup.find('img',attrs={'alt':text})['src']
        print(url)
        r = requests.get(url)
        # 有些图片的名字里有 '/','*' ,我们用 '-' 代替 .
        textstring = text.replace('/','-')
        textstring = textstring.replace('*','-')
        # 保存二进制文件 .
        with open('D:/galgame/'+textstring+'.jpg','wb') as f:
            f.write(r.content)
    browser.close()
