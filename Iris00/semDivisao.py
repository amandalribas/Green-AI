import pandas as pd
from sklearn import svm

dataset = pd.read_csv('iris.csv', header=None)
x =dataset.iloc[:, 0:4]
y = dataset.iloc[:,4]
print(x)
print()
print(y)


teste = svm.SVC()
teste.fit(x, y)

print(teste.predict([[7.2,3.0,5.8,1.6]]))
