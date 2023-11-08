def collect_tea_party(matrix, alice_position, movements):
    tea_bags_collected = 0

    for movement in movements:
        old_row, old_col = alice_position
        matrix[old_row][old_col] = '*'  # Mark Alice's path with '*'

        if movement == 'up':
            new_row, new_col = old_row - 1, old_col
        elif movement == 'down':
            new_row, new_col = old_row + 1, old_col
        elif movement == 'left':
            new_row, new_col = old_row, old_col - 1
        elif movement == 'right':
            new_row, new_col = old_row, old_col + 1

        if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[new_row]):
            if matrix[new_row][new_col] == 'R':
                return tea_bags_collected, new_row, new_col

            if matrix[new_row][new_col].isdigit():
                tea_bags_collected += int(matrix[new_row][new_col])

            if tea_bags_collected >= 10:
                return tea_bags_collected, new_row, new_col

            alice_position = (new_row, new_col)
        else:
            return tea_bags_collected, old_row, old_col

    return tea_bags_collected, alice_position[0], alice_position[1]


def print_matrix(matrix):
    for row in matrix:
        print(' '.join(row))


n = int(input())
wonderland = [input().split() for _ in range(n)]
alice_row, alice_col = [(i, row.index('A')) for i, row in enumerate(wonderland) if 'A' in row][0]
alice_position = (alice_row, alice_col)

movements = []
try:
    while True:
        movement = input().strip()
        if not movement:
            break
        movements.append(movement)
except EOFError:
    pass

tea_bags_collected, alice_final_row, alice_final_col = collect_tea_party(wonderland, alice_position, movements)

if tea_bags_collected >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

wonderland[alice_final_row][alice_final_col] = '*'
print_matrix(wonderland)
