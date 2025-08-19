import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler #Padronizacao
from sklearn.preprocessing import MinMaxScaler #Normalizacao
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

df = pd.read_csv('australian.dat', sep=' ', header=None)

#Tratamento de Registros com Colunas Vazias [213], [214]
continuous = [1, 2, 6, 9, 12, 13] #2,3,7,10,13,14
categorical = [0, 3, 4, 5, 7, 8, 10, 11] 

isnull = df.isnull().sum()
#print(df.loc[pd.isnull(df[14])]) Mostra os que tem NaN na Classe

#print(df.isnull().sum())

for i in range (0,len(isnull)):
    if (isnull[i] > 0):
        if (i in continuous): #substitui pela média
            df[i] = df[i].fillna(df[i].mean())
        else:
            df[i] = df[i].fillna(int(df[i].mean()))
#print(df.isnull().sum())

#print(df.iloc[213])
#print(df.iloc[214])

x = df.iloc[:, 0:14]
y = df.iloc[:,14]

#PADRONIZANDO... (StandardScaler)
"""
print("\nAntes da Padronizacao/Normalizacao:\nMAX: ")
for i in continuous:
    print(x.iloc[:,i].max())

print("MIN:")
for i in continuous:
    print(x.iloc[:,i].min())"""


#scaler = StandardScaler()
#x_scaler = scaler.fit_transform(x)

x_standard = x.copy()
x_standard[continuous] = StandardScaler().fit_transform(x[continuous])

"""
print("\n Depois do StandardScaler: ")
for i in continuous:
    print(x_standard.iloc[:,i].max())
print("MIN")
for i in continuous:
    print(x_standard.iloc[:,i].min())"""

#x_normalize = MinMaxScaler()
#x_normalize = minmax.fit_transform(x)

x_normalize = x.copy()
x_normalize[continuous] = MinMaxScaler().fit_transform(x[continuous])

"""
print("\n Depois do MinMaxScaler: ")
for i in continuous:
    print(x_normalize.illoc[:,i].max())

for i in continuous:
    print(x_normalize.illoc[:,i].min())"""

#print(np.unique(df[0])) #Ve os valores possiveis de cada coluna

onehotencoder = ColumnTransformer(
    transformers=[('OneHot', OneHotEncoder(), categorical)],
    remainder='passthrough'
)

x_encoded = onehotencoder.fit_transform(x_normalize)
print(x_encoded)