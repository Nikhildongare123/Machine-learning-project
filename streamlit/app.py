import streamlit as st
import pandas as pd
import numpy as np
# Titie of the web-application
st.title("my first Streamlit web Application")

## Creating a simple DataFrame
df = pd.DataFrame({
    'column 1':[1,2,3,4,5],
    'column 2':['A','B','C','D','E']
})

## Displaying the DataFram 
st.write("Here is a simple DataFram :") 
st.dataframe(df)

## Creating a simple line chart
chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['A','B','C']
)

st.line_chart(chart_data)
