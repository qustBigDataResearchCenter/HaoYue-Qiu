
# coding: utf-8

# In[11]:


str='X-DSPAM-Confidence: 0.8475'
ipos=str.find(':')     #找到冒号
#print(ipos)
piece1=str[ipos+1:]
#print(piece1)
value1=float(piece1)     #piece是一个string
print(value1)
#print(value1+40.0)

#piece2=str[ipos+2:]      #空格不影响结果
#print(piece2)
#value2=float(piece2)
#print(value2)
#print(value2+40.0)


# In[18]:


stuff='Hello\nWorld!'
stuff


# In[19]:


print(stuff)


# In[20]:


stuff='X\nY'
print(stuff)
len(stuff)       #stuff中有3个字符X,\n,Y索引分别为0,1,2


# In[23]:


fhand=open('mbox-short.txt')
count=0
for line in fhand:
    count=count+1
print('Line Count:',count)


# In[ ]:




