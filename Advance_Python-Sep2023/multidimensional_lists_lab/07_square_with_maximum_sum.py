rows, columns = map(int, input().split(', '))
matrix = []

for _ in range(rows):
    row_elements = list(map(int, input().split(', ')))
    matrix.append(row_elements)

max_sum = float('-inf')
max_submatrix = []

for i in range(rows - 1):
    for j in range(columns - 1):
        submatrix_sum = matrix[i][j] + matrix[i][j + 1] + matrix[i + 1][j] + matrix[i + 1][j + 1]
        if submatrix_sum > max_sum:
            max_sum = submatrix_sum
            max_submatrix = [[matrix[i][j], matrix[i][j + 1]], [matrix[i + 1][j], matrix[i + 1][j + 1]]]

print('\n'.join([' '.join(map(str, row)) for row in max_submatrix]))
print(f'{max_sum}')
