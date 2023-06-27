rooms = int(input())
free_chairs = 0
total_people = 0
total_chairs = 0
for room in range(1, rooms + 1):
    seats_info = input().split()
    if len(seats_info[0]) > int(seats_info[1]):
        free_chairs += len(seats_info[0]) - int(seats_info[1])


    elif len(seats_info[0]) < int(seats_info[1]):
        diff =  abs(len(seats_info[0]) - int(seats_info[1]))
        print(f'{diff} more chairs needed in room {room}')

    total_people += int(seats_info[1])
    total_chairs += len(seats_info[0])


if total_chairs >= total_people:
    print(f'Game On, {free_chairs} free chairs left')