import streamlit as st
import pandas as pd
from datetime import datetime
st.title("Layout Example")
col1, col2, col3 =st.columns(3)
with col1:
    st.header("Column 1")
    st.write("This is column 1")
    vote1=st.button("Vote for column 1")
    if vote1:
        st.success("You voted for column 1")

with col2:
    st.header("Column 2")
    st.write("This is column 2")
    vote2=st.button("Vote for column 2")
    if vote2:
        st.success("You voted for column 2")

with col3:
    st.header("Column 3")
    st.write("This is column 3")   
    vote3=st.button("Vote for column 3")
    if vote3:
        st.success("You voted for column 3")  
     