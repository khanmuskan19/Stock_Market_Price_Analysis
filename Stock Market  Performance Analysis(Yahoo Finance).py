#!/usr/bin/env python
# coding: utf-8

# In[1]:


# !pip install yfinance


# In[2]:


import pandas as pd
import yfinance as yf
from datetime import datetime


# In[3]:


start_date=datetime.now()-pd.DateOffset(months=3)
end_date=datetime.now()


# In[4]:


tickers=['AAPL','MSFT', 'NFLX','GOOG',]
df_list=[]


# In[5]:


for ticker in tickers:
    data=yf.download(ticker,start=start_date,end=end_date)
    df_list.append(data)


# In[6]:


df=pd.concat(df_list,keys=tickers,names=['Ticker','Date'])
print(df.head())


# In[7]:


df=df.reset_index()
print(df.head)


# In[8]:


import plotly.express as px
fig=px.line(df,x='Date',y='Close',color='Ticker',title='Stock Market Performance for the Last 3 Months')
fig.show()


# In[9]:


fig=px.area(df,x="Date", y='Close',color='Ticker',facet_col='Ticker',labels={'Date':'Date','Close':'Closing Price','Ticker':'Company'},title='Stock Prices for Apple, Microsoft, Netflix, and Google')
fig.show()


# In[10]:


df['MA10']=df.groupby('Ticker')['Close'].rolling(window=10).mean().reset_index(0,drop=True)
df['MA20']=df.groupby('Ticker')['Close'].rolling(window=10).mean().reset_index(0,drop=True)
for ticker, group in df.groupby('Ticker'):
    print(f'Moving Averages for {ticker}')
    print(group[['MA10','MA20']])


# In[11]:


for ticker, group in df.groupby('Ticker'):
    fig=px.line(group,x='Date',y=['Close','MA10','MA20'],title=f"{ticker} Moving Averages")
    fig.show()


# In[12]:


df['Volatility']=df.groupby('Ticker')['Close'].pct_change().rolling(window=10).std().reset_index(0,drop=True)
fig=px.line(df,x='Date',y="Volatility",color='Ticker',title='Volatility of All Companies')
fig.show()


# In[13]:


apple=df.loc[df["Ticker"]=='AAPL',['Date','Close']].rename(columns={'Close':'AAPL'})
microsoft=df.loc[df["Ticker"]=='MSFT',['Date','Close']].rename(columns={'Close':'MSFT'})
df_corr=pd.merge(apple,microsoft,on='Date')
fig=px.scatter(df_corr,x="AAPL",y='MSFT',trendline='ols',title='Correlation between Apple & Microsoft')
fig.show()


# In[ ]:





# In[ ]:




