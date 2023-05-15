import math

hengt_wall = int(input())
widht_wall = int(input())
percent_not_paint = int(input())

walls_for_paint = hengt_wall * widht_wall * 4
walls_for_paint -= math.ceil(walls_for_paint * percent_not_paint / 100)
while True:
    liters_paint = input()
    if liters_paint == "Tired!":
        break

    liters_paint = int(liters_paint)

    walls_for_paint -= liters_paint

    if walls_for_paint < 0:
        diff = abs(walls_for_paint)
        print(f'All walls are painted and you have {diff} l paint left!')
        exit()

    if walls_for_paint == 0:
        print("All walls are painted! Great job, Pesho!")
        exit()



print(f'{walls_for_paint} quadratic m left.')