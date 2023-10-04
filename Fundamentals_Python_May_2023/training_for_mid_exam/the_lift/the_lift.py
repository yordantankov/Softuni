waiting_people = int(input())
all_people = waiting_people
state_of_lift = input().split()
avaible_space_on_lift = []
spots_not_avaible = 0

for avaible_space in state_of_lift:
    avaible_space_on_lift.append(int(avaible_space))

now_space_in_lift = []

while True:
    if waiting_people == 0:
        break
    if len(now_space_in_lift) == len(avaible_space_on_lift):
        if waiting_people > 0:
           break

    for curent_index in avaible_space_on_lift:
        if curent_index < 4:
            if waiting_people == 0:
                break
            now_index = curent_index
            spots_not_avaible += now_index
            while now_index < 4:
                if waiting_people > 0 :
                    now_index += 1
                    spots_not_avaible += 1
                    waiting_people -= 1
                    if now_index == 4:
                        now_space_in_lift.append(now_index)
                        break
                elif waiting_people == 0:
                    now_space_in_lift.append(now_index)
                    break
        elif curent_index == 4:
            spots_not_avaible += curent_index
            now_space_in_lift.append(curent_index)
            continue

all_spots = 4 * len(now_space_in_lift)

if all_spots - spots_not_avaible > waiting_people:
    if waiting_people == 0:
        print('The lift has empty spots!')
        for num in now_space_in_lift:
           print(num, end=" ")

elif waiting_people > all_spots - spots_not_avaible:
    print(f"There isn't enough space! {waiting_people} people in a queue!")
    for num in now_space_in_lift:
        print(num, end=" ")

elif waiting_people == 0:
    for num in now_space_in_lift:
        print(num, end=" ")