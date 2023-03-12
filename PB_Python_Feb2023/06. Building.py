floors = int(input())
rooms = int(input())

for i in range (floors , 0 , -1):

    for room in range (rooms):

        if i == floors:
            print(f'L{i}{room}', end=" ")
        else:
            if i % 2 == 0:
               print(f'O{i}{room}', end= " " )

            else:
               print(f'A{i}{room}', end= " ")
    print("")
