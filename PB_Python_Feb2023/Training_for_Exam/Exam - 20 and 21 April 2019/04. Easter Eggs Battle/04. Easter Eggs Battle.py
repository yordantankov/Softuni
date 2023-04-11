count_eggs_1_player = int(input())
count_eggs_2_player = int(input())

while True:
    command = input()
    if command == "End":
        break

    if command == "one":
        count_eggs_2_player -= 1
        if count_eggs_2_player == 0:
            print(f"Player two is out of eggs. Player one has {count_eggs_1_player} eggs left.")
            exit()

    elif command == "two":
        count_eggs_1_player -= 1
        if count_eggs_1_player == 0:
            print(f"Player one is out of eggs. Player two has {count_eggs_2_player} eggs left.")
            exit()

print(f"Player one has {count_eggs_1_player} eggs left.")
print(f"Player two has {count_eggs_2_player} eggs left.")