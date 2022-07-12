import pandas as pd
df = pd.read_csv("plik.csv")
#checking the number of empty rows in th csv file
print (df.isnull().sum())
#Droping the empty rows
modifiedDF = df.dropna()
#Saving it to the csv file
modifiedDF.to_csv('test.csv', index=False)