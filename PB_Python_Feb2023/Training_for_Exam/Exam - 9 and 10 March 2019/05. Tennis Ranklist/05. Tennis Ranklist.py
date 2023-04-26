import math
count_tournamest = int(input())
starting_points = int(input())
win_tournamets = 0
points = 0
for i in range(count_tournamest):
    etap = input()

    if etap == "W":
        points += 2000
        starting_points += 2000
        win_tournamets += 1
    elif etap == "F":
        points += 1200
        starting_points += 1200
    elif etap == "SF":
        points += 720
        starting_points += 720

print(f"Final points: {starting_points}")
average = math.floor(points / count_tournamest)
print(f"Average points: {average}")
print(f'{win_tournamets / count_tournamest * 100 :.2f}%')