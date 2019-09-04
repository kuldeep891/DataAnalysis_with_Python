# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 14:14:26 2019
Decision Tree Algorithm:
        

@author: KUKUMAR
"""
import pandas as pd

data = pd.read_csv(r'C:\Users\kukumar\OneDrive - AMDOCS\Backup Folders\Documents\GitHub\LearningPython\Entropy&InforGain\loan.csv')
print(data)

columns = ['creditscore','emibounce']
threshold = [650,2]
entropies = []

def get_best_root(df,col):
    if(col == 2):
        df1 = data.loc[data[columns[col]] >= threshold[col]]
    else:
        df1 = data.loc[data[columns[col]] <= threshold[col]]
    return df1
    #print(df1)
#print(data.loc[data.creditscore >= 650])

def get_entropy(df,length):
    df1 = df.loc[df.approval == 1]
    entropies.append((len(df1)/length) * 100)

for i in range(2):
    df_sel = get_best_root(data,i)
    get_entropy(df_sel,len(data))
    print("Printing data for iteration : ",columns[i],":\n")
    print(df_sel)
    print(entropies[i])

