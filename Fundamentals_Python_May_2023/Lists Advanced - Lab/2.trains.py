trains = [0] * int(input())
command = input().split()

while True:

    if command == ['End']:
       break

    if command[0] == "add":
        command[1] = int(command[1])
        trains[-1] += command [1]

    elif command[0] == "insert":
        index = int(command[1])
        people = int(command[2])
        trains[index]+= people

    elif command[0] == "leave":
        index = int(command[1])
        people = int(command[2])
        trains[index] -= people
    command = input().split()

print(trains)





