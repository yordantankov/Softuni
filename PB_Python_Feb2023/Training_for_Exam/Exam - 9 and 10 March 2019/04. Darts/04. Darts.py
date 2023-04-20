player_name = input()
starting_points = 301
fail_shots  = 0
succes_shots = 0
while True:
    place = input()
    if place == "Retire":
        break

    points = int(input())

    if place == "Single":
        if points > starting_points:
            fail_shots += 1
            continue
        starting_points -= points
        succes_shots += 1

    elif place == "Double":
        points *= 2
        if points > starting_points:
            fail_shots += 1
            continue
        starting_points -= points
        succes_shots += 1

    elif place == "Triple":
        points *= 3
        if points > starting_points:
            fail_shots += 1
            continue
        starting_points -= points
        succes_shots += 1

    if starting_points == 0:
        print(f'{player_name} won the leg with {succes_shots} shots.')
        exit()

print(f"{player_name} retired after {fail_shots} unsuccessful shots.")