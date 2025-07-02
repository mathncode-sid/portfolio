import streamlit as st
import pandas

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
Below you can find some of the apps I have built in the course 
of my learning journey. Feel free to contact me!
"""
st.text(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.image("images/" + row["image"])
        st.header(row["title"])
        st.write(row["description"])
        st.write(f"[Run App]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.image("images/" + row["image"])
        st.header(row["title"])
        st.write(row["description"])
        st.write(f"[Run App]({row['url']})")
