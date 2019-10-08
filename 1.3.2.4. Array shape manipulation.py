#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
#flattening
a = np.array([[1, 2, 3], [4, 5, 6]])
a.ravel()


# In[2]:


a.T


# In[3]:


a.T.ravel()


# In[5]:


#reshaping
a.shape


# In[6]:


b = a.ravel()
b = b.reshape((2, 3))
b


# In[7]:


a.reshape((2, -1))


# In[10]:


z = np.array([1, 2, 3])
z


# In[11]:


z[:, np.newaxis]


# In[12]:


z[np.newaxis, :]


# In[13]:


#dimension sguffling
a = np.arange(4*3*2).reshape(4, 3, 2)
a.shape


# In[14]:


a[0, 2, 1]


# In[15]:


b = a.transpose(1, 2, 0)
b.shape


# In[16]:


b[2, 1, 0]


# In[17]:


b[2, 1, 0] = -1
a[0, 2, 1]


# In[18]:


#resizing
a = np.arange(4)
a.resize((8,))
a


# In[20]:


b = a
a.resize((4,1)) 


# In[ ]:




