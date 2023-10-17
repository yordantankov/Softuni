from collections import deque
water_quantity = int(input())
peoples = deque()
names = input()
while names != "Start":
    peoples.append(names)
    names = input()

while True:
    command = input()
    if command == "End":
        break

    if "refill" in command:
        command = command.split(" ")
        water_quantity += int(command[1])

    else:
        if int(command) <= water_quantity:
            water_quantity -= int(command)
            print(f"{peoples.popleft()} got water")
        else:
            print(f"{peoples.popleft()} must wait")

print(f"{water_quantity} liters left")
