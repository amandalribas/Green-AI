import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import numpy as np


dataset = pd.read_csv('iris.csv', header=None)

X =dataset.iloc[:, 0:4]
Y = dataset.iloc[:,4]

label_encoder = LabelEncoder()
y = label_encoder.fit_transform(Y)

x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.7, shuffle=True) #shuffle = embaralha

#train = svm.SVC()
#train.fit(x_train, y_train)

test = svm.SVC()
test.fit(x_train, y_train)


y_pred = test.predict(x_test)

y_test = np.array(y_test)
for i in range(0,len(x_test)):
    print(f"{x_test.iloc[i].values}, PREVISAO: {y_pred[i]}, REAL: {label_encoder.inverse_transform([y_test[i]])[0]}")
    #print(f"{x_test.iloc[i].values}, PREVISAO: {y_pred[i]}, REAL: {[y_test[i]][0]}") [0,1,2]


acc = test.score(x_test, y_test)
print(f"\nAcurácia no teste: {acc:.2f}")
