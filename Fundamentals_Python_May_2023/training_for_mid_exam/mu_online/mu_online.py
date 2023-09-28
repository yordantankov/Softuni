rooms_list = input().split("|")
current_healt = 100
bitcoins = 0
best_room = 0
for room in rooms_list:
    room = room.split()
    action, number = room[0], int(room[1])

    if action == "potion":
        diff = 100 - current_healt
        current_healt += number
        if current_healt > 100:
            number = diff
            current_healt = 100

        best_room += 1
        print(f"You healed for {number} hp.")
        print(f"Current health: {current_healt} hp.")


    elif action == "chest":
        print(f"You found {number} bitcoins.")
        bitcoins+= number
        best_room += 1

    else:
        current_healt -= number
        best_room += 1
        if current_healt > 0:
            print(f"You slayed {action}.")
        else:
            print(f"You died! Killed by {action}.")
            print(f'Best room: {best_room}')
            exit()

print("You've made it!")
print(f"Bitcoins: {bitcoins}")
print(f"Health: {current_healt}")