numbers_of_move = 0

sequence_of_elements = input().split()


while True:

    command = input()
    if command == 'end':
        break
    command = command.split()
    command = list(map(int, command))
    index_1, index_2 = command[0], command[1]
    numbers_of_move+= 1
    if index_1 < 0 or index_2 < 0:
        for i in range(2):
            sequence_of_elements.insert(len(sequence_of_elements) // 2,"-" + str(numbers_of_move) + "a")
        print("Invalid input! Adding additional elements to the board")

    elif index_1 == index_2:
        for i in range(2):
            sequence_of_elements.insert(len(sequence_of_elements) // 2,"-" + str(numbers_of_move) + "a")
        print("Invalid input! Adding additional elements to the board")
    elif index_1 >= len(sequence_of_elements) or index_2 >= len(sequence_of_elements):
        for i in range(2):
            sequence_of_elements.insert(len(sequence_of_elements) // 2, "-" + str(numbers_of_move) + "a")
        print("Invalid input! Adding additional elements to the board")

    else:
        index_in_list_1 = sequence_of_elements[index_1]
        index_in_list_2 = sequence_of_elements[index_2]

        if index_in_list_2 == index_in_list_1:
            print(f"Congrats! You have found matching elements - {index_in_list_1}!")
            sequence_of_elements.remove(index_in_list_2)
            sequence_of_elements.remove(index_in_list_1)
        else:
            print("Try again!")

    if len(sequence_of_elements) == 0:
        print(f"You have won in {numbers_of_move} turns!")
        exit()

print("Sorry you lose :(")
print(" ".join(sequence_of_elements))
