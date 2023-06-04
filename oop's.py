#!/usr/bin/env python
# coding: utf-8

# ### object orienteted progaming

# In[6]:


class Shivraj:     #class
    def welcome(self):     #method
        print('welcom to mine home all of you')
    var = 45
#creat a object

first_object = Shivraj()
first_object.welcome()
print(first_object.var)
    
    


# In[10]:


#creat class
class Tata:
    #method
    def welcome(self):
        print('welcome to here')
    def __init__(self):
        print("im an a constructor")

        
first_object=Tata() 
first_object.welcome()

    


# ### Self veriable

# In[1]:


class Student:
    
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
        
    def intro(self):
        print('Hello my name is:',self.name)
        print('My rollno is:',self.rollno)
        print('My marks are:',self.marks)


# In[2]:


s1=Student("shivraj",35,510)


# In[3]:


s1.intro()


# In[5]:


s2=Student('raj',20,450)
s2.intro()


# #### instance veriables (OBJECT LEVEL VARIABLE)

# In[9]:


class Employee:
    def __init__(self):
        self.eno=100
        self.ename="shivraj"
        self.esal=20000
        
e=Employee()
print(e.__dict__)


# In[11]:


class Test:
    
    def __init__(self):
        self.a=10
        self.b=20
        
    def m1(self):
        self.c=30
        
t=Test()
t.m1()
print(t.__dict__)
print(Test)


# In[12]:


t.d=40


# In[13]:


print(t.__dict__)


# In[14]:


print(t.a,t.b)


# In[16]:


t.m1()
print(t.a,t.b)


# In[24]:


class Test:
    
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30
        self.d=40
    def m1(self):
        del self.b      #deleting item mention here


# In[25]:


t1=Test()
print(t.__dict__)


# In[26]:


t1.m1()
print(t1.__dict__)


# In[30]:


t2=Test()
print(t.__dict__)


# In[33]:


t1=Test()
t1.a=888
t1.b=999
t2=Test()


print('t1:',t1.a,t1.b)
print('t2:',t2.a,t2.b,t2.c)


# ### Various Places to declear static Variables

# In[5]:


class Test:
    a=10


    def __init__(self):
        print(self.a)   #veriable inside constructor using self
        print(Test.a)   #veriable inside constructor using class name
    
    def m1(self):
        print(self.a) # veriable inside constuctor using self
        print(Test.a) # veriable inside a constructor using class name 
        
    @classmethod     
    def m2(cls):
        print(cls.a)
        print(Test.a)
        
    @staticmethod
    def m3():
        print(Test.a)
    
    


# In[6]:


t=Test()


# In[7]:


print(Test.a)


# In[9]:


t.m1()
t.m2()
t.m3()


# ### Local veriable

# localveriable are importatnt only for perticular method

# ### Types of Nethod
# 
# ### 1. instance Method:

# In[4]:


class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
    def display(self):
        print("Hi",self.name)
        print("your mrks are:",self.marks)
        
    def grade(self):
        if self.marks>=80:
            print("you got first class")
        elif self.marks>=60:
            print("you got secnd class")
        elif self.marks>=40:
            print("you got third class")
        else:
            print("you are failed")
            
            
n=int(input("Enter number of students:"))
for i in range(n):
    name=input("Enter name:")
    marks=int(input("Enter the marks"))
    s=Student(name,marks)
    s.display()
    s.grade()
    print()
        


# ### Class method

# In[6]:


class Animal:
    legs=4
    
    @classmethod
    def walk(cls,name):
        print('{} walk with {} the leg'.format(name,cls.legs))
        
        
Animal.walk('dog')
Animal.walk('cat')


# ### 3. Static Methods:

# In[3]:


class Basicmath:
    
    @staticmethod
    def add (x,y):
        print('the sum is:',x+y)
        
    @staticmethod
    def subtract(x,y):
        print('The subtract is:',x-y)
        
Basicmath.add(10,20)
Basicmath.subtract(20,10)


# ### 1.Composition (Has-A-Relationship):

# In[4]:


class Engine:
    a=10          #car has a Engine
    
    def __init__(self):
        self.b=20
        
    def m1(self):
        print('Engine specific functionality')
        
class Car1:
    def __init__(self):
        self.engine=Engine()
        
    def m2(self):
        print("car using engine class functionality")
        print(self.engine.a)
        print(self.engine.b)
        self.engine.m1()
        


# In[5]:


c=Car1()


# In[6]:


c.m2()


# ### 2.Inheritance (Is-A-Relationship)

# In[8]:


class Parent:
    def func1(self):     #Single inheritance
        print("This function 1")
        
class Child(Parent):
    def func2(self):
        print("This is function 2")


# In[10]:


ob=Child()


# In[13]:


ob.func1()


# In[14]:


ob.func2()


# ### Type of Inheritance

#  ### Single inheritationship
#  
#  the concept of inheritance the properties from one class to another class is known as a single inheritance

# In[3]:


class Parent:
    def func1(self):
        print("this is function 1")
class Child (Parent):
    def func2(self):
        print("this is function 2")
        


# In[4]:


ob=Child()


# In[5]:


ob.func1()

