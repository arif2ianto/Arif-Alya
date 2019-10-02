#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd


# In[5]:


pd.read_csv('zoo.csv', delimiter = ',')


# In[10]:


get_ipython().system('wget 46.101.230.157/dilan/pandas_tutorial_read.csv')


# In[11]:


pd.read_csv('pandas_tutorial_read.csv', delimiter=';')


# In[12]:


pd.read_csv('pandas_tutorial_read.csv', delimiter=';', names = ['my_datetime', 'event', 'country', 'user_id', 'source', 'topic'])


# In[13]:


article_read = pd.read_csv('pandas_tutorial_read.csv', delimiter=';', names = ['my_datetime', 'event', 'country', 'user_id', 'source', 'topic'])


# In[14]:


article_read


# In[15]:


article_read.head()


# In[16]:


article_read.tail()


# In[17]:


article_read.sample(5)


# In[18]:


article_read[['country', 'user_id']]


# In[19]:


article_read[['user_id', 'country']]


# In[20]:


article_read.user_id


# In[21]:


article_read['user_id']


# In[24]:


article_read.source == 'SEO'


# In[25]:


article_read[article_read.source == 'SEO']


# In[26]:


article_read.head()[['country', 'user_id']]


# In[27]:


article_read[['country', 'user_id']].head()


# In[28]:


pd.read_csv('pandas_tutorial_read.csv', delimiter=';', names = ['my_datetime', 'event', 'country', 'user_id', 'source', 'topic'])[['country', 'user_id']].head()


# In[29]:


article_read[article_read.country == 'country_2'][['user_id','topic', 'country']].head()


# In[30]:


ar_filtered = article_read[article_read.country == 'country_2']
ar_filtered_cols = ar_filtered[['user_id','topic', 'country']]
ar_filtered_cols.head()


# In[ ]:




