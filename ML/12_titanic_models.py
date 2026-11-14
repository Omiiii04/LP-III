"""Titanic survival prediction and comparison of common classifiers."""
from __future__ import annotations

import argparse
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.svm import SVC


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("csv")
    args = parser.parse_args()
    df = pd.read_csv(args.csv)
    target = "Survived"
    x = df.drop(columns=[target, "PassengerId", "Name", "Ticket", "Cabin"], errors="ignore")
    y = df[target]
    categorical = x.select_dtypes(exclude="number").columns
    numeric = x.select_dtypes(include="number").columns
    preprocess = ColumnTransformer([("numeric", Pipeline([("fill", __import__("sklearn").impute.SimpleImputer(strategy="median")), ("scale", StandardScaler())]), numeric),
                                    ("categorical", Pipeline([("fill", __import__("sklearn").impute.SimpleImputer(strategy="most_frequent")), ("onehot", OneHotEncoder(handle_unknown="ignore"))]), categorical)])
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.2, random_state=42, stratify=y)
    for name, classifier in [("Logistic regression", LogisticRegression(max_iter=1000)), ("Random forest", RandomForestClassifier(n_estimators=200, random_state=42)), ("SVM", SVC())]:
        model = Pipeline([("preprocess", preprocess), ("classifier", classifier)])
        model.fit(x_train, y_train)
        print(f"{name}: {accuracy_score(y_test, model.predict(x_test)):.4f}")


if __name__ == "__main__":
    main()
