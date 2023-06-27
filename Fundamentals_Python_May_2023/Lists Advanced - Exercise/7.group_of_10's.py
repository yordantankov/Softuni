given_numbers = [int(num) for num in input().split(", ")]

current_group_of_numbers = 10
while given_numbers:
    current_list_to_print = []
    for number in given_numbers:
        if int(number) <= current_group_of_numbers:
            current_list_to_print.append(int(number))
    print(f"Group of {current_group_of_numbers}'s: {current_list_to_print}")
    current_group_of_numbers+= 10
    given_numbers = [num for num in given_numbers if num not in current_list_to_print]


