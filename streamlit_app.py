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
    'Frequency',
    ('Daily', 'Weekly', 'Monthly'))
   
import datetime
import pytz
india_timezone = pytz.timezone('Asia/Kolkata')
india_time = datetime.datetime.now(india_timezone)
st.write("India time:-", india_time.strftime("%Y-%m-%d %H:%M:%S"))
india_timezone = pytz.timezone('Australia/Sydney')
india_time = datetime.datetime.now(india_timezone)
st.write("Sydney time:-", india_time.strftime("%Y-%m-%d %H:%M:%S"))


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
    

  
    fig = go.Figure(data=[go.Candlestick(x=stock_data.index,
                    open=stock_data['Open'],
                    high=stock_data['High'],
                    low=stock_data['Low'],
                    close=stock_data['Close']
                                        ,increasing_line_color= 'green', decreasing_line_color= 'red')])
    fig.update_layout(
    title=stock+"   ->   "+    round(yf.Ticker(stock+".AX").history(period="1d",interval="1d")['Close'][0],2).astype('str')
    )
    st.plotly_chart(fig,use_container_width=True)
    return 
asx_20_stocks = ['LNAS','LSF', 'WAM','NST','MFF','CPU','WOW','BHP','AKE','ARG','VHY','IOZ']
for stock in asx_20_stocks:
  chart(stock)
  st.write('-----------------------------------')
