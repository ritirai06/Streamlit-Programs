import streamlit as st
st.title("Hello, Streamlit by RITI RAI!")
st.subheader("This is my first Streamlit app.")
st.write("I am excited to learn Streamlit and build interactive web applications.")
st.text("Stay tuned for more updates!")
st.markdown("### Let's build something amazing together!")  
language = st.selectbox("Choose your favorite programming language:", ["Python", "JavaScript", "Java", "C++", "Ruby"])
st.write(f"you choose {language} is an excellent choice!")
st.success("This Streamlit app is running successfully!")