matrix = []
my_position = []
targets = 0

for row in range(5):
    matrix.append(input().split())
    for col in range(5):
        if matrix[row][col] == "A":
            my_position = [row, col]
        elif matrix[row][col] == "x":
            targets += 1

directions = {'left': (0, -1), 'right': (0, 1), 'up': (-1, 0), 'down': (1, 0)}
targets_down = []

n = int(input())

for _ in range(n):
    command = input().split()
    if command[0] == "shoot":
        direction = command[1]  # Updated line: store the direction string
        r = my_position[0] + directions[direction][0]  # Use the direction string as a key
        c = my_position[1] + directions[direction][1]  # Use the direction string as a key

        while 0 <= r < 5 and 0 <= c < 5:
            if matrix[r][c] == "x":
                matrix[r][c] = "."
                targets -= 1
                targets_down.append([r, c])
                break
            r += directions[direction][0]  # Use the direction string as a key
            c += directions[direction][1]  # Use the direction string as a key

        if targets == 0:
            print(f'Training completed! All {len(targets_down)} targets hit.')
            break
        elif command[0] == 'move':
            steps = int(command[2])
            move_direction = command[1]  # Changed variable name
            if move_direction == 'up':
                r = my_position[0] - steps
                c = my_position[1]
            elif move_direction == 'down':
                r = my_position[0] + steps
                c = my_position[1]
            elif move_direction == 'left':
                r = my_position[0]
                c = my_position[1] - steps
            else:
                r = my_position[0]
                c = my_position[1] + steps

    if 0 <= r < 5 and 0 <= c < 5 and matrix[r][c] == ".":
            matrix[r][c] = 'A'
            matrix[my_position[0]][my_position[1]] = "."
            my_position = [r, c]

if targets > 0:
    print(f'Training not completed! {targets} targets left.')

[print(row) for row in targets_down]
