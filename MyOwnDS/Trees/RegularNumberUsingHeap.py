"""
A regular number in mathematics is defined as one which evenly divides some power of 60.
Equivalently, we can say that a regular number is one whose only prime divisors are 2, 3, 5

Given an integer n, write a program that generates, in order the first n regular numbers
"""

import heapq

def regular_numbers_naive(n):
    # Brute Force, this is n ** 3
    twos = [2 ** i for i in range(n)]
    threes = [3 ** i for i in range(n)]
    fives = [5 ** i for i in range(n)]

    solution = set()
    for two in twos:
        for three in threes:
            for five in fives:
                solution.add(two * three * five)

    return sorted(solution)[:n]


def regular_numbers_heap(n):
    # Using a heap, we can reduce this to nlogn
    # make the root 1
    heap = [1]
    solution = set()

    # Because we can repeat numbers i.e 6, we only want to yield when pop > last
    last = 0
    count = 0

    while count < n:
        x = heapq.heappop(heap)
        if x > last:
            solution.add(x)
            last = x
            count += 1
            heapq.heappush(heap, 2 * x)
            heapq.heappush(heap, 3 * x)
            heapq.heappush(heap, 5 * x)

    return solution


if __name__ == "__main__":

    print(regular_numbers_naive(10))
    print(regular_numbers_heap(10))


