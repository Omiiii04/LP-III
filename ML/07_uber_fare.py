"""Uber fare regression: preprocessing, outlier filtering, correlation and models."""
from __future__ import annotations

import argparse
import math
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


def haversine(lat1, lon1, lat2, lon2):
    radius = 6371.0
    dlat, dlon = math.radians(lat2 - lat1), math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    return 2 * radius * math.asin(math.sqrt(a))


def prepare(path: str) -> tuple[pd.DataFrame, pd.Series]:
    df = pd.read_csv(path)
    target = "fare_amount"
    required = [target, "pickup_latitude", "pickup_longitude", "dropoff_latitude", "dropoff_longitude"]
    missing = [column for column in required if column not in df]
    if missing:
        raise ValueError(f"missing columns: {missing}")
    df = df[required].dropna()
    df = df[(df[target] > 0) & df.pickup_latitude.between(-90, 90) & df.dropoff_latitude.between(-90, 90)]
    df["distance_km"] = df.apply(lambda r: haversine(r.pickup_latitude, r.pickup_longitude, r.dropoff_latitude, r.dropoff_longitude), axis=1)
    q1, q3 = df[target].quantile([.01, .99])
    df = df[df[target].between(q1, q3)]
    return df[["distance_km"]], df[target]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("csv")
    args = parser.parse_args()
    x, y = prepare(args.csv)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.2, random_state=42)
    for name, model in [("Linear regression", LinearRegression()), ("Random forest", RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1))]:
        model.fit(x_train, y_train)
        prediction = model.predict(x_test)
        print(f"{name}: R2={r2_score(y_test, prediction):.4f}, RMSE={mean_squared_error(y_test, prediction) ** .5:.4f}")
    print("Correlation matrix:\n", pd.concat([x, y.rename("fare_amount")], axis=1).corr())


if __name__ == "__main__":
    main()
