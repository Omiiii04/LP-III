"""K-Means and hierarchical clustering with elbow-method selection."""
from __future__ import annotations

import argparse
import pandas as pd
from sklearn.cluster import AgglomerativeClustering, KMeans
from sklearn.preprocessing import StandardScaler


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("csv")
    parser.add_argument("--k", type=int, default=5)
    parser.add_argument("--features", nargs="+", default=["Annual Income (k$)", "Spending Score (1-100)"])
    args = parser.parse_args()
    df = pd.read_csv(args.csv)
    missing = [name for name in args.features if name not in df]
    if missing:
        raise ValueError(f"missing columns: {missing}")
    x = StandardScaler().fit_transform(df[args.features].dropna())
    print("Elbow WCSS:")
    for k in range(1, min(10, len(x)) + 1):
        print(k, f"{KMeans(n_clusters=k, n_init=10, random_state=42).fit(x).inertia_:.3f}")
    print("K-Means labels:", KMeans(n_clusters=args.k, n_init=10, random_state=42).fit_predict(x))
    print("Hierarchical labels:", AgglomerativeClustering(n_clusters=args.k).fit_predict(x))


if __name__ == "__main__":
    main()
