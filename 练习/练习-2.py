



# In[2]:


stuff='hello world'
type(stuff)
dir(stuff)


# In[5]:


greet='   hello bob   '
greet.lstrip()


# In[6]:


greet.rstrip()


# In[7]:


greet.strip()


# In[20]:


line='Please have a nice day'
line.startswith('Please')


# In[14]:


line.startswith('have')


# In[16]:


line.startswith('P')


# In[21]:


line.startswith('Please have a')


# In[16]:


data='Form stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos=data.find('@')
print(atpos)


# In[17]:


sppos=data.find(' ',atpos)
print(sppos)


# In[18]:


nppos=data.find(' ')
print(nppos)


# In[19]:


host=data[atpos+1 : sppos]
print(host)


# In[20]:


data='Form stephen.marquard@0l Sat Jan  5 09:14:16 2008'
kppos=data.find('f')
print(kppos)


# In[21]:


a='nnnnnnnnnnn'
b=a.replace('n','x')
print(b)


# In[22]:


x='爬虫'
type(x)


# In[23]:


x=u'爬虫'
type(x)    #python3中所有的string都是Unicode


# In[ ]:




