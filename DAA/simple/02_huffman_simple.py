"""Small Huffman-coding demonstration using a frequency table."""
import heapq
from collections import Counter

text = input("Enter text: ")
frequencies = Counter(text)
heap = [[frequency, [character, ""]] for character, frequency in frequencies.items()]
heapq.heapify(heap)

while len(heap) > 1:
    low = heapq.heappop(heap)
    high = heapq.heappop(heap)
    for pair in low[1:]:
        pair[1] = "0" + pair[1]
    for pair in high[1:]:
        pair[1] = "1" + pair[1]
    heapq.heappush(heap, [low[0] + high[0]] + low[1:] + high[1:])

codes = {character: code for character, code in heap[0][1:]}
encoded = "".join(codes[character] for character in text)
print("Huffman codes:", codes)
print("Encoded text:", encoded)
print("Time complexity: O(n log n)")
