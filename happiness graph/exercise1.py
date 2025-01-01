                            # DAY 32

import streamlit as st
import plotly.express as px
import pandas as pd

st.title("In Search for Happiness")
xdata = st.selectbox("select the data for x-axis",("gdp","happiness","generosity"))
ydata = st.selectbox("select the data for y-axis",("gdp","happiness","generosity"))

st.subheader(f"{xdata} and {ydata}")

fd = pd.read_csv("happy.csv")


def get_info(xdata,ydata) :
    xinform = fd[xdata]
    yinform = fd[ydata]
    return xinform,yinform


xin,yin = get_info(xdata,ydata)

# figure = px.line(x=xin,y=yin,labels={"x":f"{xdata}","y":f"{ydata}"})
figure = px.scatter(x=xin,y=yin,labels={"x":f"{xdata}","y":f"{ydata}"})
st.plotly_chart(figure)