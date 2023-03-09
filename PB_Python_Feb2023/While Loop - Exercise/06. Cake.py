lenght_cake = int(input())
width_cake = int(input())

cake_size = lenght_cake * width_cake

while True:
    command = input()
    if command == "STOP":
        break

    command = int(command)
    cake_size -= command

    if cake_size < 0:
        diff = abs(cake_size)
        print(f"No more cake left! You need {diff} pieces more.")
        exit()

print(f"{cake_size} pieces are left.")