"""
https://leetcode.com/problems/random-pick-with-blacklist/

You are given an integer n and an array of unique integers blacklist. Design an algorithm to pick a random integer
in the range [0, n - 1] that is not in blacklist. Any integer that is in the mentioned range and not
in blacklist should be equally likely to be returned.
Optimize your algorithm such that it minimizes the number of calls to the built-in random function of your language.

Implement the Solution class:
Solution(int n, int[] blacklist) Initializes the object with the integer n and the blacklisted integers blacklist.
int pick() Returns a random integer in the range [0, n - 1] and not in blacklist.
"""
from typing import List
from random import random
from bisect import bisect


class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        blacklist.sort()
        delta = 0
        self.offsets = []
        for v in blacklist:
            self.offsets.append(v - delta)
            delta += 1
        self.randmax = n - delta
        assert (self.randmax >= 1)

    def pick(self) -> int:
        rnd = int(random() * self.randmax)
        ind = bisect(self.offsets, rnd)
        return rnd + ind