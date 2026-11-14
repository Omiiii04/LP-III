"""Very simple Fibonacci practical."""

n = int(input("Enter number of terms: "))
a, b = 0, 1

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

print("\nTime complexity: O(n)")
print("Space complexity: O(1)")
