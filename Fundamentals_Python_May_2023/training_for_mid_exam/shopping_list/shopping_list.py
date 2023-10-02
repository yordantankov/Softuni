

given_list = input().split("!")
command = input()
while command != "Go Shopping!":
    command = command.split()

    if command [0] == "Urgent":
        item_from_command = command[1]
        if item_from_command not in given_list:
            given_list.insert(0, item_from_command)
        else:
            command = input()
            continue

    elif command[0] == "Unnecessary":
        item_from_command = command[1]
        if item_from_command in given_list:
            given_list.remove(item_from_command)
        else:
            command = input()
            continue

    elif command[0] == "Correct":
        old_item, new_item = command[1], command[2]

        if old_item in given_list:
           index = given_list.index(old_item)
           given_list.insert(index, new_item)
           given_list.remove(old_item)

        else:
            command = input()
            continue


    elif command[0] == "Rearrange":
        item = command[1]
        if item in given_list:
            given_list.remove(item)
            given_list.append(item)
        else:
            command = input()
            continue

    command = input()

print(", ".join(given_list))