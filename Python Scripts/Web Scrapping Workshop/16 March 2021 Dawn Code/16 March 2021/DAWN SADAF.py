import requests
from bs4 import BeautifulSoup
import writer as w


URL= 'https://www.dawn.com/latest-news'
page= requests.get(URL)

soup= BeautifulSoup(page.content,'html.parser')
results =soup.find(id='all')
print(results.prettify())


job_elems = results.find_all('article',class_='box')
i=1
for job_elem in job_elems:
    a=[]
    title_elem= job_elem.find('div')
    if None in (title_elem):
        continue
    print('News No' ,str(i))
    print('News Title=',title_elem.text.strip())
    a.append(title_elem.text.strip())
    w.csv_writers(a)
    print()
    i=i+1