#!/usr/bin/env python
# coding: utf-8

# ### Type of veriables
# 
# 1. global
# 2.local

# In[1]:


x= "awesome"
def myfunc():
    print("python is "+ x)
myfunc()    


# ### creating a global keyword
# 1 normally, when you ceart a veriable inside a a function,that veriable is local,and used inside that function .
# 
# 2. to creat a global veriable inside a function, you can use the global keyword.
#     
#     

# In[2]:


def myfunc():
    global y
    y="fantastic"
myfunc()
print("python is "+y)


# In[4]:


def function():
    global x
    x= "superstar"
function()
print("rajnikat called as a " + x)


# In[5]:


x= "awesome"
def func():
    global x
    x= "fantastic"
func()
print("python is "+x)


# In[7]:


w= "SAD"
def greet():
    global w
    w="HAPPY"
greet()
print("how you feel "+ w)


# In[8]:


x= 'global_x'
def func():
    y= 'local_y'
    z= x+y
    print(y)
    print(z)
func()
print(x)


# In[13]:


x="global_x"
def foo():
    y="local_y"
    global x
    x=x+y
    print(x)
    print(y)
foo()
print(x)


# In[18]:


total=0
def sum(*numbers):
    total=0
    for n1 in numbers:
        total = total +n1
    print("inside the function local total:",total)   
sum(10,20,30,50)    
print("outside the function global total:",total)    


# ### Aliasing function  
# for existing function we can give another name, which can nothing but
# function Aliasing

# In[23]:


def greet(name):
    print("good morning:",name)
    


# In[24]:


greeting=greet


# In[25]:


print(id(greet))
print(id(greeting))


# In[26]:


greet("shiva")
greeting("shiva")


# #### if we delete one name still we can access that function by using alias name

# In[27]:


del(greet)
greeting("shiva")


# #### Neasted function
# we can declare a function inside another function, such type of functions aew called neasted function
# 

# In[36]:


def outer():
    print("outer function started")
    def inner(): 
        print("inner function execution")
        print("outer function execution")
    inner()

outer()


# #### Another example

# In[44]:


def f():
    def x(a,b):
        return a+b
    return x
val=f()(3,4)
print(val)


# In[ ]:




