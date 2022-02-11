
# Traversing an array in Reverse
print("Traversing an array in reverse")
test = [1, 2, 3, 4, 5]
print(test)
for i in range(len(test) - 1, -1, -1):
    print(test[i])
print("\n")

# Traversing an array from both sides
print("Traversing an from both sides")
test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(test)
left, right = 0, len(test) - 1
while left <= right:
    print(test[left], test[right])
    left += 1
    right -= 1
print("\n")


# Partitioning Arrays
print("Partitioning an array, move all zeroes to the left")
test = [1, 0, 3, 0, 5, 0, 7, 0, 9, 0]
left_partition = 0
print(test)
for i in range(len(test)):
    if test[i] == 0:
        test[left_partition], test[i] = test[i], test[left_partition]
        left_partition += 1

print(test)
print("\n")


# Partitioning Arrays
print("Partitioning an array, move all zeroes to the right")
test = [1, 0, 3, 0, 5, 0, 7, 0, 9, 0]
right_partition = len(test) - 1
print(test)
for i in range(len(test) - 1, -1, -1):
    if test[i] == 0:
        test[right_partition], test[i] = test[i], test[right_partition]
        right_partition -= 1
print(test)
print("\n")

# Partitioning Arrays
print("Partitioning an array, dutch national flag")
test = [0, 2, 1, 2, 0, 1, 0, 2, 0]

left, mid, right = 0, 0, len(test) - 1

print(test)
while mid <= right:
    if test[mid] == 0:
        test[mid], test[left] = test[left], test[mid]
        mid += 1
        left += 1
    elif test[mid] == 2:
        test[mid], test[right] = test[right], test[mid]
        right -= 1
    else:
        mid += 1

print(test)
print("\n")


# Kadane's Algorithm
print("Maximum Subarray - Kadane's Algorithm")
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(nums)
current_subarray_max = overall_maximum = nums[0]

for i in range(1, len(nums)):
    if current_subarray_max < 0:
        current_subarray_max = nums[i]
    else:
        current_subarray_max = nums[i] + current_subarray_max
    overall_maximum = max(current_subarray_max, overall_maximum)

print(overall_maximum)