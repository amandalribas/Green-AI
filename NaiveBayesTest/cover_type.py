import pickle
from sklearn.naive_bayes import GaussianNB, BernoulliNB
from sklearn.metrics import confusion_matrix, classification_report

with open ("cover_type.pkl", 'rb') as f:
    (x_train, y_train, x_test, y_test)= pickle.load(f)

guassian = GaussianNB()
guassian.fit(x_train,y_train)

bernolli = BernoulliNB()
bernolli.fit(x_train,y_train)

y_pred_gauss = guassian.predict(x_test)
y_pred_bern = bernolli.predict(x_test)

print("GAUSSIAN:")
print(f"Original: {y_test}\nResultado: {y_pred_gauss}")

acc = guassian.score(x_test,y_test)
print(f"Accuracy: {acc}")

cm = confusion_matrix(y_test,y_pred_gauss)
print(cm)

print(classification_report(y_test,y_pred_gauss))

#Acurácia Maior
print("BERNOLLI:")
print(f"Original: {y_test}\nResultado: {y_pred_bern}")

acc = bernolli.score(x_test,y_test)
print(f"Accuracy: {acc}")

cm = confusion_matrix(y_test,y_pred_bern)
print(cm)

print(classification_report(y_test,y_pred_bern))