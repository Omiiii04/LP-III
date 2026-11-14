"""Huffman encoding and decoding using a greedy min-heap."""
from __future__ import annotations

import argparse
import heapq
from dataclasses import dataclass
from itertools import count


@dataclass
class Node:
    frequency: int
    character: str | None = None
    left: "Node | None" = None
    right: "Node | None" = None


def build_tree(text: str) -> Node:
    if not text:
        raise ValueError("text must not be empty")
    sequence = count()
    heap = [(frequency, next(sequence), Node(frequency, char))
            for char, frequency in __import__("collections").Counter(text).items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        f1, _, left = heapq.heappop(heap)
        f2, _, right = heapq.heappop(heap)
        parent = Node(f1 + f2, left=left, right=right)
        heapq.heappush(heap, (parent.frequency, next(sequence), parent))
    return heap[0][2]


def codes(node: Node, prefix: str = "", result: dict[str, str] | None = None) -> dict[str, str]:
    result = {} if result is None else result
    if node.character is not None:
        result[node.character] = prefix or "0"
    else:
        codes(node.left, prefix + "0", result)  # type: ignore[arg-type]
        codes(node.right, prefix + "1", result)  # type: ignore[arg-type]
    return result


def encode(text: str) -> tuple[str, dict[str, str]]:
    mapping = codes(build_tree(text))
    return "".join(mapping[char] for char in text), mapping


def decode(bits: str, root: Node) -> str:
    if root.character is not None:
        return root.character * len(bits)
    output, node = [], root
    for bit in bits:
        node = node.left if bit == "0" else node.right  # type: ignore[assignment]
        if node.character is not None:
            output.append(node.character)
            node = root
    if node is not root:
        raise ValueError("incomplete Huffman bit stream")
    return "".join(output)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("text", nargs="?", default="this is an example for huffman encoding")
    args = parser.parse_args()
    tree = build_tree(args.text)
    bit_string, mapping = encode(args.text)
    print("Codes:", mapping)
    print("Encoded:", bit_string)
    print("Decoded:", decode(bit_string, tree))


if __name__ == "__main__":
    main()
