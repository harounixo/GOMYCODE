#!/usr/bin/env python
# coding: utf-8

# In[20]:


def test(items):
    tot = 1
    for i in items:
        tot=i*tot
    return tot
print (test([2,3,6]))


# In[28]:


def test(elem):
    return elem[1]
liste = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
liste.sort(key=test)
    
print (liste)

    
    


# In[59]:


d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3 = {}
for i, j in d1.items():
    for x, y in d2.items():
                if i == x :
                    d3[i] = j+y
                    d3[z] = k
                    d3[u] = m
                    
                    
print(d3)


# In[2]:


x=int(input("your number : "))
test={i:i*i for i in range(1,x+1)}
print (test)
    


# In[7]:


price = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
print( sorted(price, reverse=True))


# In[ ]:




