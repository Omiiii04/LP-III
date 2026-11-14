"""Email spam classification using KNN and SVM."""
from __future__ import annotations

import argparse
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("csv")
    parser.add_argument("--target", default=None, help="target column; defaults to the last column")
    args = parser.parse_args()
    df = pd.read_csv(args.csv).dropna()
    target = args.target or df.columns[-1]
    x = df.drop(columns=[target]).select_dtypes("number")
    y = df[target]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.2, random_state=42, stratify=y)
    for name, model in [("KNN", make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=5))),
                        ("SVM", make_pipeline(StandardScaler(), SVC(kernel="rbf")))]:
        model.fit(x_train, y_train)
        prediction = model.predict(x_test)
        print(f"\n{name}\nAccuracy: {accuracy_score(y_test, prediction):.4f}")
        print("Confusion matrix:\n", confusion_matrix(y_test, prediction))
        print(classification_report(y_test, prediction, zero_division=0))


if __name__ == "__main__":
    main()
