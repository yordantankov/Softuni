rows = int(input())
matrix = []

for row in range(rows):
    matrix.append(input())

searching_item = input()
is_found = False
for row in range(rows):
    for col in range(rows):
        if matrix[row][col] == searching_item:
            is_found = True
            row_position = row
            col_position = col
            break
        if is_found:
            break
if not is_found:
    print(f"{searching_item} does not occur in the matrix")
else:
    print(f"({row_position}, {col_position})")
