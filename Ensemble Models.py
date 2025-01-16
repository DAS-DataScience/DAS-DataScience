
import os
import pandas as pd
import numpy as no
from sklearn.datasets import load_iris, make_moons
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.ensemble import RandomForestClassifier, VotingClassifier, BaggingClassifier, AdaBoostClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
import xgboost

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
X_train, y_train = make_moons(n_samples=10000, noise=0.15)
X_test, y_test = make_moons(n_samples=1000, noise=0.15)

log_clf = LogisticRegression()
rdf_clf = RandomForestClassifier()
svm_clf = SVC()

estimators = [('lr',log_clf), ('rf',rdf_clf), ('svc',svm_clf)]

voting_clf = VotingClassifier(estimators=estimators
                              ,voting='hard'
                            )


for clf in (log_clf, rdf_clf, svm_clf, voting_clf):
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print(clf.__class__.__name__, accuracy_score(y_test, y_pred))

#  Create a Bagging Classifier

bag_clf = BaggingClassifier(
                            DecisionTreeClassifier()
                            ,n_estimators=500
                            ,max_samples=100
                            ,bootstrap=True
                            ,n_jobs=-1
                           )
bag_clf.fit(X_train, y_train)
y_pred = bag_clf.predict(X_test)
print(accuracy_score(y_test, y_pred))

#  Out of Bag (oob) Variation
bag_oob_clf = BaggingClassifier(
                            DecisionTreeClassifier()
                            ,n_estimators=500
                            ,max_samples=100
                            ,bootstrap=True
                            ,n_jobs=-1
                            ,oob_score=True
                           )
bag_oob_clf.fit(X_train, y_train)
y_pred = bag_oob_clf.predict(X_test)
print(accuracy_score(y_test, y_pred))

#  Random Forest Classifier

rdf_clf = RandomForestClassifier(n_estimators=500, max_leaf_nodes=16, n_jobs=-1)
rdf_clf.fit(X_train, y_train)
y_pred = rdf_clf.predict(X_test)

#  Boosting with AdaBoost Classifier
ada_clf = AdaBoostClassifier(DecisionTreeClassifier(max_depth=1)
                             ,n_estimators=200
                             ,algorithm="SAMME.R"
                             ,learning_rate=0.5)
ada_clf.fit(X_train, y_train)

#  Gradient Boosting Classifier sklearn

gbrt_clf = GradientBoostingClassifier(max_depth=2
                                      ,n_estimators=3
                                      ,learning_rate=1.0
                                      )
gbrt_clf.fit(X_train, y_train)

#  Put in Section about early stopping

#  XGBoost - has built in early stopping
xgb_reg = xgboost.XGBClassifier()
xgb_reg.fit(X_train, y_train)
y_pred = xgb_reg.predict(X_test)