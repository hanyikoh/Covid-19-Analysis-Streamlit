import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
# from pages import home, about, contact

#### Tabs

# st.markdown(
#     '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">',
#     unsafe_allow_html=True,
# )
# query_params = st.experimental_get_query_params()
# tabs = ["Question 1", "Question 2", "Question 3","Question 4"]
# if "tab" in query_params:
#     active_tab = query_params["tab"][0]
# else:
#     active_tab = "Home"

# if active_tab not in tabs:
#     st.experimental_set_query_params(tab="Home")
#     active_tab = "Home"

# li_items = "".join(
#     f"""
#     <li class="nav-item">
#         <a class="nav-link{' active' if t==active_tab else ''}" href="/?tab={t}">{t}</a>
#     </li>
#     """
#     for t in tabs
# )
# tabs_html = f"""
#     <ul class="nav nav-tabs">
#     {li_items}
#     </ul>
# """

# st.markdown(tabs_html, unsafe_allow_html=True)
# st.markdown("<br>", unsafe_allow_html=True)

# if active_tab == "Question 1":
#     # home.write()
#     print('Question 1')
# elif active_tab == "Question 2":
#     # about.write()
#     print('Question 2')
# elif active_tab == "Question 3":
#     # contact.write()
#     print('Question 3')
# elif active_tab == "Question 4":
#     # contact.write()
#     print('Question 4')
# else:
#     st.error("Something has gone terribly wrong.")

# Web App Title
st.markdown('''
# **Assignment**
---
''')

# Upload CSV data
with st.sidebar.header('1. Upload your CSV data'):
    uploaded_file = st.sidebar.file_uploader(
        "Upload your input CSV file", type=["csv"])
    st.sidebar.markdown("""
[Example CSV input file](https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv)
""")

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
