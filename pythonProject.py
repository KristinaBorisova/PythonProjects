import numpy as np 
import pandas as pd 

df = pd.read_csv(r"C:\Users\User\Desktop\clubs\AUBG AI\ks2016.csv", encoding ="cp1252") #df is daved as data-frame variable 
print(df)

column_names = list(df.columns) # list function -> creates a list ; 
print(column_names) #printing all columns names - printing data 

entries_in_state = df["state "].unique()   # ---> sounds good, but would not work
print(entries_in_state) 

count_entries = df.groupby('state ')['ID '].nunique() #groupby() is a function, this is why we have '' instead of ""
print(count_entries)


df['target_variable'] = np.where(df['state ']=='successful', 1, 0) #np.where -> numpy function that saya "Take the data frame we have, look for column 'state', if this is true, put 1 //true otherwise put 0 //false  "
print(df['target_variable']) # print the specific column 

#creating new variable to print values ; 0 = false, 1 = true 
values = df.groupby('target_variable')['ID '].nunique()
print(values)