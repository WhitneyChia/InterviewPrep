from functools import reduce

print("\n")
print("Get the product of all values in a dictionary")
example = {"a": 10, "b": 20, "c": 10}
print(reduce(lambda x, y: x * y, example.values()))

print("\n")
print("Concatenate all strings keys in a dictionary")
example = {"a": 10, "b": 20, "c": 10}
print(reduce(lambda x, y: x + y, example.keys()))

print("\n")
print("Remove a key from a dictionary")
example = {"a": 10, "b": 20, "c": 10}
del example["a"]
print(example)

print("\n")
print("Remove a value from a dictionary")
example = {"a": 10, "b": 20, "c": 10}
example = {k: v for k, v in example.items() if v != 10}
print(example)


import collections

ans = collections.defaultdict(list)

print(ans)