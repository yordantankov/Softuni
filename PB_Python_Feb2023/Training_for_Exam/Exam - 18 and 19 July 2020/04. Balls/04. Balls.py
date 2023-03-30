import math

balls  = int(input())
total_points = 0
red = 0
orange = 0
yellow = 0
white = 0
others = 0
divide_count = 0

for i in range(0, balls):
    color = input()

    if color == "red":
        red+= 1
        total_points += 5
    elif color == "orange":
        orange += 1
        total_points += 10
    elif color == "yellow":
        yellow += 1
        total_points += 15
    elif color == "white":
        white += 1
        total_points += 20
    elif color == "black":
        total_points = math.floor(total_points / 2)
        divide_count += 1
    else:
        others += 1

print(f'Total points: {total_points}')
print(f'Red balls: {red}')
print(f'Orange balls: {orange}')
print(f'Yellow balls: {yellow}')
print(f'White balls: {white}')
print(f'Other colors picked: {others}')
print(f'Divides from black balls: {divide_count}')