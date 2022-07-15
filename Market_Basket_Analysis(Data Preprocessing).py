#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import networkx as nx
import matplotlib.pyplot as plt


# In[2]:


from mlxtend.preprocessing import TransactionEncoder  # return true false values for the data values by checking its presence in the row 

from mlxtend.frequent_patterns import apriori,association_rules  #for support,confidence,lift metric


# In[3]:


data=pd.read_csv('Market_Basket_Optimisation.csv',header=None)


# In[4]:


data.head()


# In[8]:


data.shape[0]


# In[9]:


data.describe()


# In[10]:


data.shape[1]


# ## Data preprocessing

# In[21]:


#transform every transform to separatelist and gather them into a numpy array
transaction=[]
for i in range(data.shape[0]):
    transaction.append([str(data.values[i,j]) for j in range (data.shape[1])])
transaction=np.array(transaction)
transaction


# In[22]:


te=TransactionEncoder()
te_ary=te.fit(transaction).transform(transaction)
dataset=pd.DataFrame(te_ary,columns=te.columns_)
dataset

#items as a column
#transaction will become row


# In[23]:


dataset.shape


# In[24]:


first50=df_table['items'].head(50).values  #select top 50
dataset=dataset.loc[:,first50] #extract top50
dataset


# In[25]:


dataset.columns


# In[26]:


def encode_units(x):
    if x==True:
        return 1
    if x==False:
        return 0
dataset=dataset.applymap(encode_units) #Apply a function to a Dataframe elementwise
dataset

