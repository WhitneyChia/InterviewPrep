"""
The trick here is creating a search space and then finding
either the min value where some condition is True
or the max value where some condition is True
"""
from typing import List


def find_first_occurrence(nums: List, target: int):
    """
    for example, if we have a list of ints that can contain dupes.
    I want the first occurrence.
    My condition would be, the value == target value
    It is the way I search and return that would handle first occurrence
    """
    def condition(num):
        return num >= target

    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if condition(nums[mid]):
            right = mid
        else:
            left = mid + 1
    return left


def find_last_occurrence(nums: List, target: int):
    """
    for example, if we have a list of ints that can contain dupes.
    I want the last occurrence.
    My condition would be, the value >= target value
    It is the way I search and return that would handle first occurrence
    """

    def condition(num):
        return num > target

    left, right = 0, len(nums) - 1

    # Here we do <=
    while left <= right:
        mid = left + (right - left) // 2
        # Because of our condition, we actually want the search to continue, the one to the left
        if condition(nums[mid]):
            right = mid - 1
        else:
            left = mid + 1
    return right


"""
Let's have a little more complex of a scenario.
We want the smallest number within a range, or the biggest number within a range.
In this case, let's say 5 - 20
You have to binary search this two times actually. So we'll run smallest and then biggest
"""


def find_smallest_number_in_range(nums):
    def condition(num):
        return num > 5

    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if condition(nums[mid]):
            right = mid
        else:
            left = mid + 1
    return left


def find_largest_number_in_range(nums):
    def condition(num):
        return num < 20

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if not condition(nums[mid]):
            right = mid - 1
        else:
            left = mid + 1
    return right


if __name__ == "__main__":

    nums = [-14, -10, 2, 108, 108, 108, 285, 285, 285, 401]
    target = 108
    expected_result = 3
    assert find_first_occurrence(nums, target) == expected_result

    nums = [-14, -10, 2, 108, 108, 108, 285, 285, 285, 401]
    target = 108
    expected_result = 5
    assert find_last_occurrence(nums, target) == expected_result

    nums = [100, 100, 100, 100, 100]
    target = 100
    expected_result = 0
    assert find_first_occurrence(nums, target) == expected_result

    nums = [100, 100, 100, 100, 100]
    target = 100
    expected_result = 4
    assert find_last_occurrence(nums, target) == expected_result

    nums = [1, 2, 3, 4, 5, 7, 8, 19]
    expected_result = 5
    assert find_smallest_number_in_range(nums) == expected_result

    nums = [1, 2, 3, 4, 5, 7, 8, 19]
    expected_result = 7
    assert find_largest_number_in_range(nums) == expected_result

    nums = [1, 2, 3, 4, 5, 7, 8, 19, 100, 101]
    expected_result = 7
    assert find_largest_number_in_range(nums) == expected_result
