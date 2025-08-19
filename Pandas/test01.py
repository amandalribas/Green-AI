import pandas as pd


dataframe = pd.read_csv('data00.csv')
print(f"{dataframe}\n")
dataframe_customindex = dataframe.set_index('id')
print(f"{dataframe_customindex}\n")
"""
dataframe_sorted = dataframe_customindex.sort_index()
print(f"{dataframe_sorted}\n")

dataframe_sorted = dataframe.sort_values(by = ['age', 'id'])
print(f"{dataframe_sorted}\n")
"""

#Resetando o index do custom index
dataframe = dataframe_customindex.reset_index()
print(f"{dataframe}\n")

#extraindo a coluna name
names = dataframe['name']
#names = dataframe.loc[:,'name']
#names = dataframe.iloc[:,1]
print(f"{names}\n")


#extraindo as 2 primeiras linhas (row)
obj = dataframe.iloc[[0,1], :]
print(f"{obj}\n")

#extraindo as 2 primeiras colunas
obj = dataframe.iloc[:, [0,1]]
print(f"{obj}\n")

#condicao
dataframe_condition = dataframe.loc[dataframe.age >=20]
print(f"{dataframe_condition}\n")



