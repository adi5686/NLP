#!/usr/bin/env python
# coding: utf-8

# # NLP Part 1 - Downloading NLTK

# In[54]:


# importing NLTK
import nltk


# In[4]:


# Downloading and installing NLTK
nltk.download()


# In[5]:


# importing inbulit corpus from NLTK
from nltk.book import *


# In[6]:


sents()


# In[7]:


sent2


# In[11]:


text1


# In[12]:


# importing another corous from NLTK
from nltk.corpus import brown


# In[13]:


brown.categories()


# In[14]:


brown.words(categories = 'adventure')


# In[16]:


from nltk.corpus import webtext


# In[19]:


for f in webtext.fileids():
    print(f)


# In[25]:


webtext.fileids()


# In[29]:


webtext.raw('firefox.txt')


# In[31]:


from nltk.corpus import inaugural


# In[33]:


inaugural.fileids()


# In[34]:


inaugural.raw('2017-Trump.txt')


# In[48]:


from nltk.corpus import genesis


# In[49]:


genesis.fileids()


# In[57]:


genesis.raw('english-web.txt')


# In[60]:


text_split = genesis.raw('english-web.txt').split()


# In[61]:


abstracts = nltk.Text(text_split)


# In[64]:


abstracts.concordance('god')


# In[ ]:





# In[72]:


freq_dist = FreqDist(text_split)


# In[73]:


print(freq_dist)


# In[74]:


freq_dist


# In[75]:


freq_dist.most_common(10)


# In[78]:


freq_dist.plot(10, cumulative = True)


# In[77]:


freq_dist.plot(40, cumulative = False)


# In[ ]:


from nltk

