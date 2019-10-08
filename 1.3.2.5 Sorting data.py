#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
a = np.array([[4, 3, 5], [1, 2, 1]])
b = np.sort(a, axis=1)
b


# In[2]:


a.sort(axis=1)
a


# In[3]:


a = np.array([4, 3, 1, 2])
j = np.argsort(a)
j


# In[4]:


a[j]


# In[5]:


a = np.array([4, 3, 1, 2])
j_max = np.argmax(a)
j_min = np.argmin(a)
j_max, j_min


# In[ ]:




