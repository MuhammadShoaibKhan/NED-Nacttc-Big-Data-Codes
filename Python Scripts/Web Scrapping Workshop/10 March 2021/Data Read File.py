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


def abc(a):
    with open('result.csv', mode='a') as data_file:
        data_writer = csv.writer(data_file, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        dataList.append(data)
        data_writer.writerow(dataList)
        data_file.close()
    

abc(a)    
    
    
import pandas
df = pandas.read_csv('resullt.csv')
size = df.size
shape = df.shape
df_ndim = df.ndim

import json
now = datetime.now()
dataitem = now.strftime("%d/%m/%Y %H:%M:%S")

data = {}
data['people'] = []
data['people'].append({
    
    
    
    }) 
