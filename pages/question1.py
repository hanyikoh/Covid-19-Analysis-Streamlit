import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from pandas_profiling import ProfileReport

malaysia_case_dir = "epidemic/cases_malaysia.csv"
state_case_dir = "epidemic/cases_state.csv"
clusters_dir = "epidemic/clusters.csv"
malaysia_tests_dir = "epidemic/tests_malaysia.csv"
states_tests_dir = "epidemic/tests_state.csv"
pkrc_dir = "epidemic/pkrc.csv"
checkIn_dir = "mysejahtera/checkin_state.csv"

def app():
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    chosen = st.radio(
    'Choose a Dataset',
    ["Malaysia Cases", "States Cases", "Clusters", "Malaysia Tests","States Tests","PKRC","CheckIn"])
    st.write(f"You chosen {chosen} dataset!")
    start_date = "2021-07-01"
    end_date = "2021-08-31"

    if chosen == "States Cases":
        state_case_df = pd.read_csv(state_case_dir)
        after_start_date = state_case_df["date"] >= start_date
        before_end_date = state_case_df["date"] <= end_date
        between_two_dates = after_start_date & before_end_date
        state_case_df = state_case_df.loc[between_two_dates]
        st.write('First 5 rows of the dataset')
        st.table(state_case_df.head())
        st.write('Outliers detection with Boxplot')
        fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharey=True)
        # fig.suptitle('Outliers Visualization')
        plt.subplots_adjust(left=None, bottom= 0.1, right=None, top=1, wspace=0.2, hspace=0.6)

        sns.boxplot(data=state_case_df,x=state_case_df["cases_import"],ax=axes[0])
        axes[0].set_title('Import Case')
        sns.boxplot(data=state_case_df,x=state_case_df["cases_new"],ax=axes[1])
        axes[1].set_title('New Case')
        sns.boxplot(data=state_case_df,x=state_case_df["cases_recovered"],ax=axes[2])
        axes[2].set_title('Recovered Case')
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()

    elif chosen == "Clusters":
        clusters_df = pd.read_csv(clusters_dir)
        after_start_date = clusters_df["date_announced"] >= start_date
        before_end_date = clusters_df["date_announced"] <= end_date
        between_two_dates = after_start_date & before_end_date
        clusters_df = clusters_df.loc[between_two_dates]
        clusters_df['date'] = clusters_df.date_announced
        st.write('First 5 rows of the dataset')
        st.table(clusters_df.head())
        st.write('Outliers detection with Boxplot')
        fig, axes = plt.subplots(3, 3, figsize=(15, 5), sharey=True)
        # fig.suptitle('Outliers Visualization')
        plt.subplots_adjust(left=None, bottom= 0.1, right=None, top=2, wspace=0.2, hspace=0.6)

        sns.boxplot(data=clusters_df,x=clusters_df["cases_new"],ax=axes[0][0])
        axes[0][0].set_title('cases_new')
        sns.boxplot(data=clusters_df,x=clusters_df["cases_total"],ax=axes[0][1])
        axes[0][1].set_title('cases_total')
        sns.boxplot(data=clusters_df,x=clusters_df["cases_active"],ax=axes[0][2])
        axes[0][2].set_title('cases_active')
        sns.boxplot(data=clusters_df,x=clusters_df["tests"],ax=axes[1][0])
        axes[1][0].set_title('tests')
        sns.boxplot(data=clusters_df,x=clusters_df["icu"],ax=axes[1][1])
        axes[1][1].set_title('icu')
        sns.boxplot(data=clusters_df,x=clusters_df["deaths"],ax=axes[1][2])
        axes[1][2].set_title('deaths')
        sns.boxplot(data=clusters_df,x=clusters_df["recovered"],ax=axes[2][0])
        axes[2][0].set_title('recovered')
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()

    elif chosen == "States Tests":
        states_tests_df = pd.read_csv(states_tests_dir)
        after_start_date = states_tests_df["date"] >= start_date
        before_end_date = states_tests_df["date"] <= end_date
        between_two_dates = after_start_date & before_end_date
        states_tests_df = states_tests_df.loc[between_two_dates]
        st.write('First 5 rows of the dataset')
        st.table(states_tests_df.head())
        st.write('Outliers detection with Boxplot')
        fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharey=True)
        # fig.suptitle('Outliers Visualization')
        plt.subplots_adjust(left=None, bottom= 0.1, right=None, top=0.5, wspace=0.2, hspace=0.6)

        sns.boxplot(data=states_tests_df, x = states_tests_df["rtk-ag"],ax=axes[0])
        axes[0].set_title('rtk-ag')

        sns.boxplot(data=states_tests_df,x = states_tests_df["pcr"],ax=axes[1])
        axes[1].set_title('pcr')
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()

    elif chosen == "Malaysia Cases":
        malaysia_case_df = pd.read_csv(malaysia_case_dir)
        after_start_date = malaysia_case_df["date"] >= start_date
        before_end_date = malaysia_case_df["date"] <= end_date
        between_two_dates = after_start_date & before_end_date
        malaysia_case_df = malaysia_case_df.loc[between_two_dates]
        st.write('First 5 rows of the dataset')
        st.table(malaysia_case_df.head())
        st.write('Outliers detection with Boxplot')
        fig, axes = plt.subplots(4, 3, figsize=(15, 5), sharey=True)
        # fig.suptitle('Outliers Visualization')
        plt.subplots_adjust(left=None, bottom= 0.1, right=None, top=2, wspace=0.2, hspace=0.6)

        sns.boxplot(data=malaysia_case_df,x=malaysia_case_df["cases_new"],ax=axes[0][0])
        axes[0][0].set_title('New Case')
        sns.boxplot(data=malaysia_case_df,x=malaysia_case_df["cases_import"],ax=axes[0][1])
        axes[0][1].set_title('Case Imprt')
        sns.boxplot(data=malaysia_case_df,x=malaysia_case_df["cases_recovered"],ax=axes[0][2])
        axes[0][2].set_title('Case Recovered')
        sns.boxplot(data=malaysia_case_df,x=malaysia_case_df["cluster_import"],ax=axes[1][0])
        axes[1][0].set_title('cluster_workplace')
        sns.boxplot(data=malaysia_case_df,x=malaysia_case_df["cluster_religious"],ax=axes[1][1])
        axes[1][1].set_title('cluster_religious')
        sns.boxplot(data=malaysia_case_df,x=malaysia_case_df["cluster_community"],ax=axes[1][2])
        axes[1][2].set_title('cluster_community')
        sns.boxplot(data=malaysia_case_df,x=malaysia_case_df["cluster_highRisk"],ax=axes[2][0])
        axes[2][0].set_title('cluster_highRisk')
        sns.boxplot(data=malaysia_case_df,x=malaysia_case_df["cluster_education"],ax=axes[2][1])
        axes[2][1].set_title('cluster_education')
        sns.boxplot(data=malaysia_case_df,x=malaysia_case_df["cluster_detentionCentre"],ax=axes[2][2])
        axes[2][2].set_title('cluster_detentionCentre')
        sns.boxplot(data=malaysia_case_df,x=malaysia_case_df["cluster_workplace"],ax=axes[3][0])
        axes[3][0].set_title('cluster_workplace')
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()

    elif chosen == "PKRC":
        pkrc_df = pd.read_csv(pkrc_dir)
        after_start_date = pkrc_df["date"] >= start_date
        before_end_date = pkrc_df["date"] <= end_date
        between_two_dates = after_start_date & before_end_date
        pkrc_df = pkrc_df.loc[between_two_dates]
        st.write('First 5 rows of the dataset')
        st.table(pkrc_df.head())
        st.write('Outliers detection with Boxplot')
        fig, axes = plt.subplots(4, 3, figsize=(15, 5), sharey=True)
        # fig.suptitle('Outliers Visualization')
        plt.subplots_adjust(left=None, bottom= 0.1, right=None, top=2, wspace=0.2, hspace=0.6)

        sns.boxplot(data=pkrc_df, x = pkrc_df["beds"],ax=axes[0][0])
        axes[0][0].set_title('beds')
        sns.boxplot(data=pkrc_df,x = pkrc_df["admitted_pui"],ax=axes[0][1])
        axes[0][1].set_title('admitted_pui')
        sns.boxplot(data=pkrc_df, x = pkrc_df["admitted_covid"],ax=axes[0][2])
        axes[0][2].set_title("admitted_covid")
        sns.boxplot(data=pkrc_df,x = pkrc_df["admitted_total"],ax=axes[1][0])
        axes[1][0].set_title('admitted_total')
        sns.boxplot(data=pkrc_df, x = pkrc_df["discharge_pui"],ax=axes[1][1])
        axes[1][1].set_title('discharge_pui')
        sns.boxplot(data=pkrc_df,x = pkrc_df["discharge_covid"],ax=axes[1][2])
        axes[1][2].set_title('discharge_covid')
        sns.boxplot(data=pkrc_df, x = pkrc_df["discharge_total"],ax=axes[2][0])
        axes[2][0].set_title('discharge_total')
        sns.boxplot(data=pkrc_df,x = pkrc_df["pkrc_covid"],ax=axes[2][1])
        axes[2][1].set_title('pkrc_covid')
        sns.boxplot(data=pkrc_df, x = pkrc_df["pkrc_pui"],ax=axes[2][2])
        axes[2][2].set_title('pkrc_pui')
        sns.boxplot(data=pkrc_df,x = pkrc_df["pkrc_noncovid"],ax=axes[3][0])
        axes[2][0].set_title('pkrc_noncovid')

        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()

    elif chosen == "State CheckIn":
        checkIn_df = pd.read_csv(checkIn_dir)
        after_start_date = checkIn_df["date"] >= start_date
        before_end_date = checkIn_df["date"] <= end_date
        between_two_dates = after_start_date & before_end_date
        checkIn_df = checkIn_df.loc[between_two_dates]
        checkIn_df.head()
        st.write('First 5 rows of the dataset')
        st.table(checkIn_df.head())
        st.write('Outliers detection with Boxplot')
        fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharey=True)
        # fig.suptitle('Outliers Visualization')
        plt.subplots_adjust(left=None, bottom= 0.1, right=None, top=0.5, wspace=0.2, hspace=0.6)

        sns.boxplot(data=checkIn_df, x = checkIn_df["checkins"],ax=axes[0])
        axes[0].set_title('checkins')
        sns.boxplot(data=checkIn_df,x = checkIn_df["unique_ind"],ax=axes[1])
        axes[1].set_title('unique_ind')
        sns.boxplot(data=checkIn_df, x = checkIn_df["unique_loc"],ax=axes[2])
        axes[1].set_title('unique_loc')

        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()

    elif chosen == "PKRC":
        pkrc_df = pd.read_csv(pkrc_dir)
        after_start_date = pkrc_df["date"] >= start_date
        before_end_date = pkrc_df["date"] <= end_date
        between_two_dates = after_start_date & before_end_date
        pkrc_df = pkrc_df.loc[between_two_dates]
        st.write('First 5 rows of the dataset')
        st.table(pkrc_df.head())
        st.write('Outliers detection with Boxplot')
        fig, axes = plt.subplots(4, 3, figsize=(15, 5), sharey=True)
        # fig.suptitle('Outliers Visualization')
        plt.subplots_adjust(left=None, bottom= 0.1, right=None, top=2, wspace=0.2, hspace=0.6)

        sns.boxplot(data=pkrc_df, x = pkrc_df["beds"],ax=axes[0][0])
        axes[0][0].set_title('beds')
        sns.boxplot(data=pkrc_df,x = pkrc_df["admitted_pui"],ax=axes[0][1])
        axes[0][1].set_title('admitted_pui')
        sns.boxplot(data=pkrc_df, x = pkrc_df["admitted_covid"],ax=axes[0][2])
        axes[0][2].set_title("admitted_covid")
        sns.boxplot(data=pkrc_df,x = pkrc_df["admitted_total"],ax=axes[1][0])
        axes[1][0].set_title('admitted_total')
        sns.boxplot(data=pkrc_df, x = pkrc_df["discharge_pui"],ax=axes[1][1])
        axes[1][1].set_title('discharge_pui')
        sns.boxplot(data=pkrc_df,x = pkrc_df["discharge_covid"],ax=axes[1][2])
        axes[1][2].set_title('discharge_covid')
        sns.boxplot(data=pkrc_df, x = pkrc_df["discharge_total"],ax=axes[2][0])
        axes[2][0].set_title('discharge_total')
        sns.boxplot(data=pkrc_df,x = pkrc_df["pkrc_covid"],ax=axes[2][1])
        axes[2][1].set_title('pkrc_covid')
        sns.boxplot(data=pkrc_df, x = pkrc_df["pkrc_pui"],ax=axes[2][2])
        axes[2][2].set_title('pkrc_pui')
        sns.boxplot(data=pkrc_df,x = pkrc_df["pkrc_noncovid"],ax=axes[3][0])
        axes[2][0].set_title('pkrc_noncovid')
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()