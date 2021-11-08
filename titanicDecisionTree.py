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
    # imp = SimpleImputer(missing_values=np.nan, strategy='mean')
    # imp.fit(df['Age'])
    # df['Age'] = imp.transform(df['Age'])

    stringCols = ['Sex', 'Cabin', 'Embarked', 'Ticket']
    #Force strings to be binary
    df = pd.get_dummies(df, prefix=stringCols, columns = stringCols, drop_first=True)
    #Sex will be converted to Sex_male with 1 meaning male, 0 meaning female

    print(df.head())
    print(df.columns)

    #Since we mostly have ages, we are going to just ignore rows with a missing age
    df = df[df['Age'].notna()]

    # Get labels
    y = df['Survived'].values

    # Get features
    # Not using PassengerId, Name, or Survived
    df.drop(['PassengerId', 'Name', 'Survived', 'Age'], axis=1, inplace=True)
    #Dropping name because it likely won't be beneficial
    x = df

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
    #TODO: Make predicitions on test csv file
    y_pred = decisionTree.predict(x)

main()