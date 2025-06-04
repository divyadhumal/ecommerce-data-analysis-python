#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd

import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio #graph template execute
import plotly.colors as colors
pio.templates.default="plotly_white"#theme is white


# In[7]:


data=pd.read_csv("Sample - Superstore.csv",encoding='latin-1')


# In[9]:


data.describe()


# In[10]:


data.info()


# Converting date format

# In[14]:


data['Order Date']= pd.to_datetime(data['Order Date'])
data['Ship Date']= pd.to_datetime(data['Ship Date'])


# In[15]:


data.info()


# In[39]:


data['Order Month'] =data['Order Date'].dt.month
data['Order Year'] =data['Order Date'].dt.year
data['Order Day of Week'] =data['Order Date'].dt.dayofweek


# In[40]:


data.head()


# #Monthly sales anaylsis

# In[41]:


sales_by_month = data.groupby('Order Month')['Sales'].sum().reset_index()
 


# In[42]:


sales_by_month


# In[43]:


fig = px.line(sales_by_month,
                x='Order Month',
                y='Sales',
                title='Monthly Sales Analysis')
fig.show()


# In[44]:


data.head()


# #Sales by category

# In[45]:


sales_by_category = data.groupby('Category')['Sales'].sum().reset_index()


# In[46]:


sales_by_category


# In[48]:


fig= px.pie(sales_by_category, #type of fig
            values ='Sales',
            names ='Category',
            hole =0.3,
            color_discrete_sequence =px.colors.qualitative.Pastel)#individual different color

fig.update_traces(textposition='inside', textinfo='percent+label')
fig.update_layout(title_text ='Sales Analysis by Category', title_font=dict(size=24))

fig.show()


# #Sales anaylsis by sub category

# In[49]:


data.head()


# In[50]:


sales_by_subcategory = data.groupby('Sub-Category')['Sales'].sum().reset_index()


# In[51]:


sales_by_subcategory


# In[54]:


fig = px.bar(sales_by_subcategory, x='Sub-Category', y='Sales', title= 'Sales analysis by sub category')

fig.show()
                    


# #Monthly Profit analysis

# In[55]:


data.head()


# In[58]:


profit_by_month = data.groupby('Order Month')['Profit'].sum().reset_index()


# In[59]:


profit_by_month


# In[68]:


fig = px.bar(profit_by_month, x='Order Month', y='Profit', title='Monthly Profit Analysis')
fig.show()


# #Profit by category

# In[70]:


data.head()


# In[72]:


profit_by_category = data.groupby('Category')['Profit'].sum().reset_index()


# In[73]:


profit_by_category


# In[75]:


fig = px.pie(profit_by_category, values='Profit', names='Category', hole=0.4, title='Profit by Category Analysis')

fig.show()


# #Profit by subcategory

# In[76]:


profit_by_subcategory = data.groupby('Sub-Category')['Profit'].sum().reset_index()


# In[77]:


profit_by_subcategory


# In[80]:


fig = px.line(profit_by_subcategory, x='Sub-Category', y='Profit', title= 'Profit Analysis by Sub-Category')

fig.show()


# #sales and profit - customer segment

# In[81]:


data.head(3)


# In[85]:


sales_profit_by_segment =data.groupby('Segment').agg({'Sales':'sum', 'Profit':'sum'}).reset_index()

color_palette = colors.qualitative.Pastel

fig= go.Figure()
fig.add_trace(go.Bar(x = sales_profit_by_segment['Segment'],
                     y= sales_profit_by_segment['Sales'],
                     name = 'Sales',
                     marker_color =color_palette[0]))

fig.add_trace(go.Bar(x=sales_profit_by_segment['Segment'],
                     y=sales_profit_by_segment['Profit'],
                     name='Profit',
                     marker_color = color_palette[1]))

fig.update_layout(title='Sales and Profit Analysis by Customer Segment',
                  xaxis_title ='Customer Segment', yaxis_title='Amount')

fig.show()


# #Sales to profit ratio

# In[87]:


sales_profit_by_segment = data.groupby('Segment').agg({'Sales':'sum', 'Profit':'sum'}).reset_index()

sales_profit_by_segment['Sales_to_profit_Ratio'] = sales_profit_by_segment['Sales'] / sales_profit_by_segment['Profit']

print(sales_profit_by_segment[['Segment','Sales_to_profit_Ratio']])


# In[88]:


fig =px.pie(sales_profit_by_segment, values= 'Sales_to_profit_Ratio',  names='Segment', title=' Sales to Profit Analysis')

fig.show()


# In[ ]:




