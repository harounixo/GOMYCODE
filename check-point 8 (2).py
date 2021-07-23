#!/usr/bin/env python
# coding: utf-8

# In[24]:



with open("python.txt",encoding = 'utf-8') as f:

    f = open("python.txt",'r',encoding = 'utf-8')
f.read()


# In[1]:


a_file = open("python.txt")
number_of_lines = int(input())
for i in range(number_of_lines):
    line = a_file. readline()
print(line)


# In[3]:


n1 = int(input())
def read_lastnlines(fname,n):
    with open('python.txt') as f:
        for line in (f.readlines() [-n:]):
            print(line)
read_lastnlines('python.txt',n1)


# In[5]:


print("choose your file path or file")
a = input()
def count_words(filepath):
    with open(filepath) as d:
        data = d.read()
        data.replace(",", " ")
        return len(data.split(" "))
print(count_words(a))


# In[ ]:




