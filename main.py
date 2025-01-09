import streamlit as st
import pandas


st.set_page_config(layout="wide")

st.title("The Best Company")
content = """
   Hi, I am Abdulganiyu! I am a Software Engineer, teacher and the founder of GsureTech. 
    I graduated in 2019 with a Bachelor Degree in Computer Science from Bayero University Kano in Nigeria. 
    I have worked with companies from various states, 
    such as Maritime Academy as a System Analyst, Hardcore Biometrics as a Software Engineer
       Hi, I am Abdulganiyu! I am a Software Engineer, teacher and the founder of GsureTech. 
    
"""
st.write(content)

st.header("Our Team")

col1, empty_col,col2, empty_col1_, col3 = st.columns([1.5,2,1.5,2,1.5])

df = pandas.read_csv("data.csv", sep=",")
with col1:
    for index, row in df[:3].iterrows():
        st.write(row["first_name"] + "  " + row["last_name"])
        st.write(row["role"])
        st.image("images/" + row["image"])

with col2:
    for index, row in df[3:6].iterrows():
        st.write(row["first_name"] + "  " + row["last_name"])
        st.write(row["role"])
        st.image("images/" + row["image"])

with col3:
    for index, row in df[6:9].iterrows():
        st.write(row["first_name"] + "  " + row["last_name"])
        st.write(row["role"])
        st.image("images/" + row["image"])

