# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 16:55:58 2021

@author: ncbc
"""


import csv
import os
from datetime import datetime

def csv_writers(x):
    with open('result.csv', mode='a') as data_file:
        data_writer = csv.writer(data_file,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        data_writer.writerow(x)
        data_file.close()