import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler #Padronizacao
from sklearn.preprocessing import MinMaxScaler #Normalizacao
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import pickle

#Le dados
df = pd.read_csv('australian.dat', sep=' ', header=None)


#Tratamento de Registros com Colunas Vazias [213], [214]

continuous = [1, 2, 6, 9, 12, 13] #A2, A3, A7, A10, A13, A14
categorical = [0, 3, 4, 5, 7, 8, 10, 11] #A1, A4, A5, A6, A8, A9. A11, A12


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


preprocessing = ColumnTransformer(
    transformers=[('OneHot', OneHotEncoder(), categorical),
                  ('StandardScaler', StandardScaler(), continuous)]
)

x_transformed = preprocessing.fit_transform(x)
#print(x_transformed)


x_train, x_test, y_train, y_test = train_test_split(
    x_transformed, y, test_size=0.75, shuffle=True) 

with open ('stalog.pkl', mode= 'wb') as f: 
    pickle.dump([x_train, x_test, y_train, y_test], f)

#train = svm.SVC()
#train.fit(x_train, y_train)

model = SVC()
model.fit(x_train, y_train)


y_pred = model.predict(x_test)

y_test = np.array(y_test)


acc = model.score(x_test, y_test)
print(f"\nAcurácia no teste: {acc:.2f}")