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


