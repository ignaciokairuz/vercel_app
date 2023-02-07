import streamlit as st

st.title("Hello, Vercel!")

if st.checkbox("Show/Hide"):
    st.text("This is a checkbox example.")

name = st.text_input("Enter your name", "")
if st.button("Submit"):
    st.write("Hello, ", name)
