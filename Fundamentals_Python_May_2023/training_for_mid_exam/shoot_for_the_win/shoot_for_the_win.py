
targets_list = list(map(int, input().split()))
shoot_count = 0
while True:
    command = input()
    if command == 'End':
        break
    current_index_value = 0
    command = int(command)
    if command <= len(targets_list)-1 and command >= 0:

        if targets_list[command] != -1:
            current_index_value = targets_list[command]
            targets_list[command] = -1
            shoot_count += 1

            for index ,num in enumerate(targets_list):
                if num != -1 and num > current_index_value:
                    targets_list[index] -= current_index_value
                elif num != -1 and num <= current_index_value:
                    targets_list[index] += current_index_value
    else:
        continue

print(f'Shot targets: {shoot_count} ->', end=" ")
for num in targets_list:
    print(num, end=" ")