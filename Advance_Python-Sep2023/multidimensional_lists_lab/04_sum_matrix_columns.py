rows, columns = map(int, input().split(', '))

matrix = []

for _ in range(rows):
    row_elements = list(map(int, input().split()))
    matrix.append(row_elements)

column_sums = [0] * columns
for col in range(columns):
    for row in range(rows):
        column_sums[col] += matrix[row][col]


for sum_val in column_sums:
    print(sum_val)
