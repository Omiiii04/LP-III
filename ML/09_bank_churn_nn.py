"""Bank churn classifier using a normalized scikit-learn neural network."""
from __future__ import annotations

import argparse
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("csv")
    parser.add_argument("--target", default="Exited")
    args = parser.parse_args()
    df = pd.read_csv(args.csv)
    if args.target not in df:
        raise ValueError(f"target column {args.target!r} not found")
    x = df.drop(columns=[args.target]).drop(columns=["RowNumber", "CustomerId", "Surname"], errors="ignore")
    y = df[args.target]
    categorical = x.select_dtypes(exclude="number").columns
    numeric = x.select_dtypes(include="number").columns
    preprocess = ColumnTransformer([("numeric", StandardScaler(), numeric),
                                    ("categorical", OneHotEncoder(handle_unknown="ignore"), categorical)])
    model = Pipeline([("preprocess", preprocess), ("classifier", MLPClassifier(hidden_layer_sizes=(32, 16), max_iter=300, random_state=42, early_stopping=True))])
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.2, random_state=42, stratify=y)
    model.fit(x_train, y_train)
    prediction = model.predict(x_test)
    print(f"Accuracy: {accuracy_score(y_test, prediction):.4f}")
    print("Confusion matrix:\n", confusion_matrix(y_test, prediction))


if __name__ == "__main__":
    main()
