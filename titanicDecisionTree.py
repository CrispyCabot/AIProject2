import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.tree import plot_tree

def main():
    ''' ### Read csv data '''
    df = pd.read_csv('Titanic_training.csv')
    print("There are total ", len(df), " sample in the loaded dataset.")
    print("The size of the dataset is: ", df.shape)

    #Replace missing values with averages
    imp = SimpleImputer(missing_values=np.nan, strategy='mean')
    imp.fit(df['Age'])
    df['Age'] = imp.transform(df['Age'])

    stringCols = ['Sex', 'Ticket', 'Cabin', 'Embarked']
    #Force strings to be binary
    df = pd.get_dummies(df, prefix=stringCols, columns = stringCols, drop_first=True)

    print(df.head())

    # Get labels
    y = df['Survived'].values

    # Get features
    #Dropping name because it likely won't be beneficial
    df.drop('Name', axis=1, inplace=True)
    x = df.drop('Survived', axis=1).values

    #Don't need train_test_split because test is in a separate file
    print(x.shape, y.shape)

    #Create the decision tree
    decisionTree = DecisionTreeClassifier(max_leaf_nodes=30, random_state=0, max_depth=6)

    decisionTree.fit(x, y)

    #Displays the decision tree
    plt.figure(figsize=(24, 12))
    plot_tree(decisionTree, fontsize=6, rounded=True)
    plt.savefig('decisiontree.png', bbox_inches="tight")    

    #Make predictions
    # Now that our classifier has been trained, let's make predictions on the test data. To make predictions, the predict method of the DecisionTreeClassifier class is used.
    y_pred = decisionTree.predict(x)

    # For classification tasks some commonly used metrics are confusion matrix, precision, recall, and F1 score.
    # These are calculated by using sklearn's metrics library contains the classification_report and confusion_matrix methods
    # print(confusion_matrix(y_test, y_pred))
    # print(classification_report(y_test, y_pred))

main()