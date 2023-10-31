rows = int(input())
matrix = []

for row in range(rows):
    col = [int(x) for x in input().split(", ")]
    matrix.append(col)

new_matrix = []
for element in matrix:
    for el in element:
        new_matrix.append(el)

print(new_matrix)
