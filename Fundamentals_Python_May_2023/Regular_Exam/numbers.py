given_list = list(map(int, input().split()))

command = input()

while command != "Finish":
    command = command.split()
    action = command[0]

    if action == "Add":
         value = int(command[1])
         given_list.append(value)

    elif action == "Remove":
        value = int(command[1])
        if value in given_list:
            given_list.remove(value)

    elif action == "Replace":
        value = int(command[1])
        replacement = int(command[2])
        if value in given_list:
            index = given_list.index(value)
            given_list[index] = replacement

    elif action == "Collapse":
        value = int(command[1])
        given_list = list(num for num in given_list if num >= value)


    command = input()

for element in given_list:
    print(element, end=" ")