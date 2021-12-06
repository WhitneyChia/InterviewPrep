from typing import List
from collections import Counter
import heapq

print("\n")
print("Adding to a heap")
heap = [99]
heapq.heappush(heap, 40)
heapq.heappush(heap, 101)

print(heap)


print("\n")
print("Popping from a heap")
heap = [99]
heapq.heappush(heap, 40)
heapq.heappush(heap, 101)

# heap = [40, 99, 101]

priority = heapq.heappop(heap)
print(priority)
print(heap)


print("\n")
print("Converting a list into a heap")
unheaped = [10, 20, 0, 1, 2, 3, 99]
heapq.heapify(unheaped)
print(unheaped)


print("\n")
print("Can convert into heap for heapsort")


def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]


print(heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))


print("\n")
print("Top K most common in a list")


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    # O(1) time
    if k == len(nums):
        return nums

    # 1. build hash map : character and how often it appears
    # O(N) time
    count = Counter(nums)
    # 2-3. build heap of top k frequent elements and
    # convert it into an output array
    # O(N log k) time
    return heapq.nlargest(k, count.keys(), key=count.get)


test = [1, 2, 3, 4, 4, 5, 5]
k = 2
print("Given [1, 2, 3, 4, 4, 5, 5], find the top 2 most frequent")
print(f"Result is: {top_k_frequent(test, k)}")


