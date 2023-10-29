rows, cols = [int(x) for x in input().split(", ")]
sum_nums = 0
matrix = []

for row in range(rows):
    lines = [int(x) for x in input().split(", ")]
    sum_nums += sum(lines)
    matrix.append(lines)

print(sum_nums)
print(matrix)
