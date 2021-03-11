# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import csv
import os
from datetime import datetime


now = datetime.now()
data = now.strftime("%d/%m/%Y  %H:%M:%S"  )
dataList = []



with open('result.csv', mode='a') as data_file:
     data_writer = csv.writer(data_file, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
     dataList.append(data)
     data_writer.writerow(dataList)
     data_file.close()
    

   
    
    
import pandas
df = pandas.read_csv('result.csv')
size = df.size
shape = df.shape
df_ndim = df.ndim

import json
now = datetime.now()
dataitem = now.strftime("%d/%m/%Y %H:%M:%S")

data = {}
data['people'] = []
data['people'].append({
     'name': 'A',
     'Time': dataitem
    
    
}) 


data['people'].append({
    'name': 'C',
    'Time' : dataitem
})


with open('data.txt', 'a') as outfile:
          json.dump(data,outfile)
          
with open('data.txt') as json_file:
    data = json.load(json_file)
    for p in data['people']:
        print('Name: ' + p['name'])
        print('Time: '+ p['Time'])
        print(' ')
        
        

        
        
a = [dataitem]
a.append()


#Write Json             