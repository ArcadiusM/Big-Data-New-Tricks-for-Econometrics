# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 21:06:17 2019

@author: Arkadiusz Modzelewski
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def print_confusion_matrix(confusion_matrix, class_names, figsize = (3,2), fontsize=10):

    df_cm = pd.DataFrame(confusion_matrix, index = class_names, columns = class_names)
    
    fig = plt.figure(figsize = figsize)
    
    try:
        heatmap = sns.heatmap(df_cm, annot=True, fmt="d")
    except ValueError:
        raise ValueError("Confusion matrix values must be integers.")
    
    heatmap.yaxis.set_ticklabels(heatmap.yaxis.get_ticklabels(), rotation=0, ha='right', fontsize=fontsize)
    heatmap.xaxis.set_ticklabels(heatmap.xaxis.get_ticklabels(), rotation=45, ha='right', fontsize=fontsize)
    
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    
    return fig