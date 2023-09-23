neighborhood_list = list(map(int, input().split("@")))
cupids_index = 0
current_index = 0
last_index = 0
command = input().split()
while command[0] != "Love!":
    index_to_jump = int(command[1])
    current_index += index_to_jump
    last_index = current_index

    if current_index > (len(neighborhood_list)-1):
        current_index = 0
        last_index = 0
    if neighborhood_list[current_index] > 0:
        neighborhood_list[current_index] -= 2
        if neighborhood_list[current_index] == 0:
            print(f"Place {last_index} has Valentine's day.")
            command = input().split()
            continue

    elif neighborhood_list[current_index] <= 0:
        print(f"Place {last_index} already had Valentine's day.")
        command = input().split()
        continue

    command = input().split()

print(f"Cupid's last position was {last_index}.")
count_fail = 0
for element in neighborhood_list:
    if element != 0:
        count_fail += 1

if count_fail > 0 :
    print(f'Cupid has failed {count_fail} places.')
else:
    print("Mission was successful.")
