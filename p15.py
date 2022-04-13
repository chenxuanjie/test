from urllib.request import urlopen
from bs4 import  BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs =BeautifulSoup(html.read(), 'html.parser')
namelist = bs.find_all(text='But tell me,')
print(len(namelist))
title = bs.find_all(id='redeviation-bs-sidebar')
print(title)
print("happy")