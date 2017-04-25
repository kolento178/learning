# from sys import argv
#
# script, filename = argv
# txt = open(filename)
#
# print("Here's your file %r" % filename)
# print(txt.read())
#
# print("Type the filename again:")
# file_again = input(">")
#
# txt_again = open(file_again)
# print(txt_again.read())


# import urllib.request
#
# url = 'http://baike.baidu.com/link?url=2BEefSGMf22HTrfmE3y7VM3kk07lcvUmjZu_mvAT6HDtciaDQ6SuotPej8Fj9i3puVKWVz7sSYkqssdZ6zl9Ja'
#
# res = urllib.request.urlopen(url)
# print(res.getcode())


# haha = [{'li': 'hahaha', 'niu': 'dan', 'wen': 'yoohoo'}]
# print(haha[0]['li'])

# from bs4 import BeautifulSoup
# import requests

# url = 'http://www.qiushibaike.com/'
# response = requests.get(url)
# res = response.read().decode('utf-8')
# soup = BeautifulSoup(response.text, 'lxml')
# summary = soup.find('div', class_="'para' label-module='para'")
# s = summary.text()
# print(s)
# print(soup)


import requests
import urllib.request
import re


def get_html(url):
    page = requests.get(url)
    return page.text


def get_text(html,file):
    textre = re.compile(r'content">\n*<span>(.*)</span>')
    textlist = re.findall(textre,html)
    num = 0
    txt = []
    for i in textlist:
        num += 1
        txt.append(str(num)+'.'+i+'\n'*2)
    with open(file,'w',encoding='utf-8') as f:
        f.writelines(txt)


def get_img(html):
    imgre = re.compile(r'<img src="(.*\.JPEG)" alt=',re.IGNORECASE)
    imglist = re.findall(imgre,html)
    x = 0
    for imgurl in imglist:
        x += 1
        urllib.request.urlretrieve(imgurl, '%s.jpg' % x)

html = get_html("http://www.qiushibaike.com/8hr/page/2/")

get_text(html,'a.txt')
get_img(html)
