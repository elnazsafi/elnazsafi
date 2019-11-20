# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 16:03:12 2019

@author: Elnaz
"""

#%%%%%%%%%%%%%%

#TASK ONE
import numpy as np 

np.random.seed(100)
arr = np.random.randint(1,11,size=(6, 10))
arr

#define function to count values row wise
def rowwise_count_array(myarray):
# counts of the numbers in each rows
    counted_num = [np.unique(myrow, return_counts=True) for myrow in myarray]

# counts of values row wise
    return([[int(x[y==i]) if i in y else 0 for i in np.unique(myarray)] for y, x in counted_num])

# print the output
print(np.arange(1,11))
rowwise_count_array(arr)

#%%%%%%%%%%%%

#TASK TWO
import pandas as pd
# reading input from csv file
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv', usecols=[0,1,2,3,5])

#Replace NaNs with ‘missing’ in columns 'Manufacturer', 'Model' and 'Type'
df[['Manufacturer', 'Model', 'Type']] = df[['Manufacturer', 'Model', 'Type']].fillna('missing')

#create a index as a combination of these three columns
df.index = df.Manufacturer + '_' + df.Model + '_' + df.Type
print(df[['Manufacturer', 'Model', 'Type', 'Min.Price', 'Max.Price']])
# check if the index is a primary key
print(df.index.is_unique)