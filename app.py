import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
# from pandas_profiling import ProfileReport
# from streamlit_pandas_profiling import st_profile_report
from multipage import MultiPage
from pages import question1,question2,question3,question4

# Create an instance of the app 
app = MultiPage()

# Import Cases and Testing Dataset
malaysia_case_dir = "epidemic/cases_malaysia.csv"
state_case_dir = "epidemic/cases_state.csv"
clusters_dir = "epidemic/clusters.csv"
malaysia_tests_dir = "epidemic/tests_malaysia.csv"
states_tests_dir = "epidemic/tests_state.csv"
pkrc_dir = "epidemic/pkrc.csv"
checkIn_dir = "mysejahtera/checkin_state.csv"

st.set_page_config(layout='wide')

# Sidebar
# with st.sidebar.header('1. Upload your CSV data'):
#     # Upload File
#     uploaded_file = st.sidebar.file_uploader(
#         "Upload your input CSV file", type=["csv"])
# st.sidebar.markdown('''[<img src='data:image/png;base64,{}' class='img-fluid' width=64 height=64>](https://streamlit.io/)'''.format(img_to_bytes("static/mooncake1.png")), unsafe_allow_html=True)
st.sidebar.header('TT3V - Mooncake')

st.sidebar.markdown('''
    Koh Han Yi (1181302907)  
    Lee Min Xuan (1181302793)  
    Tan Jia Qi (1191301879)
    '''
)

question_num = st.sidebar.selectbox(
    'Select Question:',
('Question 1', 'Question 2', 'Question 3', 'Question 4')
)

st.sidebar.markdown('__Questions__')

st.sidebar.markdown('1. Exploratory data analysis steps conducted.')
st.sidebar.markdown('2. States that exhibit strong correlation with Pahang and Johor.')
st.sidebar.markdown('3. Strong features/indicators to daily cases for Pahang, Kedah, Johor, and Selangor.')
st.sidebar.markdown('4. Models (regression/classification) that performs well in predicting the daily cases for Pahang, Kedah, Johor, and Selangor.')

st.sidebar.markdown('__Datasets Used__')
st.sidebar.markdown('Categories: Cases and Testing, Healthcare, Mobility and Contact Tracing')
st.sidebar.markdown('Filenames: cases_state.csv, clusters.csv, hospital.csv, pkrc.csv, checkin_state.csv')

st.sidebar.markdown('__Open data on COVID-19 in Malaysia__')
st.sidebar.markdown('[Ministry of Health (MOH)  Malaysia](https://github.com/MoH-Malaysia/covid19-public)')

# st.sidebar.markdown('''[<img src='data:image/png;base64,{}' class='img-fluid' width=32 height=32>](https://github.com/daniellewisDL/streamlit-cheat-sheet) <small>TDS 3301 Data Mining | Group Assignment </small>'''.format(img_to_bytes("static/mmu_logo.png")), unsafe_allow_html=True)

# Web App Title
st.title("TDS 3301 Data Mining - Group Assignment")
st.text("Question 3: COVID-19 in Malaysia")
st.write(f"## Question ({question_num})")


if question_num == "Question 1":
    question1.app()

elif question_num == "Question 2":
    question2.app()

elif question_num == "Question 3":
    question3.app()

elif question_num == "Question 4":
    question4.app()
