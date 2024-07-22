import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Sidney Baraka")
    content = """
    Hi, I am Sidney! I am an aspiring developer in Python. I fancy numbers and code.
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in the course of my learning journey. Feel free to contact me!
"""
st.text(content2)