# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 17:29:44 2021

@author: ncbc
"""

import requests
from bs4 import BeautifulSoup
import writer as w



URL = 'https://www.dawn.com/latest-news'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='all')
#print(results.prettify())


job_elems = results.find_all('article', class_='box')

i = 1
for job_elem in job_elems:
    a=[]
    title_elem = job_elem.find('a')
    
    
    if None in (title_elem):
        continue
    print('News Noo',str(i))
    print('Job Title =',title_elem.text.strip())
    a.append(title_elem.text.strip())
    w.csv_writers(a)
    print()
    i = i + 1
    