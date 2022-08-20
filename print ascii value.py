#!/usr/bin/env python
# coding: utf-8

# # Write a Python program to print a dictionary whose keys should be the alphabet from a-z and the value should be corresponding ASCII values.

# In[37]:


dic={}
for i in range(97,123):
    dic[chr(i)]=i
print(dic)

