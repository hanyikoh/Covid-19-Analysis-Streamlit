import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import display
from sklearn.ensemble import RandomForestClassifier
from boruta import BorutaPy
from sklearn.feature_selection import RFECV

import numpy as np
import pandas as pd

from matplotlib import pyplot as plt
import seaborn as sns

from sklearn.preprocessing import MinMaxScaler
from tqdm import tqdm_notebook, tqdm
#tqdm.pandas(tqdm_notebook)

import warnings
warnings.filterwarnings('ignore')

start_date = "2021-07-01"
end_date = "2021-08-31"
df_final = pd.read_csv("data.csv")
df_final.rename(columns = {'Unnamed: 0': 'date', 'Unnamed: 1': 'state'}, inplace=True)
rslt_df_ph = df_final[df_final['state'] == "Pahang"]
rslt_df_kd = df_final[df_final['state'] == "Kedah"]
rslt_df_jh = df_final[df_final['state'] == "Johor"]
rslt_df_sl = df_final[df_final['state'] == "Selangor"]
rf = RandomForestClassifier(n_jobs=-1, class_weight="balanced",criterion = "entropy")
feat_selector = BorutaPy(rf, n_estimators="auto", random_state=1)

def ranking(ranks, names, order=1):
    minmax = MinMaxScaler()
    ranks = minmax.fit_transform(order*np.array([ranks]).T).T[0]
    ranks = map(lambda x: round(x,2), ranks)
    return dict(zip(names, ranks))

def app():
    
    st.markdown("### " +"The strong features to daily new Covid-19 cases...")
    st.markdown("#### We have used two different methods, which are Boruta and Recursive Feature Elimination (RFE) to select the most useful feature. Feature selection can reduce overfitting, increase the model's accuracy and reduce training time. " 
            + "By applying in different state, we might get different rank of the features.")
    st.markdown("##### Choose state(s) that you want to view ^ o ^")
    selected_metrics = st.selectbox(label = "State :", options=['Pahang','Johor','Kedah','Selangor','All 4 states'] )
    
    if selected_metrics == "Pahang":
        df = rslt_df_ph
    elif selected_metrics == "Kedah":
        df = rslt_df_kd
    elif selected_metrics == "Johor" :  
        df = rslt_df_jh
    elif selected_metrics == "Selangor" :
        df = rslt_df_sl
    elif selected_metrics == "All 4 states" :
        df = df_final
        
    y = df.cases_new
    X = df.drop(["cases_new","date","state"], 1)
    colnames = X.columns
    feat_selector.fit(X.values, y.values.ravel())
    boruta_score = ranking(list(map(float, feat_selector.ranking_)), colnames, order=-1)
    boruta_score = pd.DataFrame(list(boruta_score.items()), columns=['Features', 'Score']) 
    boruta_score = boruta_score.sort_values("Score",ascending = False)
    
    
    #rf=RandomForestClassifier(n_jobs=-1, class_weight="balanced", max_depth = 5, n_estimators = 100)
    rf.fit(X,y)
    rfe = RFECV(rf, min_features_to_select = 1, cv =2)
    rfe.fit(X,y)
    rfe_score = ranking(list(map(float, rfe.ranking_)), colnames, order=-1)
    rfe_score = pd.DataFrame(list(rfe_score.items()), columns=['Features', 'Score'])
    rfe_score = rfe_score.sort_values("Score", ascending = False)

    chosen = st.radio('Choose a feature selection method',["Boruta feature selection", "RFE Feature Selection"])
    
    st.markdown("#### " +"Features ranking using " + chosen + " method in " + selected_metrics)
    if chosen == "Boruta feature selection":
        top15 = boruta_score.head(15).reset_index(drop=True)
        sns.catplot(x="Score", y="Features", data = boruta_score[0:35], kind = "bar", 
               height=14, aspect=1.1, palette='RdYlBu')
        plt.title("Boruta Features Ranking")
        st.pyplot()
        
    elif chosen == "RFE Feature Selection":
        top15 = rfe_score.head(15).reset_index(drop=True)
        sns.catplot(x="Score", y="Features", data = rfe_score[0:35], kind = "bar", 
               height=14, aspect=1.1, palette='Spectral')
        plt.title("RFE Features Ranking")
        st.pyplot()
    st.markdown("#### " +"Top 15 features using " + chosen + " method in " + selected_metrics)
    if chosen == "Boruta feature selection":    
        st.table(top15)
    elif chosen == "RFE Feature Selection":
        st.table(top15)