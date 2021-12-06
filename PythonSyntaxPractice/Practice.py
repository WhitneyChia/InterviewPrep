import collections

# Collections Library
print("\n")
print("Default dict example, name and int value")
my_names = collections.defaultdict(int)
my_names["Whitney"] = 38
print(my_names)
print(my_names["Mandy"])

print("\n")
print("Counter Example")
test = "WhitneyChia"
counter = collections.Counter(test)
print(counter)

print("\n")
print("Deque Example")
q = collections.deque(["Whitney", "Mandy", "Kenny"])
right = q.pop()
left = q.popleft()
print(right)  # -> Kenny
print(left)  # -> Whitney


print("\n")
print("Binary Search")


def binary_search(sorted_list, target):
    left = 0
    right = len(sorted_list)

    while left <= right:
        mid = (right + left) // 2
        if sorted_list[mid] == target:
            return mid
        # num is on left side
        elif sorted_list[mid] > target:
            right = mid - 1
        # num is on right side
        else:
            left = mid + 1

    return -1


example_1 = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 30, 99]
print(binary_search(example_1, 14))
print(binary_search(example_1, 7))

