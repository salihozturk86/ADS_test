#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from pandas import Series
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings


# In[2]:


data = pd.read_csv('data_kpi_forecasting_new.csv')


# In[3]:


data_original = data.copy()


# In[4]:


data.columns


# In[5]:


data.dtypes


# In[6]:


data.shape


# In[17]:


data['time'] = pd.to_datetime(data.time,format='%m/%d/%Y %H:%M')


# In[24]:


data['day_of_week'] = data['time'].dt.dayofweek


# In[27]:


data.tail()


# In[33]:


temp  = data['time']


# In[35]:


def applyer(row):
    if row.dayofweek == 5 or row.dayofweek == 6:
        return 1
    else:
        return 0
temp2 = data['time'].apply(applyer)
data['weekend'] = temp2


# In[37]:





# In[38]:


data.index = data['time']
plt.figure(figsize=(16,8))
plt.plot(data['kpi'],label='KPI_Value')
plt.xlabel("Time")
plt.ylabel("KPI")
plt.legend(loc='best')


# In[42]:


data['Hour'] = data['time'].dt.hour


# In[46]:


data.groupby('Hour')['kpi'].mean().plot.bar()


# In[47]:


data.groupby('weekend')['kpi'].mean().plot.bar()


# In[48]:


data.groupby('day_of_week')['kpi'].mean().plot.bar()


# In[ ]:




