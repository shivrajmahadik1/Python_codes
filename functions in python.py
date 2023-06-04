#!/usr/bin/env python
# coding: utf-8

# In[1]:


def greet():
    print("Hello")
    print("good morning")
greet()    
    


# In[3]:


def greet():
    print("Hello")
    print("good morning")
def add(x,y):
    c=x+y
    print(c)
add(5,4)   
greet()


# In[21]:


def add(x,y):
    c=x+y
    return(c)
    
result=add(200,400)  
print(result)


# In[1]:


def wish():
    print("Hello good morning")

wish()    


# In[3]:


def wish(name):
    print("Hello",name,"good morning")
wish("ravi")
wish("durga")


# In[16]:


def greet (name):
     print(f'Hello {name} Good Evening!')
greet('rohit')   


# In[17]:


greet('sameer')


# In[19]:


def print_sum(a,b):
    print(a+b)


# In[20]:


def return_sum(a,b):
    return a+b


# In[21]:


print_sum(10,15)


# In[22]:


return_sum(10,15)


# In[23]:


my_result=print_sum(10,15)


# In[24]:


print(my_result)


# In[25]:


my_result= return_sum(10,15)


# In[26]:


my_result


# In[33]:


def is_even1(number):
    if number % 2==0:
        return "even"
    else:
        return "odd"
x= is_even1(40)
print(x)


# In[1]:


def wish():
    print("hello")
    print("good morning")
    print("how are you today")
wish()    


# In[7]:


def name(name):
    print(" hello",name,"welcome")
name("ravi")    


# In[10]:


def name(name):
    print(f"hello {name} welcome")    #f format method
name("ravi") 


# In[14]:


def print_sum(a,b):
    return a+b


# In[20]:


print_sum(20,30)


# In[21]:


def sum(a,b):
    return a+b
    


# In[22]:


sum(20,30)


# In[31]:


def cal(a,b):
    sum= a+b
    sub= a-b
    mul= a*b
    div= a/b
    return sum,sub,mul,div
t= cal(200,100)
print("the result are")
for i in t:
      print(i)


# In[32]:


t=cal(10,5)


# In[33]:


print("the result are")
for i in t:
      print(i)


# In[42]:


def even_num(number):
    if number %2==0:
        return("given number are even")
        
    else:
        return("given number are odd")
x=even_num(40)
print(x)


# In[43]:


x=even_num(41)
print(x)


# In[44]:


def even_odd(num):
    if num%2==0:
        print(num,"even number")
        
    else:
        print(num,"it is odd number")
even_odd(21)
even_odd(22)


# ### Global and local function

# In[50]:


x= "awesome"
def myfunc():
    print("python is", x)
myfunc()    


# In[55]:


x= "awesome"
def myfunc():
    x="fantastic"
    print("python is ", x)
myfunc() 
print("python is",x)


# In[56]:


def myfunc():
    global y
    y= "fantastic"
myfunc()
print("python is",y)


# In[60]:


x=" awesome"
def myfunc():
    global x
    x="fantastic"
myfunc()
print("python is" ,x)


# In[61]:


x= "global_x"
def foo():
    y= "local_y"
    z= x+y
    print(y)
    print(z)
    
foo()
print(x)


# In[68]:


x= "global_x"
def foo():
    y= "local_y"
    global x
    x= x+y
    print(x)
    print(y)
    
foo()
print(x)


# ## advance functions 
# 
# **Recursive function**

# In[69]:


def factorial(n):
    if n==0:
        result=1
    else:
        result= n*factorial(n-1)
    return result    


# In[71]:


factorial(5)


# In[72]:


factorial(3)


# In[73]:


factorial(2)


# # Lambda

# In[78]:


sqrIt= lambda n:n*n


# In[79]:


print(sqrIt(12))


# In[80]:


sqrIt(24)


# In[81]:


sum1=lambda n:n+n


# In[82]:


sum1(30)


# In[83]:


sum1(22)


# In[86]:


sum2= lambda a,b:a+b


# In[87]:


sum2(20,5)


# In[88]:


s= lambda a,b: a if a>b else b
s(10,20)


# In[89]:


s(200,100)


# In[ ]:




