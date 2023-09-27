targets_list = list(map(int, input().split()))

command = input().split()
if_is_valid = True
while command[0] != "End":

    if command [0] == "Shoot":
        index_from_command, power_from_command = int(command[1]), int(command[2])
        if index_from_command in range(len(targets_list)):
            targets_list[index_from_command] -= power_from_command
            if targets_list[index_from_command] <= 0:
                targets_list.pop(index_from_command)

    elif command[0] == "Add":
        index_from_command, value_from_command = int(command[1]), int(command[2])
        if index_from_command in range(len(targets_list)):
            targets_list.insert(index_from_command, value_from_command)
        else:
            print("Invalid placement!")


    elif command[0] == "Strike":
        index_from_command, radius_from_command = int(command[1]), int(command[2])
        radius_before = index_from_command - radius_from_command
        radius_after = index_from_command + radius_from_command

        if index_from_command in range(len(targets_list)):
           if radius_before in range(len(targets_list)):

               if radius_after in range(len(targets_list)):
                  first_part = targets_list[:index_from_command - radius_from_command]
                  second_part = targets_list[index_from_command + radius_from_command+ 1:]
                  targets_list = first_part + second_part
               else:
                   if_is_valid = False

           else:
               if_is_valid = False
        else:
            if_is_valid = False
    if not if_is_valid:
        if_is_valid = True
        print("Strike missed!")

    command = input().split()


print(*targets_list, sep="|")