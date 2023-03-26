capacity_of_trunk = float(input())
suit_count = 0
suitcase_count = 0
while True:
    suitcase = input()
    if suitcase == "End":
        print('Congratulations! All suitcases are loaded!')
        break
    suit_count += 1
    suitcase = float(suitcase)
    if suit_count == 3 :
        suit_count = 0
        suitcase += suitcase * 0.10

    capacity_of_trunk -= suitcase
    if capacity_of_trunk <= 0:
        print('No more space!')
        break
    suitcase_count+= 1

print(f'Statistic: {suitcase_count} suitcases loaded.')


