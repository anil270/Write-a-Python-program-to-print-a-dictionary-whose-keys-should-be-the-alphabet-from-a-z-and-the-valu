#!/usr/bin/env python
# coding: utf-8

# # Write a Python program to print a dictionary whose keys should be the alphabet from a-z and the value should be corresponding ASCII values.

# In[37]:


dic={}
a = int(input())
b = int(input())
for i in range(a,b):
    dic[chr(i)]=i
print(dic)

