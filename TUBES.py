#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv("Salesforce_stock_history.csv")
df.head()


# In[3]:


import plotly.graph_objects as go

fig = go.Figure(data=go.Scatter(x=df['Date'] ,y=df['Close'], mode='lines'))
fig.show()


# In[4]:


from plotly.subplots import make_subplots

fig = make_subplots(specs=[[{"secondary_y": True}]])
fig.add_trace(go.Scatter(x=df['Date'],y=df['Close'],name='Price'),secondary_y=False)
fig.add_trace(go.Bar(x=df['Date'],y=df['Volume'],name='Volume'),secondary_y=True)
fig.show()


# In[5]:


fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])])
fig.update_layout(title={'text':'Salesforce', 'x':0.5})

fig.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




