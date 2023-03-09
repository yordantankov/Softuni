widht_space = int(input())
lenght_space = int(input())
height_space = int(input())

free_space = widht_space * lenght_space * height_space

while True:
    command = input()
    if command == "Done":
        break

    command = int(command)
    free_space -= command

    if free_space < 0 :
        diff = abs(free_space)
        print(f'No more free space! You need {diff} Cubic meters more.')
        exit()

print(f'{free_space} Cubic meters left.')