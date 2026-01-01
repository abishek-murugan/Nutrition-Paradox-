import streamlit as st

st.header("📘 Project Overview")

st.subheader("Problem Statement")
st.markdown("""
The goal of this project is to analyze global patterns of **obesity and malnutrition**
across countries, regions, age groups, and genders using WHO public datasets.
""")

st.subheader("Business Use Cases")
st.markdown("""
- Identify regions requiring urgent nutrition intervention  
- Understand demographic disparities (age, gender)  
- Support data-driven health policy planning  
- Highlight coexistence of obesity and malnutrition (nutrition paradox)
""")

st.subheader("Project Workflow")
st.markdown("""
1. Dataset collection from WHO APIs  
2. Data cleaning & feature engineering  
3. Exploratory Data Analysis (EDA)  
4. SQL table creation & query writing  
5. Streamlit dashboard for analysis & reporting  
""")
