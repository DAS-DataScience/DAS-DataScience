
import os
import pandas as pd
import numpy as no
from sklearn.datasets import load_iris, make_moons
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

#  Basic Decision Tree
iris = load_iris()

X = iris.data[:, 2:]
y = iris.target

tree_clf = DecisionTreeClassifier(max_depth=2)
tree_clf.fit(X, y)

# export_graphviz(tree_clf
#                 ,out_file=image_path("iris_tree.dot")
#                 ,feature_names=iris.feature_names[2:]
#                 ,class_names=iris.target_names
#                 ,rounded=True
#                 ,filled=True
#                 )

tree_clf.predict_proba([[5, 1.5]])
tree_clf.predict([[5, 1.5]])

#  Creating a Voting Classifier
#  Uses Make Moons
X_train, y_train = make_moons(n_samples=100, noise=0.15)
X_test, y_test = make_moons(n_samples=100, noise=0.15)

log_clf = LogisticRegression()
rdf_clf = RandomForestClassifier()
svm_clf = SVC()

estimators = [('lr',log_clf), ('rf',rdf_clf), ('svc',svm_clf)]

voting_clf = VotingClassifier(estimators=estimators
                              ,voting='hard'
                            )

from sklearn.metrics import accuracy_score
for clf in (log_clf, rdf_clf, svm_clf, voting_clf):
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print(clf.__class__.__name__, accuracy_score(y_test, y_pred))