# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 17:02:22 2021

@author: ncbc
"""


import csv
import os
from datetime import datetime


now = datetime.now()
data = now.strftime("%d/%m/%Y  %H:%M:%S"  )
dataList = []
dataList.append(data)


def csv_writter(x):
    with open('result.csv', mode='a') as data_file:
        data_writer = csv.writer(data_file, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
    #    dataList.append(data)
        data_writer.writerow(x)
        data_file.close()
    

csv_writter(dataList)