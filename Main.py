import pandas as pd
import streamlit as st
import os
import datetime as dt
from datetime import timedelta
from dateutil.relativedelta import relativedelta

start=dt.date(2021, 1, 1)
Symbol = 'ADA-USDT'
st.title(Symbol)
st.header('The Cracked Strat')

col1, col2, col3 = st.columns(3)
col1.metric("Profit", "1,428 USD", "243 USD")
col2.metric("Sharpe Ratio", "2.3", "+0.2%")
col3.metric("Drawdown", "31%", "-3.2%", delta_color='inverse')

starttime = st.slider('Select a date: ', start, start + relativedelta(years=2))

normaliseTickerOne = 'COSUSDT'
normaliseTickerTwo = 'FIOUSDT'

base_dir = r'D:\gibbs\Documents\Python\pythonProject1\Crypto'

filename1 = r'' + str(normaliseTickerOne) + ' Binance Data'
filename2 = r'' + str(normaliseTickerTwo) + ' Binance Data'

leg_path1 = os.path.join(base_dir, filename1)
leg_path2 = os.path.join(base_dir, filename2)

leg1 = pd.read_csv(leg_path1)
leg1 = leg1.set_index(["Timestamp"])
leg1.index = pd.to_datetime(leg1.index)
leg1 = leg1["Close"]
leg1 = leg1[starttime::]

leg2 = pd.read_csv(leg_path2)
leg2 = leg2.set_index(["Timestamp"])
leg2.index = pd.to_datetime(leg2.index)
leg2 = leg2["Close"]
leg2 = leg2[starttime::]


l1_factor = 100 / (leg1[0])
norm1 = (leg1 * l1_factor)

l2_factor = 100 / (leg2[0])
norm2 = (leg2 * l2_factor)



norm1.index = pd.to_datetime(norm1.index)
norm1 = norm1.resample('15min').last()
norm1 = norm1.dropna()

norm2.index = pd.to_datetime(norm2.index)
norm2 = norm2.resample('15min').last()
norm2 = norm2.dropna()



combinedData = norm1
combinedData = pd.concat([norm1, norm2], axis=1)
combinedData = combinedData.dropna()

combinedData.columns.values[0] = normaliseTickerOne
combinedData.columns.values[1] = normaliseTickerTwo





st.line_chart(combinedData)


