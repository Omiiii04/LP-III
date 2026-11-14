"""0/1 knapsack using dynamic programming with item reconstruction."""
from __future__ import annotations

import argparse


def knapsack(capacity: int, weights: list[int], values: list[int]) -> tuple[int, list[int]]:
    if capacity < 0 or len(weights) != len(values) or any(weight < 0 for weight in weights):
        raise ValueError("invalid capacity, weights, or values")
    table = [[0] * (capacity + 1) for _ in range(len(weights) + 1)]
    for i, (weight, value) in enumerate(zip(weights, values), 1):
        for current in range(capacity + 1):
            table[i][current] = table[i - 1][current]
            if weight <= current:
                table[i][current] = max(table[i][current], value + table[i - 1][current - weight])
    chosen = []
    current = capacity
    for i in range(len(weights), 0, -1):
        if table[i][current] != table[i - 1][current]:
            chosen.append(i - 1)
            current -= weights[i - 1]
    return table[-1][-1], chosen[::-1]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--capacity", type=int, default=50)
    args = parser.parse_args()
    values, weights = [60, 100, 120], [10, 20, 30]
    maximum, selected = knapsack(args.capacity, weights, values)
    print(f"Maximum value = {maximum}; selected item indexes = {selected}")


if __name__ == "__main__":
    main()
