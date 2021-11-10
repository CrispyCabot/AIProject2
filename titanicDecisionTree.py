import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree

def main():
    ''' ### Read csv data '''
    df = pd.read_csv('Titanic_training.csv')
    testDf = pd.read_csv('Titanic_test.csv')
    print("There are total ", len(df), " sample in the loaded dataset.")
    print("The size of the dataset is: ", df.shape)

    #Replace missing values with averages
    # imp = SimpleImputer(missing_values=np.nan, strategy='mean')
    # imp.fit(df['Age'])
    # df['Age'] = imp.transform(df['Age'])

    stringCols = ['Sex', 'Cabin', 'Embarked', 'Ticket']
    #Force strings to be binary
    #This essentially converts string features into many features but binary
    #e.g. the string C85 will be turned into a feature, Cabin_C85 with the value 1
    #indicating it is C85 while everything else will have the value 0
    df = pd.get_dummies(df, prefix=stringCols, columns = stringCols, drop_first=True)
    testDf = pd.get_dummies(testDf, prefix=stringCols, columns = stringCols, drop_first=True)

    print(df['Sex_male'])

    # print(df.head())
    # print(df.columns)

    #Since we mostly have ages, we are going to just ignore rows with a missing age
    df = df[df['Age'].notna()]

    #Need to make up ages, however, for test data that doesn't have an age because we still want to get one
    #So set missing ages to the average age of train data
    avgAge = df['Age'].mean()
    testDf['Age'].fillna(int(avgAge), inplace=True)

    # Get labels
    y = df['Survived'].values

    # Get features
    # Not using PassengerId, Name, or Survived as features
    df.drop(['PassengerId', 'Name', 'Survived'], axis=1, inplace=True)
    features = df.columns

    testDf.drop(['PassengerId', 'Name'], axis=1, inplace=True)
    #Drop all columns in testDf not found to be a feature
    testDf = testDf[testDf.columns.intersection(features)]
    #Add all missing feature columns with value of 0
    for feature in features:
        if feature not in testDf.columns:
            testDf[feature] = 0

    #Order columns the same
    testDf = testDf[df.columns]
    testDf = testDf.fillna(df.mean())

    x = df

    print("Shape of train x and y")
    print(x.shape, y.shape)
    print("Shape of test x")
    print(testDf.shape)

    #Create the decision tree
    decisionTree = DecisionTreeClassifier(max_leaf_nodes=30, random_state=0, max_depth=6, criterion='entropy')

    decisionTree.fit(x, y)

    #Saves the decision tree as a png image so we can easily see it
    plt.figure(figsize=(24, 12))
    plot_tree(decisionTree, fontsize=6, rounded=True)
    plt.savefig('decisiontree.png', bbox_inches="tight")    

    #Make predictions
    #Make predicitions on test csv file
    y_pred = decisionTree.predict(testDf)
    resultsDf = pd.read_csv('Titanic_Dataset_Accuracy_Test\\DecisionTree_submission_file_template.csv')
    resultsDf['Survived'] = y_pred

    resultsDf.to_csv('results.csv', index=False)

main()