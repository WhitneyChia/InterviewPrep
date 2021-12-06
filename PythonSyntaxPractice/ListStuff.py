from functools import reduce

print("\n")
print("Get the product of a list of numbers")
example = [1, 2, 4, 5, 10]
print(reduce(lambda x, y: x * y, example))


print("\n")
print("Get the sum of a list of numbers")
example = [1, 2, 4, 5, 10]
print(sum(example))
print(reduce(lambda x, y: x + y, example))

print("\n")
print("Remove an element from a list and then insert it back")
example = [1, 2, 4, 5, 10]
example.remove(4)
print(example)
example.insert(2, 4)
print(example)

example = [(0, 10), (99, 1), (10, 5), (9, 4)]
example.remove((99, 1))
print(example)
example.insert(1, (99, 1))
print(example)

print("\n")
print("Get the index of a particular element")
example = [1, 2, 4, 5, 10]
print(example.index(10))

print("\n")
print("Sort a list ascending")
example = [10, 2, 4, 5, 10]
print(sorted(example))
example.sort()
print(example)

print("\n")
print("Sort a list descending")
example = [10, 2, 4, 5, 10]
print(sorted(example, reverse=True))
example.sort(reverse=True)
print(example)

print("\n")
print("Given a list of tuples, sort by the first element")
example = [(0, 10), (99, 1), (10, 5), (9, 4)]

# sorted gives you a new list, the original remains intact
new_sorted_list = sorted(example, key=lambda x: x[0])
print(new_sorted_list)
print(example)

# .sort modifies the list in place
example.sort(key=lambda x: x[0])
print(example)


print("\n")
print("Given a list of tuples, sort by the second element")
example = [(0, 10), (99, 1), (10, 5), (9, 4)]
new_sorted_list = sorted(example, key=lambda x: x[1])
print(new_sorted_list)
print(example)

# .sort modifies the list in place
example.sort(key=lambda x: x[1])
print(example)


print("\n")
print("Given a list of tuples, sort by the first and then the second element")
example = [(10, 10), (99, 1), (10, 5), (9, 4)]
new_sorted_list = sorted(example, key=lambda x: (x[0], x[1]))
print(new_sorted_list)
print(example)

# .sort modifies the list in place
example.sort(key=lambda x: (x[0], x[1]))
print(example)


print("\n")
print("Given a list of tuples, sort by the first and then the second element desc")
example = [(10, 10), (99, 1), (10, 5), (9, 4)]
new_sorted_list = sorted(example, key=lambda x: (x[0], -x[1]))
print(new_sorted_list)
print(example)

# .sort modifies the list in place
example.sort(key=lambda x: (x[0], -x[1]))
print(example)


print("\n")
print("Given two lists of sorted arrays, combine into one sorted array nlogn way")
example_1 = [1, 2, 3, 4, 5]
example_2 = [1, 1, 2, 3, 30]
solution = sorted(example_1 + example_2)
print(solution)


print("\n")
print("Given two lists of sorted arrays, combine into one sorted array n+m way, two pointers")
example_1 = [1, 2, 3, 4, 5]
example_2 = [1, 1, 2, 3, 30, 99]

example_1_pointer = 0
example_2_pointer = 0

solution = []

while example_1_pointer < len(example_1) and example_2_pointer < len(example_2):
    if example_1[example_1_pointer] <= example_2[example_2_pointer]:
        solution.append(example_1[example_1_pointer])
        example_1_pointer += 1
    else:
        solution.append(example_2[example_2_pointer])
        example_2_pointer += 1

if example_1_pointer < len(example_1):
    solution.extend(example_1[example_1_pointer:])
elif example_2_pointer < len(example_2):
    solution.extend(example_2[example_2_pointer:])

print(solution)


print("\n")
print("Binary Search")


def binary_search(sorted_list, target):
    left, right = 0, len(sorted_list) - 1

    while left <= right:
        mid = (right + left) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return False


example_1 = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 30, 99]
print(binary_search(example_1, 14))
print(binary_search(example_1, 7))


print("\n")
print("iterating through a list of tuples")

example = [(0, 10), (99, 1), (10, 5), (9, 4)]

for (k, v) in example:
    print(k, v)