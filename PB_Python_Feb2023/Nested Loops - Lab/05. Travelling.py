money = 0

while True:
    destination = input()

    if destination == "End":
        exit()
    budjet_needed = float(input())

    while True:
        money_save = float(input())
        money += money_save

        if money >= budjet_needed:
            print(f'Going to {destination}!')
            money = 0
            break


