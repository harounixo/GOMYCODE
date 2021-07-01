#!/usr/bin/env python
# coding: utf-8

# In[53]:


firstname=str(input("first name"))
lastname=str(input("last name"))
print (lastname, firstname)


# In[57]:


n=int(input("Your number : "))
print (n+n*11+n*111)


# In[69]:


x=int(input('your number : '))
if x%2==0:
    print("even number detected")
else :
    print("odd number detected")


# In[10]:


for i in range (1999,3201):
    if i%7==0:
        if i%5==0:
            print()
        else :
            print(i,end="/")
        
        
    
   
               


# In[130]:


x=1
number=int(input("your number : "))
if number<0:
    print("factorial does not exist for negative numbers")
else :    
    if number==0:
        print("the factorial of 0 is 1")
    elif number>0:
        for i in range (1,number+1):
            x=x*i
        print("the factorial of ",number,"is",x)
                
        
        
        


# In[ ]:


phrase=str(input("your senten : "))

def remove(phrase):
    x=""
    for i in range (len(phrase)):
        if i%2==0:
            x=x+phrase[i]
    return x
print(remove(phrase))
        


# In[11]:


price=int(input("your price : "))
if price>=500:
    print("your new price is : ",price/2)
if  200<=price<500:
    print("your new price is : ",price*70/100)
if price<200:
    print("your new price is : ",price*90/100)


# In[ ]:




