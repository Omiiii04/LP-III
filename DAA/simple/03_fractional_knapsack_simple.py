"""Fractional knapsack using the greedy method."""

values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
items = sorted(
    zip(values, weights),
    key=lambda item: item[0] / item[1],
    reverse=True,
)

total_value = 0
for value, weight in items:
    if capacity >= weight:
        capacity -= weight
        total_value += value
    else:
        total_value += value * capacity / weight
        break

print("Maximum value:", total_value)
