#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
import requests
from bs4 import BeautifulSoup


# In[2]:


inp=input()
s=requests.get(inp+'/about')


# In[3]:


#print(s.text)


# In[4]:


soup=BeautifulSoup(s.text,'html.parser')


# In[5]:


href=soup.find_all('a','')


# In[6]:


links=[]
for i in href:
    links.append(i.get('href'))


# In[7]:


#links


# In[8]:


# print(re.findall(re.compile("\W*\d*\W?\d{3}\W*\d{3}\W?\d{4}"),s.text))


# In[9]:


# gml='\w*@'+inp.split('//')[1]
# print(gml)
# print(re.findall(re.compile(gml),s.text))


# In[10]:


l=['facebook','linkedin','instagram']
sml=set()
print("Social links -")
for i in links:
    for j in l:
        if i.find(j)!=-1:
            sml.add(i)
print('\n'.join(sml))


# In[11]:


gml='\w*@'+inp.split('//')[1]
print("Email/s-")
print(*set(re.findall(re.compile(gml),s.text.lower())))


# In[12]:


print("Contact: ")
print(*re.findall(re.compile("\W?\d*\W*\d{3,}\W*\d{3,}\W?\d{4,}"),' '.join(links)))
input()
