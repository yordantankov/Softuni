matrix = []
rows = int(input())

for row in range(rows):
    col = [int(x) for x in input().split(", ") if int(x) % 2 == 0]
    matrix.append(col)

print(matrix)
