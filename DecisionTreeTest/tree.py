from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import pandas as pd
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report



df = pd.read_csv('iris.csv', header=None)



x  =df.iloc[:, 0:4]
y = df.iloc[:,4]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.7, shuffle=True) 

decision_tree = DecisionTreeClassifier(criterion='entropy')
decision_tree.fit(x_train,y_train)

print(decision_tree.feature_importances_)

tree.plot_tree(decision_tree)
#plt.show()

y_pred = decision_tree.predict(x_test)
acc = decision_tree.score(x_test,y_test)
#print(previsoes)

print(acc)


print(classification_report(y_test,y_pred))