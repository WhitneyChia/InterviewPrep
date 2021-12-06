
print("\n")
print("Transpose a Matrix")


def transpose(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]


print("Given: [[1, 2], [3, 4]]")
test = [[1, 2], [3, 4]]
transpose(test)
print(f"After transposed: {test}")


print("\n")
print("Reflect a Matrix")


def reflect(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n // 2):
            matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]


print("Given: [[1, 2], [3, 4]]")
test = [[1, 2], [3, 4]]
reflect(test)
print(f"After reflected: {test}")
