"""Diabetes prediction using scaled KNN and classification metrics."""
from __future__ import annotations

import argparse
import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("csv")
    parser.add_argument("--target", default="Outcome")
    args = parser.parse_args()
    df = pd.read_csv(args.csv)
    target = args.target if args.target in df else ("diabetes" if "diabetes" in df else df.columns[-1])
    x_train, x_test, y_train, y_test = train_test_split(df.drop(columns=target), df[target], test_size=.2, random_state=42, stratify=df[target])
    model = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=5))
    model.fit(x_train, y_train)
    prediction = model.predict(x_test)
    print("Confusion matrix:\n", confusion_matrix(y_test, prediction))
    print(f"Accuracy={accuracy_score(y_test, prediction):.4f}, Error rate={1 - accuracy_score(y_test, prediction):.4f}")
    print(f"Precision={precision_score(y_test, prediction, zero_division=0):.4f}, Recall={recall_score(y_test, prediction, zero_division=0):.4f}")


if __name__ == "__main__":
    main()
