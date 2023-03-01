import math

tournaments_qty = int(input())
starting_points = int(input())
win_count = 0
average_points = 0
for i in range (0, tournaments_qty):
    succes_type = input()
    if succes_type == "W":
        starting_points += 2000
        win_count += 1
        average_points += 2000
    elif succes_type == "F":
        starting_points += 1200
        average_points += 1200
    elif succes_type == "SF":
        starting_points += 720
        average_points += 720

print(f'Final points: {starting_points}')
print(f'Average points: {math.floor(average_points / tournaments_qty)}')
print(f'{(win_count / tournaments_qty) * 100 :.2f}%')