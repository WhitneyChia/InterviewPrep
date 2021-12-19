"""
https://www.hackerrank.com/challenges/tree-huffman-decoding/problem

For instance, consider the string ABRACADABRA.

Input characters are only present in the leaves. Internal nodes have a character value of ϕ (NULL).
We can determine that our values for characters are:
A - 0
B - 111
C - 1100
D - 1101
R - 10

Our Huffman encoded string is:
A B    R  A C     A D     A B    R  A
0 111 10 0 1100 0 1101 0 111 10 0
or
01111001100011010111100
"""
import heapq
from collections import defaultdict


def encode_huffman(s):
    frequency = generate_frequency(s)
    heap = [[weight, [symbol, '']] for symbol, weight in frequency.items()]
    heapq.heapify(heap)
    print(heap)
    print("\n")
    while len(heap) > 1:
        low = heapq.heappop(heap)
        high = heapq.heappop(heap)
        for value in low[1:]:
            value[1] = '0' + value[1]
        for value in high[1:]:
            value[1] = '1' + value[1]
        heapq.heappush(heap, [low[0] + high[0]] + low[1:] + high[1:])
        print(len(heap))
        print(heap)
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))


def decode_huffman(root, s):
    ans = ''
    curr = root
    for i in range(0, len(s)):
        if s[i] == '0':
            curr = curr.left
        else:
            curr = curr.right
        if not curr.left and not curr.right:
            ans = ans + curr.data
            curr = root
    return ans


def generate_frequency(s) -> dict:
    frequency = defaultdict(int)
    for character in s:
        frequency[character] += 1
    return frequency


if __name__ == "__main__":

    s = "ABRACADABRA"
    huffman_encoded = encode_huffman(s)
    print(huffman_encoded)




