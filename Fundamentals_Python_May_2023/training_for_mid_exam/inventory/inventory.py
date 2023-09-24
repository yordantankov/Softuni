given_list = input().split(", ")
command = input()

while command != "Craft!":
    action = command.split(" - ")[0]
    item = command.split(" - ")[1]
    if action == "Collect":

        if item not in given_list:
            given_list.append(item)

    elif action == "Drop":
        if item in given_list:
            given_list.remove(item)

    elif action == "Combine Items":
        old_item = item.split(":")[0]
        new_item = item.split(":")[1]

        if old_item in given_list:
            current_index = given_list.index(old_item)
            given_list.insert(current_index+1, new_item)

    elif action == "Renew":
        if item in given_list:
            given_list.remove(item)
            given_list.append(item)


    command = input()

print(", ".join(given_list))