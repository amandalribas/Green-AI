from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt

iris = load_iris()

x = iris.data
#print(x)

y = iris.target
#print(y)
#print(iris.target_names)

#print(x.shape)
#print(y.shape)


#indice = knn.predict([[6.5, 3, 5.2, 2 ]])
#print(iris.target_names[indice[0]])

x_train, x_test, y_train, y_test = train_test_split(x,y, train_size=0.7)
k_values = list()
k_accuracy = list()
for k in range (1,26):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train, y_train)
    previsoes = knn.predict(x_test)
    #print(previsoes)
    accuracy = metrics.accuracy_score(y_test, previsoes)
    k_accuracy.append(accuracy)
    k_values.append(k)
    print(f"{accuracy:.2f} Acertos em K = {k} ")


plt.plot(k_values,k_accuracy)
plt.xlabel("K Values")
plt.ylabel("Accuracy")
plt.show()
'''
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train, y_train)
previsoes = knn.predict(x_test)
#print(previsoes)
accuracy = metrics.accuracy_score(y_test, previsoes)
print(f"{accuracy:.2f} Acertos em K = 3 ")'''
