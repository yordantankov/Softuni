waiting_people = int(input())
state_of_lift = list(map(int, input().split()))
all_spots = 4 * len(state_of_lift)

while waiting_people > 0:
    
    if sum(state_of_lift) == all_spots:
        break

    for current_lift in state_of_lift:
        current_index = state_of_lift.index(current_lift)

        if current_lift == 4:
            continue

        if waiting_people == 0 :
            break

        else:
           while current_lift < 4:
              current_lift += 1
              waiting_people -= 1
              if waiting_people == 0:
                  break
           state_of_lift[current_index] = current_lift


if all_spots > sum(state_of_lift) and waiting_people == 0:
    print("The lift has empty spots!")
    for element in state_of_lift:
        print(element, end=" ")

elif waiting_people > 0:
    print(f"There isn't enough space! {waiting_people} people in a queue!")
    for element in state_of_lift:
        print(element, end=" ")

else:
    for element in state_of_lift:
        print(element, end=" ")