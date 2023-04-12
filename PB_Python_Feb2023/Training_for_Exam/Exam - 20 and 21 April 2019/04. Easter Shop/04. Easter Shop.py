starting_count_eggs = int(input())
sell_eggs = 0

while True:
    command = input()
    if command == "Close":
        break

    if command == "Buy":
        eggs_to_buy = int(input())
        if eggs_to_buy > starting_count_eggs:
            print('Not enough eggs in store!')
            print(f'You can buy only {starting_count_eggs}.')
            exit()
        starting_count_eggs -= eggs_to_buy
        sell_eggs += eggs_to_buy

    elif command == "Fill":
        egg_to_fill = int(input())
        starting_count_eggs += egg_to_fill


print("Store is closed!")
print(f"{sell_eggs} eggs sold.")