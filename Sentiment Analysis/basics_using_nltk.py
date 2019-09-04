# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 15:32:52 2019

Sentiment Analysis Program 
    Store 3 csvs, ( positive words, negative words and stop words )
    append with tags like pos and neg , combine positive and negative and use label encode to provess tags
    take input from user and remove the stop words
    take output to train logistic regression
    use logistic regression to predict the sentiment from the input

@author: KUKUMAR
Refer for better understanding of Requirements :
    https://www.cs.uic.edu/~liub/FBS/sentiment-analysis.html
"""
#import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
import pandas as pd
from sklearn import linear_model 
from sklearn import preprocessing

#import the whole nltk package once to download all the libraries and modules
#nltk.download("all")

#import the list of postive, negative words and stop words from below link
#https://github.com/jeffreybreen/twitter-sentiment-analysis-tutorial-201107/tree/08a269765a6b185d5f3dd522c876043ba9628715/data/opinion-lexicon-English

df_stop = pd.read_csv(r'C:\Users\kukumar\OneDrive - AMDOCS\Backup Folders\Documents\GitHub\LearningPython\Sentiment Analysis\stop-word-list.csv',encoding='ISO-8859-1')
df_pos = pd.read_csv(r'C:\Users\kukumar\OneDrive - AMDOCS\Backup Folders\Documents\GitHub\LearningPython\Sentiment Analysis\positive-words.csv',encoding='ISO-8859-1')
df_neg = pd.read_csv(r'C:\Users\kukumar\OneDrive - AMDOCS\Backup Folders\Documents\GitHub\LearningPython\Sentiment Analysis\negative-words.csv',encoding='ISO-8859-1')
#CHECK BELOW LINES FOR REDUCING THE CODE
#Add tags pos and neg to the list of words and concatenate them
l_pos = [i + ['pos'] for i in df_pos.values.tolist() ] 
l_neg = [i + ['neg'] for i in df_neg.values.tolist() ] 
lwords = l_pos + l_neg

df_words = pd.DataFrame(lwords,columns = ['words','tags'])

print(df_words.head(3))
print(df_stop .head(3))

#Create object of lable encoder
le_w = preprocessing.LabelEncoder()
le_t = preprocessing.LabelEncoder()



#decode tags with unique integer values
print(df_words.head(3))
df_words['tags_n'] = le_t.fit_transform(df_words['tags'])
df_words['words_n'] = le_w.fit_transform(df_words['words'])

print(df_words.head(3))

#  inverse the values transformed using label encoder
#df_words['tags'] = le.inverse_transform(df_words['tags'])
#df_words['words'] = le.inverse_transform(df_words['words'])
print(df_words.head(3))

#Convert Series values into Arrays
x_train = df_words['words_n'].values.reshape(-1,1)
y_train = df_words['tags_n'].values.reshape(-1,1)

#Create logistic Reg and train it
log_reg = linear_model.LogisticRegression()
log_reg.fit(x_train,y_train)

#Take input Data
data = input("Enter the Paragraph : \n")
print("After word_tokenize : ",word_tokenize(data))
print("After sent_tokenize : ",sent_tokenize(data))

#Remove all the stop words from the input
data_list = word_tokenize(data)
remove = list()
#print(df_stop.values.tolist())
for word in data_list:
    for i in range(len(df_stop)):
        if(df_stop.iloc[i].Values==word):
            remove.append(word)
print(remove,"with df")
stop_list = df_stop['Values'].values.tolist()
remove = list()
for i in data_list:
    if i in list(stop_list):
        remove.append(i)
print(remove,"with list")
#print(data_list)
for item in remove:
    data_list.remove(item)

print("Data after removing stop words : ",data_list)
data_listf = pd.DataFrame(data_list,columns = ['Values'])
#le_d = preprocessing.LabelEncoder()
x_test = le_w.fit_transform(data_listf['Values'])
print('TEST VALUES : ',x_test.reshape(-1,1))
ypred_log=log_reg.predict(x_test.reshape(-1,1)) 
print(ypred_log)
#FOR TAGS, USE SAME LABEL ENCODER AS OF USED FOR TAG FIR TRANSFORM
print('Predicted Value : ',le_t.inverse_transform(ypred_log))
    
#print(data_list)









