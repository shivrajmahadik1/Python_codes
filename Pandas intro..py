#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


pd.__version__


# In[5]:


pd.DataFrame    #pd. tab button for documention


# In[6]:


# index  series + series = DataFrame


# In[9]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[11]:


a=('Name',1,2,3,4)
se= pd.Series(a)
se


# In[12]:


li= list(range(10,20))
se1=pd.Series(li)
se1


# ### Pandas series object

# In[13]:


data= pd.Series([0.25,0.5,0.75,1.0])  #1-D array object
data


# In[14]:


data.values


# In[15]:


data.index


# In[18]:


data[1]


# In[19]:


data[1:3]


# In[20]:


data.describe


# In[21]:


data.head    #top five element


# In[22]:


data.tail    # last of 5 element


# In[23]:


data.head(2)


# In[25]:


data.tail(2)


# In[27]:


data.mean()


# In[28]:


data.ndim


# In[29]:


data.shape


# In[31]:


data.size


# In[32]:


data.plot()


# In[ ]:




