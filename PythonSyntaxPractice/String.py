print("\n")
test = "Whitney Chia and Mandy Cheuk"

print(test.split())


def sum67(nums):
    summation = 0
    i = 0

    while i < len(nums):
        if nums[i] != 6:
            summation += nums[i]
            i += 1
        else:
            i = nums[i + 1:].index(7) + i + 2

    return summation


test = [1, 2, 2, 6, 99, 99, 7]

print(sum67(test))