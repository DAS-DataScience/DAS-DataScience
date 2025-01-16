
import os
import pandas as pd
import numpy as no
from sklearn.datasets import load_iris, make_moons
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.ensemble import RandomForestClassifier, VotingClassifier

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