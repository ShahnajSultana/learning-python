matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
matrix[1][2] = 20 #modify the value
print(matrix[1][2])

print("\n")
for row in matrix: #one by one list
    for item in row:
        print(item)
