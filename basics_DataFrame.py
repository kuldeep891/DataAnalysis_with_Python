# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 12:16:41 2019

@author: KUKUMAR
"""
import pandas as pd
import os
import cx_Oracle as co

conn = co.connect('sa4/sa4@ilcevfz061:1521/vzcntgt1')
cursor = conn.cursor()

query = r'select * from table_contact where rownum < 2'
cursor.execute(query)

result = cursor.fetchall()

for i in result:
    print(i)

conn.close()


raw_data_path = os.path.join(os.path.pardir,'data','raw')
train_data_path = os.path.join(raw_data_path,r"C:\Users\kukumar\OneDrive - AMDOCS\Backup Folders\Documents\GitHub\LearningPython\ZS\Cristano_Ronaldo_Final_v1\data.csv" )

data = pd.read_csv(train_data_path)
print(data)

###############
#prints info of ddata alongwith the not null values count
#data.info()

#############
#print("Top  3 rows \n")
#print(data.head(3))

#print("Bottom 3 rows \n")
#print(data.tail(3))

#print(data.match_event_id.head(5))

print(data[['match_event_id','type_of_shot']].head(5))


print(data.iloc[0])
#print(data.loc[:,'_'])
