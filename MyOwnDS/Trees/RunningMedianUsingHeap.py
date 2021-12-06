"""
Using the Python's heapq module.
Find the running median of a stream of numbers
"""

import heapq


def get_median(min_heap: heapq, max_heap: heapq):
    # I have an odd total amount of numbers, my median is the root of the larger one
    if len(min_heap) > len(max_heap):
        return min_heap[0]
    elif len(min_heap) < len(max_heap):
        return -1 * max_heap[0]
    # I have an even total amount of numbers, my median is the average of both roots
    else:
        return (min_heap[0] + -1 * max_heap[0]) / 2.0


def add(num, min_heap, max_heap):
    # If empty, then just add it to the min heap
    if len(min_heap) + len(max_heap) < 1:
        heapq.heappush(min_heap, num)
        return

    median = get_median(min_heap, max_heap)
    if num > median:
        heapq.heappush(min_heap, num)
    else:
        # heapq only support min heaps, so we simply negate the num
        heapq.heappush(max_heap, -1 * num)


def rebalance(min_heap, max_heap):
    """ We only allow one heap to be greater than the other by 1, else need to rebalance """
    if len(min_heap) > len(max_heap) + 1:
        root = heapq.heappop(min_heap)
        heapq.heappush(max_heap, -1 * root)
    elif len(max_heap) > len(min_heap) + 1:
        root = -1 * heapq.heappop(max_heap)
        heapq.heappush(min_heap, root)


def print_median(min_heap, max_heap):
    print(get_median(min_heap, max_heap))


def running_median(stream):
    min_heap = []
    max_heap = []
    for num in stream:
        add(num, min_heap, max_heap)
        rebalance(min_heap, max_heap)
        print_median(min_heap, max_heap)


if __name__ == "__main__":

    test = [2, 1, 5, 7, 2, 0, 5]

    running_median(test)
