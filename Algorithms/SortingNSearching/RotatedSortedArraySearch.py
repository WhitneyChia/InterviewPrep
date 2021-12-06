"""
A sorted array of integers has been rotated an unknown number of times.
Find the index of an element in the array in faster than linear time.
"""


def shifted_array_search(nums, num):
    # First, find where the breaking point is in the shifted array
    mid = len(nums) // 2
    dist = mid // 2

    while True:
        if nums[0] > nums[mid] and nums[mid - 1] > nums[mid]:
            break
        elif dist == 0:
            break
        elif nums[0] <= nums[mid]:
            mid += dist
        elif nums[mid-1] <= nums[mid]:
            mid -= dist
        else:
            break
        dist = dist // 2

    # Now that we have the bottom, we can do binary search as usual, wrapping round the rotation

    low = mid
    high = mid - 1
    dist = len(nums) // 2

    while True:
        if dist == 0:
            return None

        guess_ind = (low + dist) % len(nums)
        guess = nums[guess_ind]

        if guess == num:
            return guess_ind
        if guess < num:
            low = (low + dist) % len(nums)
        if guess > num:
            high = (len(nums) + high - dist) % len(nums)

        dist = dist // 2


if __name__ == "__main__":

    test = [13, 18, 25, 2, 8, 10]
    print(shifted_array_search(test, 8))

    print((3 + 1) % 6)