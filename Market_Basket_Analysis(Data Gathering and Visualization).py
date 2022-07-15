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


# In[5]:


data.shape[0]


# In[6]:


data.describe()


# In[7]:


data.shape[1]


# # Data visualizations

# In[8]:


#gather all data values into numpy array
transaction=[]
for i in range(0,data.shape[0]):
    for j in range(0,data.shape[1]):
        transaction.append(data.values[i,j])
transaction=np.array(transaction)
#converts them into a pandas dataframe
df=pd.DataFrame(transaction,columns=['items'])
df["incident_count"]=1 #put 1 to each item for marketing countable Table

#Delete nan items to datasets
indexNames=df[df['items']=="nan"].index
df.drop(indexNames,inplace=True)

df_table=df.groupby('items').sum().sort_values("incident_count",ascending=False).reset_index()
df_table.style.background_gradient(cmap='Blues')


# ## Customer's first choice

# In[9]:


#gather only fisrt choice of Each transaction into numpy array
transaction=[]
for i in range(0,data.shape[0]):
    transaction.append(data.values[i,0])
transaction=np.array(transaction)
#converts them into a pandas dataframe
df_first=pd.DataFrame(transaction,columns=['items'])
df_first["incident_count"]=1 #put 1 to each item for marketing countable Table

#Delete nan items to datasets
indexNames=df_first[df_first['items']=="nan"].index
df_first.drop(indexNames,inplace=True)

df_table_first=df_first.groupby('items').sum().sort_values("incident_count",ascending=False).reset_index()
df_table_first['food']='food'
#df_table_first.head(15).style.background_gradient(cmap='Blues')
df_table_first=df_table_first.truncate(before = -1 ,after=15)  #first 15 values


# In[10]:


df_table_first


# In[11]:


#network graph using networkx
import warnings
warnings.filterwarnings('ignore')
plt.rcParams['figure.figsize']=(20,20)
first_choice=nx.from_pandas_edgelist(df_table_first,source='food',target='items',edge_attr=True) #edge_attr=True means in the graph weights also included
pos=nx.spring_layout(first_choice) #for Positioning nodes 
nx.draw_networkx_nodes(first_choice,pos,node_size=10000,node_color='lavender') #Draw the nodes of the graph
nx.draw_networkx_edges(first_choice,pos,width=3,alpha=0.6,edge_color='red') #Draw the edges of the graph 
nx.draw_networkx_labels(first_choice,pos,font_size=10,font_family='sans-serif') #Draw node labels on the graph
plt.axis('off')
plt.grid()
plt.title('Top 15 first choice',fontsize=25)
plt.show()


# In[12]:


fig=go.Figure(data=[go.Bar(x=df_table_first['items'],y=df_table_first['incident_count'],
                  hovertext=df_table_first['items'],text=df_table_first['incident_count'])])
fig.update_traces(marker_color='rgb(0,0,225)',marker_line_color='rgb(8,48,107)',marker_line_width=1.5,opacity=0.7)
fig.update_layout(title_text="Customer's first choice",template='plotly_white')
fig.show()


# ## Customer's second choice

# In[13]:


#gather only second choice of Each transaction into numpy array
transaction=[]
for i in range(0,data.shape[0]):
    transaction.append(data.values[i,1])
transaction=np.array(transaction)
#converts them into a pandas dataframe
df_second=pd.DataFrame(transaction,columns=['items'])
df_second["incident_count"]=1 #put 1 to each item for marketing countable Table

#Delete nan items to datasets
indexNames=df_second[df_second['items']=="nan"].index
df_second.drop(indexNames,inplace=True)

df_table_second=df_second.groupby('items').sum().sort_values("incident_count",ascending=False).reset_index()
df_table_second['food']='food'
#df_table_first.head(15).style.background_gradient(cmap='Blues')
df_table_second=df_table_second.truncate(before = -1 ,after=15)  #first 15 values


# In[14]:


df_table_second


# In[15]:


#network graph using networkx
import warnings
warnings.filterwarnings('ignore')
plt.rcParams['figure.figsize']=(20,20)
second_choice=nx.from_pandas_edgelist(df_table_second,source='food',target='items',edge_attr=True) #edge_attr=True means in the graph weights also included
pos=nx.spring_layout(second_choice) #for Positioning nodes 
nx.draw_networkx_nodes(second_choice,pos,node_size=10000,node_color='honeydew') #Draw the nodes of the graph
nx.draw_networkx_edges(second_choice,pos,width=3,alpha=0.6,edge_color='red') #Draw the edges of the graph 
nx.draw_networkx_labels(second_choice,pos,font_size=10,font_family='sans-serif') #Draw node labels on the graph
plt.axis('off')
plt.grid()
plt.title('Top 15 second choice',fontsize=25)
plt.show()


# In[16]:


fig=go.Figure(data=[go.Bar(x=df_table_second['items'],y=df_table_second['incident_count'],
                  hovertext=df_table_second['items'],text=df_table_second['incident_count'])])
fig.update_traces(marker_color='rgb(255,0,0)',marker_line_color='rgb(8,48,107)',marker_line_width=1.5,opacity=0.7)
fig.update_layout(title_text="Customer's second choice",template='ggplot2')
fig.show()


# ## Customer's third choice

# In[17]:


#gather only third choice of Each transaction into numpy array
transaction=[]
for i in range(0,data.shape[0]):
    transaction.append(data.values[i,2])
transaction=np.array(transaction)
#converts them into a pandas dataframe
df_third=pd.DataFrame(transaction,columns=['items'])
df_third["incident_count"]=1 #put 1 to each item for marketing countable Table

#Delete nan items to datasets
indexNames=df_third[df_third['items']=="nan"].index
df_third.drop(indexNames,inplace=True)

df_table_third=df_third.groupby('items').sum().sort_values("incident_count",ascending=False).reset_index()
df_table_third['food']='food'
#df_table_first.head(15).style.background_gradient(cmap='Blues')
df_table_third=df_table_third.truncate(before = -1 ,after=15)  #first 15 values


# In[18]:


df_table_third


# In[19]:


fig=go.Figure(data=[go.Bar(x=df_table_third['items'],y=df_table_third['incident_count'],
                  hovertext=df_table_third['items'],text=df_table_third['incident_count'])])
fig.update_traces(marker_color='rgb(158,202,225)',marker_line_color='rgb(8,48,107)',marker_line_width=1.5,opacity=0.7)
fig.update_layout(title_text="Customer's third choice",template='plotly_dark')
fig.show()

