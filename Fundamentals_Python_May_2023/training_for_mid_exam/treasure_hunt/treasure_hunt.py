chest = input().split("|")

command = input()
while command != "Yohoho!":
    command = command.split()
    action = command[0]

    if action == "Loot":
        items = command[1:]
        for item in items:
            if item not in chest:
                chest.insert(0, item)

    elif action == "Drop":
        index = int(command[1])
        if index in range(len(chest)):
            current_item = chest[index]
            chest.remove(current_item)
            chest.append(current_item)


    elif action == "Steal":
        count = int(command[1])
        if count >= len(chest):
            print(", ".join(chest))
            chest = []
        else:
            last_items = len(chest) - count
            print(", ".join(chest[last_items:]))
            chest = chest[0:last_items]


    command = input()

if len(chest) == 0 :
    print("Failed treasure hunt.")

else:
    sum= 0
    for item in chest:
        sum += len(item)
    average = sum / len(chest)
    print(f"Average treasure gain: {average:.2f} pirate credits.")