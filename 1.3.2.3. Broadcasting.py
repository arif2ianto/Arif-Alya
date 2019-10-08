#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
a = np.tile(np.arange(0, 40, 10), (3, 1)).T
a


# In[3]:


b = np.array([0, 1, 2])
a + b


# In[4]:


a = np.ones((4, 5))
a[0] = 2  # we assign an array of dimension 0 to an array of dimension 1
a


# In[5]:


a = np.arange(0, 40, 10)
a.shape


# In[6]:


a = a[:, np.newaxis]  # adds a new axis -> 2D array
a.shape


# In[7]:


a


# In[8]:


a+b


# In[9]:


#worked example : broadcasting


# In[10]:


mileposts = np.array([0, 198, 303, 736, 871, 1175, 1475, 1544,
       1913, 2448])
distance_array = np.abs(mileposts - mileposts[:, np.newaxis])
distance_array


# In[11]:


x, y = np.arange(5), np.arange(5)[:, np.newaxis]
distance = np.sqrt(x ** 2 + y ** 2)
distance


# In[20]:


#in color
import matplotlib.pyplot as plt
plt.pcolor(distance)    
plt.colorbar() 


# In[14]:


x, y = np.ogrid[0:5, 0:5]
x, y


# In[15]:


x.shape, y.shape


# In[18]:


distance = np.sqrt(x ** 2 + y ** 2)
x, y = np.mgrid[0:4, 0:4]
x


# In[19]:


y


# In[ ]:




