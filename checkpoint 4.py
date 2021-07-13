#!/usr/bin/env python
# coding: utf-8

# In[1]:


def max(a,b,c):
    if a>b:
        if a>c:
            print(a,"is the max")
    elif b>a:
        if b>c:
            print(b,"is the max")
    elif c>a:
        if c>b:
            print(c,"is the max")
max(20,35,19)


# In[5]:


a=int(input("a :"))
b=int(input("b :"))
def calculation(a,b):
    z=a+b
    s=a-b
    return (z,s)
    print(z,s)
calculation(a,b)


# In[20]:


list1 = [11, 5, 17, 18, 23]
def sums(list1):
    total = sum(list1)
    print(total)
list2 = [1, 2, 3]
def multiplyList(list2) :
    result = 1
    for x in list2:
         result = result * x
    return result

sums(list1)
multiplyList(list2)


# In[21]:


def test(items):
    items=[n for n in input().split('-')]
    items.sort()
    print('-'.join(items))
test(items)


# In[ ]:




