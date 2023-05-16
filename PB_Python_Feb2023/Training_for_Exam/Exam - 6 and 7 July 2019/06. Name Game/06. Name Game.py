import sys
highest_points = -sys.maxsize
points = 0
top_player = ''
while True:
    name = input()
    points = 0
    if name == "Stop":
        break

    for i in range(len(name)):
        number = int(input())
        char_letter = ord(name[i])

        if number == char_letter:
              points += 10
        else:
              points += 2

        if points >= highest_points:
            highest_points = points
            top_player = name

print(f"The winner is {top_player} with {highest_points} points!")