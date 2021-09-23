import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def app():
    st.write("The strong features to daily new Covid-19 cases...")
    selected_metrics = st.selectbox(
    label="Choose states", options=['TotalCases','Deaths','Recoveries']
    )