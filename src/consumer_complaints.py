# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 15:35:47 2020

@author: saran
"""
import sys
import csv
import time
from collections import Counter
import math

def sort(sub_li): 
    return sorted(sub_li, key=lambda x: (x[0], x[1], x[2]))

def rounding(n):
    if n- math.floor(n) >= 0.5:
        return math.ceil(n)
    return math.floor(n)

def data_output(data_dict, dir):
    with open(output_file, 'w', newline='') as file:      
        writer = csv.writer(file)
        for k, c in data_dict.items(): 
            tot_complaints=len(c)
            high_comp=max(Counter(c).values())
            n_companies=len(Counter(c).keys())
            high_per=rounding((high_comp/tot_complaints)*100)
            yr_pro=k.split("|")
            year=yr_pro[0]
            product=yr_pro[1]
            #check=","
            #if check in product:
            #    product='"'+product+'"'
            writer.writerow([product,year,tot_complaints, n_companies,high_per])    

def data_processing(data_m,dir):
    data=[]
    for column in data_m:
        date_received=column[0]
        product=column[1].lower()
        company=column[7]
        temp_list=[date_received, product, company]
        data.append(temp_list)
    
    for line in data[1:]:
        date=line[0]
        date_split=date.split("-")
        year=date_split[0]
        line[0]=year
   
    data_copy=sort(data[1:])
    d_dict = {}
    for cr in data_copy:
        if "|".join(cr[0:2]) in d_dict:
            company=cr[2]
            d_dict["|".join(cr[0:2])].append(company)  
        else:
            d_dict["|".join(cr[0:2])] = cr[2:]
    data_output(d_dict,dir)

if __name__ == "__main__":
    start1 = time.time()
    dir='C:/New_partition/Project_insight/'
    input_file=sys.argv[1]
    output_file=sys.argv[2]
    with open(input_file,mode='r' ,newline='',encoding='utf8') as f:
        reader = csv.reader(f)
        #data_m = list(reader)
        data_processing(list(reader),dir)    
    