n = int(input())
matrix = []
primary_diagonal_sum = 0

for i in range(n):
    row_elements = list(map(int, input().split()))
    matrix.append(row_elements)
    primary_diagonal_sum += matrix[i][i]

print(primary_diagonal_sum)
