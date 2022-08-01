import pandas as pd
df_name = pd.read_excel('Email Address.xlsx', sheet_name=0, usecols="B") #extract column B from sheet 1
n = df_name.iloc[:,0].tolist() #convert the col into list
print(n)

