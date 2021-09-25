import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder

state_case_dir = "dataset/cases_state.csv"

def app():
    st.markdown('> What are the states that exhibit strong correlation with Pahang and Johor?')
    selected_correlation = st.selectbox(
    label="Evaluate Correlation On", options=['New Cases','Imported Cases','Recovered Cases']
    )
    state_case_df = pd.read_csv(state_case_dir)
    date = state_case_df.date
    state_case_df = pd.get_dummies(state_case_df, prefix='', columns=['state'])
    # state_case_df
    state_case_import_df = state_case_df.loc[:,'_Johor':].multiply(state_case_df["cases_import"], axis="index")
    state_case_new_df = state_case_df.loc[:,'_Johor':].multiply(state_case_df["cases_new"], axis="index")
    state_case_recovered_df = state_case_df.loc[:,'_Johor':].multiply(state_case_df["cases_recovered"], axis="index")
    
    state_case_import_df['date'] = date
    state_case_new_df['date'] = date
    state_case_recovered_df['date'] = date

    state_case_import_df = state_case_import_df.groupby([state_case_import_df['date']]).sum()
    state_case_new_df = state_case_new_df.groupby([state_case_new_df['date']]).sum()
    state_case_recovered_df = state_case_recovered_df.groupby([state_case_recovered_df['date']]).sum()

    state_case_import_df.columns = state_case_import_df.columns.str[1:]
    state_case_new_df.columns = state_case_new_df.columns.str[1:]
    state_case_recovered_df.columns = state_case_recovered_df.columns.str[1:]
    if selected_correlation == "New Cases":
        st.write('The state that exhibit strongest correlation in terms of New Covid Cases with Pahang: Kedah, correlation coefficient = 0.94')     
        st.write('The state that exhibit strongest correlation in terms of New Covid Cases with Johor: Perak and Pulau Pinang, correlation coefficient = 0.93')     
        
        corr = state_case_new_df.corr()
        fig, ax = plt.subplots(figsize=(20,10))  
        ax = sns.heatmap(
            corr, 
            vmin=-1, vmax=1, center=0,
            cmap=sns.diverging_palette(20, 220, n=200),
            square=True,
            annot = True,
            linewidths = 2
        )

        ax.set_xticklabels(
            ax.get_xticklabels(),
            rotation=45,
            horizontalalignment='right'
        )
        ax.set_title('Cases Correlation Heatmap')
        st.pyplot()

    elif selected_correlation == "Imported Cases":
        st.write('The state that exhibit strongest correlation in terms of Imported Covid Cases with Pahang: Perak, correlation coefficient = 0.26')     
        st.write('The state that exhibit strongest correlation in terms of Imported Covid Cases with Johor: Pulau Pinang, correlation coefficient = 0.17')     
        
        corr = state_case_import_df.corr()
        fig, ax = plt.subplots(figsize=(20,10))  
        ax = sns.heatmap(
            corr, 
            vmin=-1, vmax=1, center=0,
            cmap=sns.diverging_palette(20, 220, n=200),
            square=True,
            annot = True,
            linewidths = 2
        )

        ax.set_xticklabels(
            ax.get_xticklabels(),
            rotation=45,
            horizontalalignment='right'
        )
        ax.set_title('Imported Cases Correlation Heatmap')
        st.pyplot()

    elif selected_correlation == "Recovered Cases":
        st.write('The state that exhibit strongest correlation in terms of Recovered Cases with Pahang: Kedah, correlation coefficient = 0.93')     
        st.write('The state that exhibit strongest correlation in terms of Recovered Cases with Johor: Perak, correlation coefficient = 0.83')     
        
        corr = state_case_recovered_df.corr()
        fig, ax = plt.subplots(figsize=(20,10))  
        ax = sns.heatmap(
            corr, 
            vmin=-1, vmax=1, center=0,
            cmap=sns.diverging_palette(20, 220, n=200),
            square=True,
            annot = True,
            linewidths = 2
        )

        ax.set_xticklabels(
            ax.get_xticklabels(),
            rotation=45,
            horizontalalignment='right'
        )
        ax.set_title('Recovered Cases Correlation Heatmap')
        st.pyplot()