import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# Web App Title
st.markdown('''
# **Assignment**
---
''')
# Sidebar
with st.sidebar.header('1. Upload your CSV data'):
    # Upload File
    uploaded_file = st.sidebar.file_uploader(
        "Upload your input CSV file", type=["csv"])


# Import Cases and Testing Dataset
malaysia_case_dir = "epidemic/cases_malaysia.csv"
state_case_dir = "epidemic/cases_state.csv"
clusters_dir = "epidemic/clusters.csv"
malaysia_tests_dir = "epidemic/tests_malaysia.csv"
states_tests_dir = "epidemic/tests_state.csv"

malaysia_case_df = pd.read_csv(malaysia_case_dir)
pr = ProfileReport(malaysia_case_df, explorative=True)
st.header('**Input DataFrame**')
st.write(malaysia_case_df)
st.write('---')
st.header('**Pandas Profiling Report**')
st_profile_report(pr)


# Pandas Profiling Report
if uploaded_file is not None:
    @st.cache
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header('**Input DataFrame**')
    st.write(df)
    st.write('---')
    st.header('**Pandas Profiling Report**')
    st_profile_report(pr)
else:
    st.info('Awaiting for CSV file to be uploaded.')
    if st.button('Press to use Example Dataset'):
        # Example data
        @st.cache
        def load_data():
            a = pd.DataFrame(
                np.random.rand(100, 5),
                columns=['a', 'b', 'c', 'd', 'e']
            )
            return a
        df = load_data()
        pr = ProfileReport(df, explorative=True)
        st.header('**Input DataFrame**')
        st.write(df)
        st.write('---')
        st.header('**Pandas Profiling Report**')
        st_profile_report(pr)
