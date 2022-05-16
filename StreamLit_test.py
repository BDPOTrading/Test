import pandas as pd
import streamlit as st
import os
import datetime as dt
from datetime import timedelta
from dateutil.relativedelta import relativedelta
import time

start=dt.date(2021, 1, 1)
Symbol = 'ADA-USDT'




sidebar = st.sidebar.selectbox(
    "Select a strat to see results?",
    ("Breakout", "Mean reversion", "Coming soon")
)



st.title(sidebar)



col1, col2, col3 = st.columns(3)
col1.metric("Profit", "1,428 USD", "243 USD")
col2.metric("Sharpe Ratio", "2.3", "+0.2%")
col3.metric("Drawdown", "31%", "-3.2%", delta_color='inverse')

starttime = st.slider('Select a date: ', start, dt.date.today())



leg1 = pd.read_csv('https://raw.githubusercontent.com/BDPOTrading/Test/main/ADAUSDT1h')
leg1 = leg1.set_index(["datetime"])
leg1.index = pd.to_datetime(leg1.index)
leg1 = leg1[starttime::]
print(leg1)
st.line_chart(leg1['close'])


