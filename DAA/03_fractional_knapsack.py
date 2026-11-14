"""Fractional knapsack solved by decreasing value/weight ratio."""
from __future__ import annotations

import argparse
from dataclasses import dataclass


@dataclass(frozen=True)
class Item:
    value: float
    weight: float


def fractional_knapsack(capacity: float, items: list[Item]) -> tuple[float, list[tuple[Item, float]]]:
    if capacity < 0 or any(item.weight <= 0 for item in items):
        raise ValueError("capacity must be non-negative and weights must be positive")
    remaining, total, selected = capacity, 0.0, []
    for item in sorted(items, key=lambda x: x.value / x.weight, reverse=True):
        if remaining == 0:
            break
        fraction = min(1.0, remaining / item.weight)
        selected.append((item, fraction))
        total += item.value * fraction
        remaining -= item.weight * fraction
    return total, selected


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("capacity", type=float, nargs="?", default=50)
    args = parser.parse_args()
    items = [Item(60, 10), Item(100, 20), Item(120, 30)]
    value, selected = fractional_knapsack(args.capacity, items)
    print(f"Maximum value = {value:.2f}")
    for item, fraction in selected:
        print(f"value={item.value:g}, weight={item.weight:g}, fraction={fraction:.2f}")


if __name__ == "__main__":
    main()
