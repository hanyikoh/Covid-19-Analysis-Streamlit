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

def app():
    st.write("To be added")
    confusion_report(['High','medium'],['High','medium'])