#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
a = np.array([1, 2, 3, 4])
a + 1


# In[3]:


2**a


# In[4]:


b = np.ones(4) + 1
a - b


# In[5]:


a*b


# In[7]:


j = np.arange(5)
2**(j + 1) - j


# In[8]:


a = np.arange(10000)
get_ipython().run_line_magic('timeit', 'a + 1')


# In[9]:


l = range(10000)
get_ipython().run_line_magic('timeit', '[i+1 for i in l]')


# In[10]:


c = np.ones((3, 3))
c * c   #bukan matriks multiplication


# In[11]:


c.dot(c)


# In[12]:


[2**0, 2**1, 2**2, 2**3, 2**4]


# In[15]:


a = np.array([1, 2, 3, 4])
b = np.array([4, 2, 2, 4])
a == b


# In[16]:


a > b


# In[17]:


a = np.array([1, 1, 0, 0], dtype=bool)
b = np.array([1, 0, 1, 0], dtype=bool)
np.logical_or(a, b)


# In[18]:


np.logical_and(a, b)


# In[19]:


a = np.arange(5)
np.sin(a)


# In[20]:


np.log(a)


# In[21]:


np.exp(a)


# In[25]:


a = np.arange (4)
a + np.array([1, 2]) 


# In[26]:


a = np.triu(np.ones((3, 3)), 1)   # see help(np.triu)
a


# In[27]:


a.T


# In[29]:





# In[ ]:




