import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier 
from sklearn.naive_bayes import GaussianNB

from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from sklearn.metrics import precision_recall_curve

df_final = pd.read_csv("data.csv")
df_final.rename(columns = {'Unnamed: 0': 'date', 'Unnamed: 1': 'state'}, inplace=True)
rslt_df_ph = df_final[df_final['state'] == "Pahang"]
rslt_df_kd = df_final[df_final['state'] == "Kedah"]
rslt_df_jh = df_final[df_final['state'] == "Johor"]
rslt_df_sl = df_final[df_final['state'] == "Selangor"]

def confusion_report(y_test, y_pred):
    # Confusion matrix report

    evaluation_methods = []
    evaluation_scores = []

    confusion_majority=confusion_matrix(y_test, y_pred)

    print('Mjority classifier Confusion Matrix\n', confusion_majority)

    print('**********************')
    print('Majority TN= ', confusion_majority[0][0])
    print('Majority FP=', confusion_majority[0][1])
    print('Majority FN= ', confusion_majority[1][0])
    print('Majority TP= ', confusion_majority[1][1])
    print('**********************')

    precision = precision_score(y_test, y_pred, pos_label="High")
    recall = recall_score(y_test, y_pred, pos_label="High")
    f1 = f1_score(y_test, y_pred, pos_label="High")
    accuracy = accuracy_score(y_test, y_pred)

    evaluation_methods.append('Precision')
    evaluation_methods.append('Recall')
    evaluation_methods.append('F1')
    evaluation_methods.append('Accuracy')

    evaluation_scores.append(precision)
    evaluation_scores.append(recall)
    evaluation_scores.append(f1)
    evaluation_scores.append(accuracy)

    st.table(pd.DataFrame({'Evaluation Method':evaluation_methods, 'Score':evaluation_scores}).set_index('Evaluation Method'))

def showMSE(y_test,y_pred):
    from sklearn.metrics import r2_score,median_absolute_error,mean_squared_error,mean_absolute_error
    evaluation_methods = []
    evaluation_scores = []
    
    evaluation_methods.append('Median absolute error')
    evaluation_methods.append('Mean absolute error')
    
    evaluation_scores.append(median_absolute_error(y_test, y_pred))
    evaluation_scores.append(mean_absolute_error(y_test, y_pred))
    st.table(pd.DataFrame({'Evaluation Method':evaluation_methods, 'Score':evaluation_scores}).set_index('Evaluation Method'))

def read_choice(state_choice):
    if state_choice == "Pahang":
        df = rslt_df_ph
    elif state_choice == "Kedah":
        df = rslt_df_kd
    elif state_choice == "Johor" :  
        df = rslt_df_jh
    elif state_choice == "Selangor" :
        df = rslt_df_sl
    elif state_choice == "All 4 states" :
        df = df_final
    
        
def app():
    #st.write("To be added")
    #confusion_report(['High','medium'],['High','medium'])
    st.markdown('> Comparing regression and classification models, what model performs well in predicting the daily cases for Pahang, Kedah, Johor, and Selangor?')
    state_choice = st.selectbox( label = "Choose a State :", options=['Pahang','Johor','Kedah','Selangor','All 4 states'] )
    model_choice = st.selectbox( label = "Choose regressor or classifier :", options=['Regressor','Classifier'] )
    read_choice(state_choice)