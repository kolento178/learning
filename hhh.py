from bs4 import BeautifulSoup
import requests
import re


response = requests.get('http://www.baidu.com')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')
print(soup)
