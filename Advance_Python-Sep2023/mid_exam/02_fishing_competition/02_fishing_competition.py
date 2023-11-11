n = int(input())
matrix = []

for _ in range(n):
    row = input()
    matrix.append(list(row))

ship_row, ship_col = None, None
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'S':
            matrix[i][j] = '-'
            ship_row, ship_col = i, j
            break

quota = 20
fish_caught = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
while True:
    comm = input()
    if comm == "collect the nets":
        if fish_caught >= quota:
            print("Success! You managed to reach the quota!")
        else:
            lack_of_fish = quota - fish_caught
            print(
                f"You didn't catch enough fish and didn't reach the quota! You need {lack_of_fish} tons of fish more.")
        if fish_caught > 0:
            print(f"Amount of fish caught: {fish_caught} tons.")
        matrix[ship_row][ship_col] = 'S'
        break
    moves = directions.get(comm)
    if moves:
        new_row = (ship_row + moves[0]) % n
        new_col = (ship_col + moves[1]) % n

        if 0 <= new_row < n and 0 <= new_col < n:
            pass
        else:
            if not 0 <= new_row:
                new_row = n - 1
            elif not new_row < n:
                new_row = 0
            elif not 0 <= new_col:
                new_col = n - 1
            elif not new_col < n:
                new_col = 0
        if matrix[new_row][new_col] == 'W':
            print(
                f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{new_row},{new_col}]")
            exit(0)
        cell_value = matrix[new_row][new_col]
        if cell_value != '-':
            fish_caught += int(cell_value)
            matrix[new_row][new_col] = '-'
        ship_row, ship_col = new_row, new_col

for i in range(n):
    print("".join(matrix[i]))
