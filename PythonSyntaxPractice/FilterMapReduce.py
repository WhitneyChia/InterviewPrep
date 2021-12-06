from functools import reduce

print("\n")
print("Filter list for value")
example = [1, 2, 4, 5, 10]
print(list(filter(lambda x: x == 5, example)))


print("\n")
print("Filter string for value")
example = "Whitney"
print(list(filter(lambda x: x == "W", example)))


print("\n")
print("Filter string for is alphanumeric")
example = "Whi$tn&ey"
print(list(filter(lambda x: x.isalnum(), example)))


print("\n")
print("Map to change to lower")
example = "WHITNEY"
print(list(map(lambda x: x.lower(), example)))