import streamlit as st
import yfinance as yf
import datetime
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
import datetime
import pytz
import requests

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)


import datetime
import pytz
while True:
    india_timezone = pytz.timezone('Asia/Kolkata')
    india_time = datetime.datetime.now(india_timezone)
    st.write("The current time in India is:", india_time.strftime("%Y-%m-%d %H:%M:%S"))
    india_timezone = pytz.timezone('Australia/Sydney')
    india_time = datetime.datetime.now(india_timezone)
    st.write("The current time in India is:", india_time.strftime("%Y-%m-%d %H:%M:%S"))


def get_falling_stocks(asx_stocks):
    falling_stocks = []
    for stock in asx_stocks:
        stock_data = yf.Ticker(stock + ".AX").history(period="5d")
        if (stock_data["Close"][1] < stock_data["Close"][0]):
          if (stock_data["Close"][2] < stock_data["Close"][1]):
            if (stock_data["Close"][3] < stock_data["Close"][2]):
              if (stock_data["Close"][4] < stock_data["Close"][3]):    
                st.write('yes')
                falling_stocks.append(stock)
    return falling_stocks


asx_20_stocks = ['AGVT', 'LNAS']
falling_stocks = get_falling_stocks(asx_20_stocks)
st.write(falling_stocks)




def chart(stock):
    stock_data = yf.Ticker(stock+".AX").history(period="2y",interval="1wk")
    st.header(stock)
  
    fig = go.Figure(data=[go.Candlestick(x=stock_data.index,
                    open=stock_data['Open'],
                    high=stock_data['High'],
                    low=stock_data['Low'],
                    close=stock_data['Close'])])
    st.plotly_chart(fig)
    return 
asx_20_stocks = ['LNAS', 'WAM','NST','MFF','CPU']
for stock in asx_20_stocks:
  chart(stock)
