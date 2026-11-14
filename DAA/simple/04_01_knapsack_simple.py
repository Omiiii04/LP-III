"""0/1 knapsack using a small dynamic-programming table."""

values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
table = [[0] * (capacity + 1) for _ in range(len(values) + 1)]

for item in range(1, len(values) + 1):
    for weight in range(capacity + 1):
        table[item][weight] = table[item - 1][weight]
        if weights[item - 1] <= weight:
            table[item][weight] = max(
                table[item][weight],
                values[item - 1] + table[item - 1][weight - weights[item - 1]],
            )

print("Maximum value:", table[-1][-1])
