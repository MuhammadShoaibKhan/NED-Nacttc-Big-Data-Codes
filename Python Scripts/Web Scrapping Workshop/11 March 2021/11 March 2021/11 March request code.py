# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 15:37:48 2021

@author: ncbc
"""

import requests
from bs4 import BeautifulSoup
import csv

def csv_writers(x):
    with open('result.csv', mode='a') as data_file:
        data_writer = csv.writer(data_file,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        data_writer.writerow(x)
        data_file.close()
        
        
URL = 'https://pk.indeed.com/jobs?q=python&d='

#URL = 'https://pk.indeed.com/jobs?q=python&d='

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='')
print(results.prettify())

job_elems = results.find_all(",class_=")
for job_elem in job_elems:
    print(job_elem, end='\n'*2)


i = 1
data = []
for job_elem in job_elems:
    title_elem = job_elem.find('',class_='')
    company_elem = job_elem.find('',class_='')
    summary = job_elem.find('',class_='')
    location_elem = job_elem.find('',class_='')
    date = job_elem.find('',class_='')
    
    if None in (title_elem, summary, company_elem, location_elem, data):
        continue
    print('Job Number ',str(i))
    print('Job Title = ',title_elem.text.strip())
    print('Company Name =', company_elem.text.strip())
    print('Job Description = ',summary.text.strip())
    print('Location = ',location_elem.text.strip())
    print('Job Posting Date', date.text.strip())
    print()
    i = i+1
    

    
    
