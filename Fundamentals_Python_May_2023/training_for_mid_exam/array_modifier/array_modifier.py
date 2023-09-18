def swap(the_list, first_index_from_com, second_index_from_com):
    if index_1_from_command <= len(the_list) and index_2_from_command <= len(the_list):
        the_list[first_index_from_com], the_list[second_index_from_com] = the_list[second_index_from_com], the_list[
          first_index_from_com]
        return the_list


def multiply(the_list, first_index_from_com, second_index_from_com):
    if index_1_from_command <= len(the_list) and index_2_from_command <= len(the_list):
        the_list[first_index_from_com] = the_list[first_index_from_com] * the_list[second_index_from_com]
        return the_list


def decrease(the_list):
    the_list = list(map(int, the_list))
    for element in range(len(the_list)):
        the_list[element] -= 1
    return the_list


given_list = input().split()
given_list = list(map(int, given_list))
command = input()
result = []
while command != "end":
    if command == "decrease":
        given_list = decrease(given_list)

    else:
        command = command.split()
        index_1_from_command, index_2_from_command = command[1], command[2]
        index_1_from_command, index_2_from_command = int(index_1_from_command), int(index_2_from_command)
        action = command[0]

        if action == 'swap':
            result = swap(given_list, index_1_from_command, index_2_from_command)

        elif action == "multiply":
            result = multiply(given_list, index_1_from_command, index_2_from_command)

    command = input()

print(*result, sep=", ")
