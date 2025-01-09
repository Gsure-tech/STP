import streamlit as st
import pandas


st.set_page_config(layout="wide")

st.header("The Best Company")
content = """
   Hi, I am Abdulganiyu! I am a Software Engineer, teacher and the founder of GsureTech. 
    I graduated in 2019 with a Bachelor Degree in Computer Science from Bayero University Kano in Nigeria. 
    I have worked with companies from various states, 
    such as Maritime Academy as a System Analyst, Hardcore Biometrics as a Software Engineer
       Hi, I am Abdulganiyu! I am a Software Engineer, teacher and the founder of GsureTech. 
    
"""
st.write(content)

st.subheader("Our Team")

col1,col2, col3 = st.columns(3)

df = pandas.read_csv("data.csv")
with col1:
    for index, row in df[:4].iterrows():
        st.write(f'{row["first_name"].title() + "  " + row["last_name"].title()}')
        st.write(row["role"])
        st.image("images/" + row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.write(f'{row["first_name"].title() + "  " + row["last_name"].title()}')
        st.write(row["role"])
        st.image("images/" + row["image"])

with col3:
    for index, row in df[8:12].iterrows():
        st.write(f'{row["first_name"].title() + "  " + row["last_name"].title()}')
        st.write(row["role"])
        st.image("images/" + row["image"])

