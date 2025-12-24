# Standard Library Overview
# Python's Standard Library is a vast collection of modules and packages that come bundled with Python, providing a wide range of functionalities out of the box. Here's an overview of some of the most commonly used modules and packages in the Python Standard Library.

import array
arr=array.array('i',[1,2,3,4])
print(arr)
# output: array('i', [1, 2, 3, 4])


import math
print(math.sqrt(16))
print(math.pi)

# output : 4.0
#        3.141592653589793 

## random 

import random
print(random.randint(1,10))
# print(random.choice(['apple','banana','cherry'])) output :2  cherry


### File And Directory Access

import os
print(os.getcwd())


## High level operations on files and collection of files
import shutil
shutil.copyfile('source.txt','destination.txt') 
# output : destination.txt'


## Data Serialization
import json
data={'name':'Krish','age':25}

json_str=json.dumps(data)
print(json_str)
print(type(json_str))

parsed_data=json.loads(json_str)
print(parsed_data)
print(type(parsed_data))

## Regular expresiion
import re

pattern=r'\d+'
text='There are 123 apples 456'
match=re.search(pattern,text)
print(match.group())

## time
import time
print(time.time())
time.sleep(2)
print(time.time())


## datetime
from datetime import datetime,timedelta

now=datetime.now()
print(now)

yesterday=now-timedelta(days=1)

print(yesterday)


## csv

import csv

with open('example.csv',mode='w',newline='') as file:
    writer=csv.writer(file)
    writer.writerow(['name','age'])
    writer.writerow(['Krish',32])

with open('example.csv',mode='r') as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)