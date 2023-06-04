#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import numpy as np


# In[1]:


get_ipython().run_line_magic('matplotlib', 'notebook')

# %matplotlib inline


# In[3]:


x = [1,2,3,4,5,6,7,8,9]
y = [38,50,42,48,40,45,39,35,37]


# In[4]:


plt.xlabel('Day')
plt.ylabel('Temp')
plt.plot(x,y,'r+')


# In[7]:


plt.xlabel('Day')
plt.ylabel('Temp')
plt.plot(x,y,marker = 'o',linestyle ='-.',markersize = 10,linewidth = 3)


# In[8]:


plt.xlabel('Day')
plt.ylabel('Temp')
plt.title('Weather')
plt.plot(x,y,'ro:')


# In[9]:


plt.xlabel('Day')
plt.ylabel('Temp')
plt.title('Weather')
plt.plot(x,y,'r+--')


# In[10]:


plt.xlabel('Day')
plt.ylabel('Temp')
plt.plot(x,y,marker = 'o',linestyle ='--',markersize = 10,linewidth = 3)


# In[11]:


plt.xlabel('Day')
plt.ylabel('Temp')
plt.plot(x,y,marker = 'o',linestyle ='--',markersize = 10,linewidth = 3,alpha = 0.5)


# In[12]:


days=[1,2,3,4,5,6,7]
max_t=[50,51,52,48,47,49,46]
min_t=[43,42,40,44,33,35,37]
avg_t=[45,48,48,46,40,42,41]


# In[13]:


plt.plot(days, max_t, label="max")
plt.plot(days, min_t, label="min")
plt.plot(days, avg_t, label="average")


# In[14]:


plt.xlabel('Days')
plt.ylabel('Temp')
plt.title('Weather')
plt.plot(days,max_t)
plt.plot(days,min_t)
plt.plot(days,avg_t)


# In[15]:


plt.xlabel('Days')
plt.ylabel('Temp')
plt.title('Weather')
plt.plot(days,max_t,label = 'max')
plt.plot(days,min_t,label = 'min')
plt.plot(days,avg_t,label = 'avg')

plt.legend(loc='lower left')


# In[16]:


plt.xlabel('Days')
plt.ylabel('Temp')
plt.title('Weather')
plt.plot(days,max_t,label = 'max')
plt.plot(days,min_t,label = 'min')
plt.plot(days,avg_t,label = 'avg')

plt.legend(loc='lower left',shadow= True,fontsize ='large')

plt.grid(linestyle = '--',linewidth = 1,color = 'blue')


# In[17]:


company = ['TCS','INFY','TECMAHI','WIPRO']
revenue = [100,30,15,12]


# In[18]:


plt.bar(company,revenue,label = 'Revenue')
plt.xlabel('Company')
plt.ylabel('Revenue(Biln)')
plt.title('Indian Tech stock')
plt.legend()


# In[19]:


xpos = np.arange(len(company))
xpos


# In[20]:


plt.bar(xpos+0.2,revenue,label= 'Revenue')

plt.xticks(xpos,company)
plt.ylabel('revenue(biln)')
plt.legend()


# In[21]:


plt.bar(xpos,revenue,label= 'Revenue',width = 0.5)

plt.ylabel('revenue(biln)')
plt.legend()


# In[22]:


profit = [80,20,8,5]


# In[23]:


plt.bar(xpos-0.2,revenue,width = 0.4,label = 'Revenue')
plt.bar(xpos+0.2,profit,width = 0.4,label = 'Profit')

plt.xticks(xpos,company)
plt.ylabel('Revenue(Biln)')
plt.title('IND Tech Stock')
plt.legend()


# In[24]:


plt.barh(xpos-0.2,revenue,label = 'Revenue',)
# plt.barh(xpos+0.2,profit,label = 'Profit')

plt.yticks(xpos,company)
plt.ylabel('Revenue(Biln)')
plt.title('IND Tech Stock')
plt.legend()


# In[25]:


blood_sugar = [113, 85, 90, 150, 149, 88, 93, 115, 135, 80, 77, 82, 129]
plt.hist(blood_sugar,bins=10,rwidth = 0.8)


# In[26]:


plt.hist(blood_sugar,bins = 10,rwidth = 0.8,color = 'orange')
plt.xlabel('Sugar Level')
plt.ylabel('No. of Patients')
plt.title('Blood Sugar chart')


# In[27]:


plt.hist(blood_sugar,bins = [75,100,125,150],rwidth = 0.9,color = 'orange')
plt.xlabel('Sugar Level')
plt.ylabel('No. of Patients')
plt.title('Blood Sugar chart')


# In[28]:


plt.xlabel("Sugar Level")
plt.ylabel("Number Of Patients")
plt.title("Blood Sugar Chart")

blood_sugar_men = [113, 85, 90, 150, 149, 88, 93, 115, 135, 80, 77, 82, 129]
blood_sugar_women = [67, 98, 89, 120, 133, 150, 84, 69, 89, 79, 120, 112, 100]

plt.hist([blood_sugar_men,blood_sugar_women],bins=[75,100,125,150],label = ['Men','Women'],color=['green','orange'],rwidth = 0.9)
plt.legend()


# In[29]:


plt.xlabel("Sugar Level")
plt.ylabel("Number Of Patients")
plt.title("Blood Sugar Chart")

blood_sugar_men = [113, 85, 90, 150, 149, 88, 93, 115, 135, 80, 77, 82, 129]
blood_sugar_women = [67, 98, 89, 120, 133, 150, 84, 69, 89, 79, 120, 112, 100]

plt.hist([blood_sugar_men,blood_sugar_women],bins=[75,100,125,150],label = ['Men','Women'],color=['green','orange'],rwidth = 0.9,histtype = 'barstacked')
plt.legend()


# In[30]:


plt.xlabel("Sugar Level")
plt.ylabel("Number Of Patients")
plt.title("Blood Sugar Chart")

blood_sugar_men = [113, 85, 90, 150, 149, 88, 93, 115, 135, 80, 77, 82, 129]
blood_sugar_women = [67, 98, 89, 120, 133, 150, 84, 69, 89, 79, 120, 112, 100]

plt.hist([blood_sugar_men,blood_sugar_women],bins=[75,100,125,150],label = ['Men','Women'],color=['green','orange'],rwidth = 0.9,histtype = 'bar',orientation= 'horizontal')
plt.legend()


# In[31]:


plt.xlabel("Sugar Level")
plt.ylabel("Number Of Patients")
plt.title("Blood Sugar Chart")

blood_sugar_men = [113, 85, 90, 150, 149, 88, 93, 115, 135, 80, 77, 82, 129]
blood_sugar_women = [67, 98, 89, 120, 133, 150, 84, 69, 89, 79, 120, 112, 100]

plt.hist([blood_sugar_men,blood_sugar_women],bins=[75,100,125,150],label = ['Men','Women'],color=['green','orange'],rwidth = 0.9,histtype = 'barstacked',orientation= 'horizontal')
plt.legend()


# In[32]:


exp_vals = [2000,1000,500,800,700]
exp_labels = ['home rent','food','phone bill','bike','other']
plt.pie(exp_vals,labels=exp_labels)


# In[33]:


exp_vals = [2000,1000,500,800,700]
exp_labels = ['home rent','food','phone bill','bike','other']
plt.pie(exp_vals,labels=exp_labels,shadow = True,autopct= '%1.1f%%')
plt.show()


# In[60]:


exp_vals = [2000,1000,500,800,700]
exp_labels = ['home rent','food','phone bill','bike','other']
plt.pie(exp_vals,labels=exp_labels,shadow = True,autopct= '%1.1f%%',radius = 1.2)
plt.show()


# In[42]:


exp_vals = [2000,1000,500,800,700]
exp_labels = ['home rent','food','phone bill','bike','other']
plt.pie(exp_vals,labels=exp_labels,shadow = True,autopct= '%1.1f%%',radius = 1.2,explode=[0.1,0.2,0.3,0,0.1])
plt.show()


# In[50]:


exp_vals = [2000,1000,500,800,700]
exp_labels = ['home rent','food','phone bill','bike','other']
plt.pie(exp_vals,labels=exp_labels,shadow = True,autopct= '%1.1f%%',radius = 1.2,explode=[0.1,0.2,0.3,0,0.1])
plt.show()
plt.axis()


# In[59]:


exp_vals = [2000,1000,500,800,700]
exp_labels = ['home rent','food','phone bill','bike','other']
plt.pie(exp_vals,labels=exp_labels,shadow = True,autopct= '%1.1f%%',radius = 1.2,explode=[0.1,0.2,0.3,0,0.1],counterclock = True,startangle = 45)
plt.show()


# In[68]:


exp_vals = [2000,1000,500,800,700]
exp_labels = ['home rent','food','phone bill','bike','other']
plt.pie(exp_vals,labels=exp_labels,shadow = True,autopct= '%1.1f%%',radius = 1.2,explode =[0,0.1,0,0,0])
plt.show()
plt.savefig('./piechar.pdf',bbox_inches='tight',pad_inches = 1,transparent = True,facecolor = 'auto',edgecolor = 'auto')

