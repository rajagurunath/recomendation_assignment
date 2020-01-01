import pandas as pd 
import numpy as np
import streamlit as st 
from path import Path

DIR=Path("..\listing_price_suggest.csv")
df=pd.read_csv(DIR)
st.title("Price Recommendation")
st.table(df.iloc[:5])
# st.line_chart(df.iloc[1:])
