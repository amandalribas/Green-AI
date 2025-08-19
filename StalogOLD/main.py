import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
import numpy as np

dataset = pd.read_csv('shuttle.tst', sep=' ', header=None)
#print(dataset)

x = dataset.iloc[:, 0:9]
y = dataset.iloc[:,9]

#print(x)
#print(y)

class_names = {
    1: "Rad Flow",
    2: "Fpv Close",
    3: "Fpv Open",
    4: "High",
    5: "Bypass",
    6: "Bpv Close",
    7: "Bpv Open"
}

#treinando
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.7, shuffle=True)

train = svm.SVC()
train.fit(x_train,y_train)


y_pred = train.predict(x_test)
y_test = np.array(y_test)


for i in range(0,len(x_test)):
    print(f"{x_test.iloc[i].values}, PREVISAO: {class_names.get(y_pred[i])}, REAL: {class_names.get(y_test[i])}")
    #print(f"{x_test.iloc[i].values}, PREVISAO: {y_pred[i]}, REAL: {[y_test[i]][0]}") [0,1,2]
acc = train.score(x_test, y_test)
print(f"Acurácia no teste: {acc:.2f}")