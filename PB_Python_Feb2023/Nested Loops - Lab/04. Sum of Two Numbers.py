entry_interval = int(input())
end_interval = int(input())
magic_num = int(input())
count_combination = 0

for i in range(entry_interval, end_interval + 1 ):
    for x in range (entry_interval, end_interval + 1 ):
        combination = i + x
        count_combination += 1
        if combination == magic_num:
            print(f'Combination N:{count_combination} ({i} + {x} = {magic_num})')
            exit()

print(f'{count_combination} combinations - neither equals {magic_num}')