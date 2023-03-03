num_of_turns = int(input())
points = 0
percent_0_9 = 0
percent_10_19 = 0
percent_20_29 = 0
percent_30_39 = 0
percent_40_50 = 0
invalid_nums = 0

for i in range (0, num_of_turns):
    number = int(input())
    if number >= 0 and number <= 9:
        points += number * 0.20
        percent_0_9 += 1
    elif number >= 10 and number <= 19:
        points += number * 0.30
        percent_10_19 += 1
    elif number >= 20 and number <= 29:
        points += number * 0.40
        percent_20_29 +=1
    elif number >= 30 and number <= 39:
        points += 50
        percent_30_39 += 1
    elif number >= 40 and number <= 50:
        points += 100
        percent_40_50 += 1
    else:
        points /= 2
        invalid_nums += 1

print(f'{points :.2f}')
print(f'From 0 to 9: {percent_0_9 / num_of_turns * 100 :.2f}%')
print(f'From 10 to 19: {percent_10_19 / num_of_turns * 100 :.2f}%')
print(f'From 20 to 29: {percent_20_29 / num_of_turns * 100 :.2f}%')
print(f'From 30 to 39: {percent_30_39 / num_of_turns * 100 :.2f}%')
print(f'From 40 to 50: {percent_40_50 / num_of_turns * 100 :.2f}%')
print(f'Invalid numbers: {invalid_nums / num_of_turns * 100 :.2f}%')

