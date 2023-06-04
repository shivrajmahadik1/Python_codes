#!/usr/bin/env python
# coding: utf-8

# ## Scatter plots

# In[38]:


import pandas as pd
import seaborn as sns
import numpy as np


# In[2]:


df= pd.read_csv("dm_office_sales.csv")


# In[3]:


df.head()


# In[4]:


df.info()


# In[5]:


sns.scatterplot(x='salary',y='sales',data=df)


# In[6]:


import matplotlib.pyplot as plt


# In[7]:


plt.figure(figsize=(12,8))
sns.scatterplot(x='salary',y='sales',data=df)
plt.show()


# In[8]:


plt.figure(figsize=(12,8))
sns.scatterplot(x='salary',y='sales',hue='division',data=df)
plt.show()


# In[9]:


plt.figure(figsize=(12,8))
sns.scatterplot(x='salary',y='sales',hue= 'work experience',data=df)
plt.show()


# In[10]:


plt.figure(figsize=(12,8))
sns.scatterplot(x='salary',y='sales',hue= 'work experience',data=df,palette='Blues')
plt.show()


# ## size()

# In[11]:


plt.figure(figsize=(12,8))
sns.scatterplot(x='salary',y='sales',size= 'work experience',data=df)
plt.show()


# In[12]:


plt.figure(figsize=(12,8))
sns.scatterplot(x='salary',y='sales',data=df,size='work experience')
plt.show()


# In[13]:


plt.figure(figsize=(12,8))
sns.scatterplot(x='salary',y='sales',data=df,s=100,linewidth=0.5,alpha=0.1 )


# ## Style()

# In[14]:


plt.figure(figsize=(12,8))
sns.scatterplot(x='salary',y='sales',data=df,style='level of education')


# In[15]:


plt.figure(figsize=(12,8))
sns.scatterplot(x='salary',y='sales',hue= 'level of education',data=df,style='level of education')
plt.show()


# In[16]:


plt.figure(figsize=(12,8))
sns.scatterplot(x='salary',y='sales',hue= 'level of education',data=df,style='level of education',s=100)
plt.show()


# In[17]:


import pandas as pd


# ## Rugplot

# In[18]:


sns.rugplot(x='salary',data=df)


# In[19]:


sns.rugplot(x='salary',data=df,height=0.5)


# # distplot and histplot

# In[20]:


sns.displot(data=df,x='salary',hue='level of education',palette='viridis')


# In[21]:


sns.displot(data=df,x='salary',kde=True)


# In[22]:


sns.displot(data=df,x='salary')


# In[23]:


sns.histplot(data=df,x='salary')


# In[24]:


sns.histplot(data=df,x='salary',bins=50)


# In[25]:


sns.set(style='darkgrid')
sns.histplot(data=df,x='salary',bins=50)


# In[26]:


sns.set(style='white')
sns.histplot(data=df,x='salary',bins=50)


# In[28]:


plt.figure(figsize=(14,8),dpi=300)
sns.countplot(x='division',data=df)


# In[29]:


plt.figure(figsize=(14,8),dpi=100)
ax=sns.countplot(x='division',data=df)
ax.bar_label(ax.containers[0])


# In[30]:


plt.figure(figsize=(14,8),dpi=300)
sns.countplot(x='level of education',data=df)


# In[31]:


plt.figure(figsize=(14,8),dpi=200)
sns.countplot(x='level of education',data=df,hue='training level')


# In[32]:


plt.figure(figsize=(14,8),dpi=200)
sns.countplot(x='level of education',data=df,hue='training level',palette='Set1')


# In[33]:


plt.figure(figsize=(14,8),dpi=200)
ax=sns.countplot(x='level of education',data=df,hue='training level',palette='Set1')
for container in ax.containers:
    ax.bar_label(container)


# ## barplot()

# In[39]:


plt.figure(figsize=(10,6))
sns.barplot(x='level of education',y='salary',data=df,estimator=np.mean,ci='sd')


# In[42]:


plt.figure(figsize=(14,10))
sns.barplot(x='level of education',y='salary',data=df,estimator=np.mean,ci='sd',hue='division')


# In[45]:


plt.figure(figsize=(14,10))
sns.barplot(x='level of education',y='salary',data=df,estimator=np.mean,ci='sd',hue='division')
plt.legend(bbox_to_anchor=(1,1))


# In[46]:


df= pd.read_csv("StudentsPerformance.csv")


# In[47]:


df.head()


# ## Boxplot

# In[48]:


plt.figure(figsize=(12,6))
sns.boxplot(x='parental level of education',y='math score',data=df)


# In[49]:


plt.figure(figsize=(12,6))
sns.boxplot(x='parental level of education',y='math score',data=df,hue='gender')


# ## Boxplot styling paramerter

# In[54]:


sns.boxplot(y='parental level of education',x='math score',data=df,orient='h')


# **Width**

# In[58]:


plt.figure(figsize=(12,6))
sns.boxplot(x='parental level of education',y='math score',data=df,hue='gender',width=.4)


# **violinplot**

# In[60]:


plt.figure(figsize=(12,6))
sns.violinplot(x='parental level of education',y='math score',data=df)


# In[61]:


plt.figure(figsize=(12,6))
sns.violinplot(x='parental level of education',y='math score',data=df,hue='gender',split=True)


# In[63]:


plt.figure(figsize=(12,6))
sns.violinplot(x='parental level of education',y='math score',data=df,inner=None)


# In[65]:


plt.figure(figsize=(12,6))
sns.violinplot(x='parental level of education',y='math score',data=df,inner='quartile')


# **swarmplot**

# In[ ]:




