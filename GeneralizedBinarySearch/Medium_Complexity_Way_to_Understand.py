"""
Slightly more complex conditions, the binary search has small modifications
"""


def min_rate_something_is_successful(nums, within_d_days):
    """
    The set up here is at the rate for d days, what is the min rate we can finish the nums.
    If we treat each num in nums as one unit, the min rate must be max nums.
    Our search space can be 0, and sum of nums, since we know sum of nums definitely works.
    """
    def condition(rate):
        total = 0
        days = 1
        for num in nums:
            total += num
            if total > rate:
                total = num
                days += 1
                if days > within_d_days:
                    return False
        return True

    left, right = 0, sum(nums)
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left


if __name__ == "__main__":

    nums = [1, 2, 3, 4, 5, 6, 7]
    within_d_days = 3
    expected_result = 11
    # Explanation: We need to finish our something within 3 days and we have sum(nums) to do.
    # At 11, the first day we can do [1, 2, 3, 4], second day we can do [5, 6], third day we can do [7]
    # Anything greater than 11, for sure will also work
    # At 10, the first day we can do [1, 2, 3, 4] second day we can only do [5],
    # third day we can only do [6], [7] needs a 4th day
    # The min rate here is 11 that satisfies our condition
    assert min_rate_something_is_successful(nums, within_d_days) == expected_result

    # This still works even if it isn't sorted because of our condition function
    nums = [7, 6, 5, 4, 3, 2, 1]
    within_d_days = 3
    expected_result = 11
    # Explanation: We need to finish our something within 3 days and we have sum(nums) to do.
    # At 11, the first day we can do [7], second day we can do [5, 6], third day we can do [1, 2, 3, 4]
    # Anything greater than 11, for sure will also work
    # At 10, the first day we can do [7] second day we can only do [6], third day we can only do [5, 4],
    # [3, 2, 1] needs a 4th day
    # The min rate here is 11 that satisfies our condition
    assert min_rate_something_is_successful(nums, within_d_days) == expected_result




