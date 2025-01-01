                                    # DAY 32
# another method for exercise1.py using match case

import streamlit as st
import plotly.express as px
import pandas as pd

st.title("In Search for Happiness")
option_x = st.selectbox("select the data for x-axis",("gdp","happiness","generosity"))
option_y = st.selectbox("select the data for y-axis",("gdp","happiness","generosity"))

df = pd.read_csv("happy.csv")

match option_x :
    case "happiness" :
        x_array = df["happiness"]
    case "gdp" :
        x_array = df["gdp"]
    case "generosity" :
        x_array = df["generosity"]

match option_y :
    case "happiness" :
        y_array = df["happiness"]
    case "gdp" :
        y_array = df["gdp"]
    case "generosity" :
        y_array = df["generosity"]

st.subheader(f"{option_x} and {option_y}")

figure = px.scatter(x=x_array,y=y_array,labels={"x":f"{option_x}","y":f"{option_y}"})
st.plotly_chart(figure)