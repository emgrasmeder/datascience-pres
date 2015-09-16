
# coding: utf-8

# In[4]:

from nltk.tokenize import sent_tokenize


# In[6]:

sent_tokenize("Hello Women Who Code Python! You are all wonderful.")


# In[9]:

from nltk.tokenize import word_tokenize


# In[11]:

word_tokenize("A woman a plan a canal panamowa")


# In[13]:

from nltk.tag import pos_tag # pos = parts of speech


# In[21]:

words = word_tokenize("Python has several science friendly packages")
pos_tag(words)


# In[49]:

from nltk.corpus import genesis, stopwords
from nltk.collocations import BigramCollocationFinder
from nltk.util import ngrams


# In[50]:

stopwords.words("english")


# In[47]:

[g 
 for g in ngrams(genesis.words('english-web.txt'), 2) 
 if not any(
        [w in stopwords.words("english") 
         for w in g])]


# In[ ]:



