"""Recursive and iterative Fibonacci implementations."""
from __future__ import annotations

import argparse
import time


def fibonacci_recursive(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    if n < 2:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iterative(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int, nargs="?", default=10)
    args = parser.parse_args()
    start = time.perf_counter()
    recursive = fibonacci_recursive(args.n)
    recursive_time = time.perf_counter() - start
    start = time.perf_counter()
    iterative = fibonacci_iterative(args.n)
    iterative_time = time.perf_counter() - start
    print(f"F({args.n}) recursive = {recursive} ({recursive_time:.6f}s)")
    print(f"F({args.n}) iterative = {iterative} ({iterative_time:.6f}s)")
    print("Complexity: recursive O(2^n) time, O(n) stack; iterative O(n) time, O(1) space")


if __name__ == "__main__":
    main()
