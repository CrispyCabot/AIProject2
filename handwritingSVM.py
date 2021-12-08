import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.svm import SVC

#TODO: Set Train size to be .10, .20...1 and create graph showing the accuracies
#TODO: Do the same thing but change the kernel (Use at least 1 different kernel, I would go ahead and do 2 more)

def main():
  #  df1 = pd.read_csv('mnist\\mnist_train.csv')
    df = pd.read_csv('mnist\\mnist_test.csv')
  #  df = pd.concat([df1, df2])

    labels = df['label']
    df.drop(['label'], axis=1, inplace=True)

    x_train, x_test, y_train, y_test = train_test_split(df, labels, train_size=0.8, random_state=5)

    #kernels: ‘linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’
    model = SVC(kernel='linear')

    print(x_train.shape)
    print(y_train.shape)

    model.fit(x_train, y_train)

    # Now that our classifier has been trained, let's make predictions on the test data. To make predictions, the predict method of the DecisionTreeClassifier class is used.
    y_pred = model.predict(x_test)
    print('Train accuracy: ' + str(model.score(x_train, y_train)))
    print('Test accuracy: ' + str(model.score(x_test, y_test)))

    # For classification tasks some commonly used metrics are confusion matrix, precision, recall, and F1 score.
    # These are calculated by using sklearn's metrics library contains the classification_report and confusion_matrix methods
    # print(confusion_matrix(y_test, y_pred))
    # print(classification_report(y_test, y_pred))
main()