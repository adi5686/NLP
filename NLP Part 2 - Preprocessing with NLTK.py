#!/usr/bin/env python
# coding: utf-8

# # Preprocessing with NLTK - Tokenization and Stopwords

# In[1]:



import nltk.tokenize


# In[3]:


# dfining a variable with sample data
text = '''It was a fairy-tale moment in 1985 when John Travolta, 
one of the biggest Hollywood stars of the time, danced with a real-life princess in the White House. 
Photos of Princess Diana dancing with John Travolta have gone down in the pop culture hall of fame as iconic. 
The two took to the dance floor at the White House during a dinner hosted in honour of Prince Charles and Princess Diana on November 9, 1985. 
In the years since, the Saturday Night Fever star has spoken about the moment often in interviews, 
once referring to it as "one of the highlights of my life'''


# In[16]:


# tokenize the text at sentence level
tokenized_text = nltk.tokenize.sent_tokenize(text)


# In[17]:


print(tokenized_text)


# In[19]:


len(tokenized_text)


# In[20]:


tokenized_text[0]


# In[21]:


# tokenizing the text at word level
tokenized_text_word = nltk.tokenize.word_tokenize(text)


# In[22]:


print(tokenized_text_word)


# In[23]:


len(tokenized_text_word)


# In[24]:


len(text)


# In[30]:


# checking frequency distribution
fdist = nltk.probability.FreqDist(tokenized_text)
print(fdist)


# In[32]:


fdist.most_common(2)


# In[33]:


fdist = nltk.probability.FreqDist(tokenized_text_word)
print(fdist)


# In[34]:


fdist.most_common(5)


# In[35]:


fdist.plot(20,cumulative = True)


# # Stopwords

# Words which are considered as noise, and generally have no contribution in drawing inferences or making analysis

# In[36]:


from nltk.corpus import stopwords


# In[37]:


stopwords.words('english')


# In[38]:


len(stopwords.words('english'))


# In[40]:


stop_words = stopwords.words("english")


# In[49]:


filtered_text = []


# In[50]:


for word in tokenized_text_word:
    if word not in stop_words:
        filtered_text.append(word)


# In[51]:


print(len(filtered_text))


# In[52]:


print(len(tokenized_text_word))


# In[53]:


filtered_text


# In[ ]:




