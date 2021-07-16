#!/usr/bin/env python
# coding: utf-8

# In[19]:


class Point3D(object):
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
my_point=Point3D(1,2,3)
print (my_point.x ,my_point.y ,my_point.z )


# In[29]:


class Rectangle:
    def __init__(self,l,w):
        self.length=l
        self.width=w
    def rectangle_area(self):
        return self.length*self.width
    def rectangle_perimeter(self):
        return 2*(self.length+self.width)
my_rectangle = Rectangle(4,3)
print("the area :",my_rectangle.rectangle_area())
print("the perimeter :",my_rectangle.rectangle_perimeter())
        


# In[31]:


class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14
    
    def perimeter(self):
        return 2*self.radius*3.14

NewCircle = Circle(8)
print(NewCircle.area())
print(NewCircle.perimeter())


# In[ ]:


class Bank_Account:
    def __init__(self):
        self.balance=0
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine")
  
    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:",amount)
  
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")
  
    def display(self):
        print("\n Net Available Balance=",self.balance)
  
# Driver code

# creating an object of class
    s = Bank_Account()
# Calling functions with that class object
i=1
while i<2 :  
    s.deposit()
    s.withdraw()
    s.display()


# In[ ]:




