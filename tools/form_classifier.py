#!/usr/bin/env python3

import pandas as pd
import argparse
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier

from sklearn.model_selection import cross_val_score


def trainModels(src):

    df = pd.read_csv(src)

    # print(df.dtypes)
    # print(df.head(10))
    # print(df.columns)

    columns_to_drop = []

    # convert categorical fields to codes
    for field in df.columns:
        if df[field].dtype == 'object':
            columns_to_drop.append(field)

    df = df.drop(columns_to_drop, axis=1)
    labels = df['research_consent']
    df = df.drop(['research_consent'], axis=1)

    for column in df.columns:
        if df[column].isnull().values.any():
            df[column].fillna(0, inplace=True)

    # correlations
    corr_matrix = df.corr()
    print(corr_matrix)
    print()

    models = []

    models.append(("LogisticRegression",LogisticRegression()))
    models.append(("SVC",SVC()))
    models.append(("LinearSVC",LinearSVC()))
    models.append(("KNeighbors",KNeighborsClassifier()))
    models.append(("DecisionTree",DecisionTreeClassifier()))
    models.append(("RandomForest",RandomForestClassifier()))
    rf2 = RandomForestClassifier(n_estimators=100, criterion='gini',
                                    max_depth=10, random_state=0, max_features=None)
    models.append(("RandomForest2",rf2))
    models.append(("MLPClassifier",MLPClassifier(solver='lbfgs', random_state=0)))

    results = []
    names = []
    for name, model in models:
        result = cross_val_score(model, df, labels,  cv=7)
        names.append(name)
        results.append(result)

    print()

    for i in range(len(names)):
        print(names[i],results[i].mean())


if __name__ == "__main__":

    # parse command-line args
    parser = argparse.ArgumentParser(description='file')
    parser.add_argument("--src", help=".csv file to train a model")
    args = parser.parse_args()

    # run puppy, run
    trainModels(args.src)
