sea_vacation_count = int(input())
mountain_vacation_count = int(input())
earn = 0

while True:
    type_vacation = input()
    if type_vacation == "Stop":
        break

    if type_vacation == "sea":
        if sea_vacation_count == 0:
            continue
        earn += 680
        sea_vacation_count -= 1
    elif type_vacation == "mountain":
        if mountain_vacation_count == 0:
            continue
        earn += 499
        mountain_vacation_count -= 1

    if sea_vacation_count == 0 and mountain_vacation_count == 0:
        print('Good job! Everything is sold.')
        break

print(f'Profit: {earn} leva.')
