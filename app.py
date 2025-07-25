import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

st.set_page_config('Year Sales', 
                   page_icon='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%2Fid%2FOIP.DLSmFifnKFAC080fPx7MIgHaFP%3Fpid%3DApi&f=1&ipt=e2cc9abb3e6718eea922e80ab76bade6d86ac0c9102d96306bd2b1e01496d176&ipo=images',
                   layout='wide',
                   initial_sidebar_state='expanded',)
df=pd.read_excel('sales_data.xlsx')

#side bar
st.sidebar.header('Sales DashBoard')
st.sidebar.image('https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%2Fid%2FOIP.fw-DmCXGgaFSWhA8iYjEaAHaEK%3Fpid%3DApi&f=1&ipt=b713cd9cfe47e0bb0c882be8c6e2bb2091f89c39e38a17156786dd34629ffb15&ipo=images')
st.sidebar.write('This Dashboard for showing the analysis of sales tables')

st.sidebar.write("")
st.sidebar.markdown('Made with Eng. [AMR AHMED]')
#st.write(df) 
cat_filter=st.sidebar.selectbox(' categorical filtering',[None,'Region','Product Category','Product Sub_Category'])
Num_filter=st.sidebar.selectbox('Numerical Filtering',[None, 'Order Quantity','Profit','Sales','Order ID'])
row_filter=st.sidebar.selectbox(' Row filtering',[None,'Region','Product Category','Product Sub_Category'])
column_filter=st.sidebar.selectbox('Column Filtering',[None, 'Order Quantity','Profit','Sales','Order ID'])


#body
# row a
a1,a2,a3,a4=st.columns(4)
a1.metric("Max of Sales", df['Sales'].max())
a2.metric('Min of Sales', df['Sales'].min())
a3.metric('Max of profit', df['Profit'].max())
a4.metric('Min of profit', df['Profit'].min())

#ROW b
st.subheader('Profit of sales vs Region ')
fig=px.scatter(data_frame=df,
               x='Region',
               y='Profit',
               color=cat_filter,
               size=Num_filter,
               facet_col=column_filter,
               facet_row=row_filter)
st.plotly_chart(fig,use_container_width=True) #for making figure more flexiable upon the size of the screen 
#

#Row C
c1,c2,c3=st.columns((3,3,4))
with c1:
    st.text('Profit vs Region')
    fig=px.bar(data_frame=df,x='Region',
               y='Profit',color=cat_filter
               )
    st.plotly_chart(fig,use_container_width=True)
    
with c2:
    st.text('Profit vs Categorical')
    fig=px.pie(data_frame=df,values='Profit',
               names='Product Category',
               color=cat_filter)
    st.plotly_chart(fig,use_container_width=True)

with c3:
    st.text('Sales vs Sub-Categorical')
    fig=px.pie(data_frame=df,values='Profit',names='Product Sub-Category',
               color=cat_filter,
                
                hole=0.4)
    st.plotly_chart(fig,use_container_width=True)
