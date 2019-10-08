#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
x = np.array([1, 2, 3, 4])
np.sum(x)


# In[3]:


x.sum()


# In[4]:


x = np.array([[1, 1], [2, 2]])
x


# In[5]:


x.sum(axis=0)


# In[6]:


x[:, 0].sum(), x[:, 1].sum()


# In[7]:


x.sum(axis=1)


# In[8]:


x[0, :].sum(), x[1, :].sum()


# In[13]:


x=np.random.rand(2,2,2)
x.sum(axis=2) [0,1]


# In[14]:


x[0,1,:].sum()


# In[15]:


x = np.array([1, 3, 2])
x.min()


# In[16]:


x.max()


# In[17]:


x.argmin()


# In[18]:


x.argmax()


# In[19]:


np.all([True, True, False])


# In[20]:


np.any([True, True, False])


# In[22]:


a = np.zeros((100, 100))
np.any(a != 0)


# In[23]:


np.all(a != 0)


# In[24]:


a = np.array([1, 2, 3, 2])
b = np.array([2, 2, 3, 2])
c = np.array([6, 4, 4, 5])
((a <= b) & (b <= c)).all()


# In[25]:


x = np.array([1, 2, 3, 1])
y = np.array([[1, 2, 3], [5, 6, 1]])
x.mean()


# In[26]:


np.median(x)


# In[27]:


np.median(y, axis=-1)


# In[28]:


x.std()     


# In[33]:


#worked example : data statistics


# In[62]:


data = np.loadtxt(fname ="populations.txt")
year, hares, lynxes, carrots = data.T


# In[63]:


from matplotlib import pyplot as plt
plt.axes([0.2, 0.1, 0.5, 0.8]) 
plt.plot(year, hares, year, lynxes, year, carrots) 
plt.legend(('Hare', 'Lynx', 'Carrot'), loc=(1.05, 0.5)) 


# In[64]:


populations = data[:, 1:]
populations.mean(axis=0)


# In[66]:


populations.std(axis=0)


# In[67]:


np.argmax(populations, axis=1)


# In[36]:


#worked example : data statistics


# In[37]:


n_stories = 1000 
t_max = 200 


# In[40]:


t = np.arange(t_max)
steps = 2 * np.random.randint(0, 1 + 1, (n_stories, t_max))-1


# In[41]:


np.unique(steps)


# In[42]:


positions = np.cumsum(steps, axis=1) # axis = 1: dimension of time
sq_distance = positions**2


# In[43]:


mean_sq_distance = np.mean(sq_distance, axis=0)


# In[53]:


import matplotlib.pyplot as plt
plt.figure(figsize=(4, 3)) 
plt.plot(t, np.sqrt(mean_sq_distance), 'g.', t, np.sqrt(t), 'y-') 
plt.xlabel(r"$t$") 
plt.ylabel(r"$\sqrt{\langle (\delta x)^2 \rangle}$") 
plt.tight_layout() # provide sufficient space for labels
plt.show()


# In[ ]:




