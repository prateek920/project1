# -*- coding: utf-8 -*-
"""Diabetes prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1w1eMxI1Iol4vjdRaqJJdQQTWY0CGaDDP
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.model_selection import learning_curve

def plot_learning_curve(estimator, title, X, y, train_sizes, ylim=None, cv=None,
                        n_jobs=None):
 
    plt.figure()
    plt.title(title)
    if ylim is not None:
        plt.ylim(*ylim)
    plt.xlabel("Training examples")
    plt.ylabel("Score")
    train_sizes, train_scores, test_scores = learning_curve(
        estimator, X, y, cv=cv, n_jobs=n_jobs, train_sizes=train_sizes)
    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    test_scores_std = np.std(test_scores, axis=1)
    plt.grid()

    plt.fill_between(train_sizes, train_scores_mean - train_scores_std,
                     train_scores_mean + train_scores_std, alpha=0.1,
                     color="r")
    plt.fill_between(train_sizes, test_scores_mean - test_scores_std,
                     test_scores_mean + test_scores_std, alpha=0.1, color="g")
    plt.plot(train_sizes, train_scores_mean, 'o-', color="r",
             label="Training score")
    plt.plot(train_sizes, test_scores_mean, 'o-', color="g",
             label="Cross-validation score")

    plt.legend(loc="best")
    return plt


df = pd.read_csv('/content/diabetes.csv')
X = df.iloc[:, : -1]
y = df.iloc[:, -1]

#Plotting
plt.figure(figsize=(15,10))
plt.subplot(2, 2, 1)
plt.hist(df['Pregnancies'], bins = 10)
plt.xlabel('No. of times Pregnant')
plt.ylabel('Frequency')

plt.subplot(2, 2, 2)
plt.hist(df['Age'], bins = 10)
plt.xlabel('Age')
plt.ylabel('Frequency')

plt.subplot(2, 2, 3)
plt.hist(df['Glucose'], bins = 10)
plt.xlabel('Glucose')
plt.ylabel('Frequency')

plt.subplot(2, 2, 4)
plt.hist(df['BloodPressure'], bins = 10)
plt.xlabel('BloodPressure')
plt.ylabel('Frequency')

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

#Random forest
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier()
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

acc = round(accuracy_score(y_test, y_pred), 5)
print("Random Forest Classifier accuracy:", acc)

plot_learning_curve(classifier, "Learning Curve", X_train, y_train,[1,10, 20, 50, 100, 200, 300, 400], (0.7, 1.01))

plt.show()
