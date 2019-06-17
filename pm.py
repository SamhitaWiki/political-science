# -*- coding: utf-8 -*-
"""
Created on Wed May  1 11:23:42 2019

@author: Rajesh
"""
import os
import urllib.request
import pandas as pd
import csv

#import titlecase
from bs4 import BeautifulSoup
pm = "https://archivepmo.nic.in/" #reading the url of the recipe
page1 = urllib.request.urlopen(pm)
soup = BeautifulSoup(page1,features="lxml")
t = []
write = soup.find_all('div', {"id":"Container"})




for i in write:
    tds= i.text.splitlines()
    print("  hello  : \n",tds[1])
    #print("###########################################")
    #if tds != '' :
    #t.append[tds]
        
len(tds)  

for i in range(len(tds)):
    if tds[i] != '' :
        t.append(tds[i])
        

print(t[1].split()[1])
n = len(t[1].split())
start = []
end = []
name = []
df  = pd.DataFrame()
df1  = pd.DataFrame()

for i in range(len(t)):
    print("i",i)
    n = len(t[i].split())
    print("n ", n)
    if n != 7 and n !=14 and n !=13 and n != 6:
        print("########################")
        name.append(t[i])
    if n == 14:
        s = t[i].split()
        print(len(s))
        start.append(s[0]+' '+s[1]+' '+s[2]+','+s[7]+' '+s[8]+' '+s[9])
        end.append(s[4]+' '+s[5]+' '+s[6]+','+s[11]+' '+s[12]+' ' +s[13])
    if n == 7 :
        s = t[i].split()
        print(len(s))
        start.append(s[0]+' '+s[1]+' '+s[2])
        end.append(s[4]+' '+s[5]+' '+s[6])
    if n == 6 :
        s = t[i].split()
        print(len(s))
        start.append(s[0]+' '+s[1]+' '+s[2])
        end.append(s[3]+' '+s[4]+' '+s[5])
    if n == 13 :
        s = t[i].split()
        print(len(s))
        start.append(s[0]+' '+s[1]+' '+s[2]+','+s[7]+' '+s[8])
        end.append(s[4]+' '+s[5]+' '+s[6]+','+s[10]+' '+s[11]+' ' +s[12])
            
df1['name'] = name
df['start'] = start
df['end'] = end

a = pd.concat([df,df1], ignore_index=True, axis=1)

a.to_csv('pm.csv')

df1 = pd.DataFrame({'name':name,'start':start,'end':end}) 



#for i in range(len(t)):
 #   n = len(t[i].split())
  #  print(n)
     
#print(t[9])      
        
    