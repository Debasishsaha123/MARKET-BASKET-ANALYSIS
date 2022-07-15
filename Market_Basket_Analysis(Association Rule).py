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


# # Apriori and association algorithm implementation

# In[27]:


frequent_itemsets=apriori(dataset,min_support=0.01,use_colnames=True) #to generate itemset
frequent_itemsets['length']=frequent_itemsets['itemsets'].apply(lambda x:len(x))
frequent_itemsets


# In[54]:


frequent_itemsets[(frequent_itemsets['length']==2 )& (frequent_itemsets['support']>=0.05)]


# In[55]:


frequent_itemsets[(frequent_itemsets['length']==3 )].head()


# Now,we will use the extracted frequent itemsets in rule creation

# In[56]:


rules=association_rules(frequent_itemsets,metric='lift',min_threshold=1.2)
rules['antecedents_length']=rules['antecedents'].apply(lambda x:len(x))
rules['consequents_length']=rules['consequents'].apply(lambda x:len(x))
rules.sort_values('lift',ascending=False)


# According the above table we can easily say that the dependency between (herb & pepper) and (ground beef) is high since lift value is approximately 2.5x of threshold value and conviction is higher than 1

# In[58]:


#sort values based on their confidence
rules.sort_values('confidence',ascending=False)


# now see the confidence matrix without mineral water

# In[60]:


rules[~rules['consequents'].str.contains('mineral water',regex=False) &
     ~rules['antecedents'].str.contains('mineral water',regex=False)].sort_values('confidence',ascending=False)


# # According the redifined table there is a significant relationship between ground beef and spaghetti ,red wine,olive oli

# In[ ]:





# In[68]:


from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
sns.set(style = "whitegrid")
fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(projection = '3d')


x = rules['support']
y = rules['confidence']
z = rules['lift']

ax.set_xlabel("Support")
ax.set_ylabel("Confidence")
ax.set_zlabel("Lift")

ax.scatter(x, y, z)
ax.set_title("3D Distribution of Association Rules")

plt.show()


# In[69]:


spaghetti_rules = rules[rules['consequents'].astype(str).str.contains('spaghetti')]
spaghetti_rules = spaghetti_rules.sort_values(by=['lift'],ascending = [False]).reset_index(drop = True)

display(spaghetti_rules.head())


# In[ ]:




