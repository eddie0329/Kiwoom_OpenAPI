import pandas as pd
import numpy as np
import sklearn
from sklearn import tree
import random
from sklearn.metrics import accuracy_score
from sklearn import ensemble
from sklearn.neural_network import MLPClassifier

# 1. Install machine learning libraries: pandas, numpy, scikit-learn, matplotlib.
# 2. Download the datasets.

def main():

    # Load the data to the variable df (Data Frame).
    df = pd.read_csv("data.csv")

    # split the data into training set and test set
    # use 75 percent of the data to train the model and hold back 25 percent
    # for testing
    train_ratio = 0.75
    # number of samples in the data_subset
    num_rows = df.shape[0]
    # shuffle the indices
    shuffled_indices = list(range(num_rows))
    random.seed(42)
    random.shuffle(shuffled_indices)

    # calculate the number of rows for training
    train_set_size = int(train_ratio * num_rows)

    # training set: take the first 'train_set_size' rows
    train_indices = shuffled_indices[:train_set_size]  # Exclusive index.
    # test set: take the remaining rows
    test_indices = shuffled_indices[train_set_size:]  # Inclusive index.

    # create training set and test set
    # Select all the rows in the data frame by the indices we have chosen.
    train_data = df.iloc[train_indices, :]
    test_data = df.iloc[test_indices, :]
    print(len(train_data), "training + ", len(test_data), "test")

    # prepare training features and training labels
    # features: all columns except 'price'
    # labels: 'price' column
    train_features = train_data.drop('Survived', axis='columns', inplace=False)
    train_labels = train_data.loc[ : , ['Survived']]

    # prepare test features and test labels
    test_features = test_data.drop('Survived', axis='columns', inplace=False)
    test_labels = test_data.loc[ : , ['Survived']]

    # CREATE THE MODEL: Replace this statement with the model of the project
    # clf = sklearn.tree.DecisionTreeClassifier()
    # clf = sklearn.ensemble.RandomForestClassifier()
    clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
                        hidden_layer_sizes=(1000, 1000, 1000), random_state=1)


    # Train the model using the training sets
    clf.fit(train_features, train_labels)

    # Make predictions using the testing set
    y_pred = clf.predict(test_features)
    y_pred_percentage = clf.predict_proba(test_features)


    acc = accuracy_score(test_labels, y_pred)

    print(acc)

    print("End of the project")



if __name__ == '__main__':
    main()

