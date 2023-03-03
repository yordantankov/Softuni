stadion_capacity = int(input())
all_fans = int(input())
team_1 = 0
team_2 = 0
f_in_A = 0
f_in_B = 0
f_in_V = 0
f_in_G = 0
percent_all_fan = all_fans / stadion_capacity * 100

for i in range(0, all_fans):
    sector = input()
    if sector == "A":
        f_in_A += 1
    elif sector == "B":
        f_in_B +=1
    elif sector == "V":
        f_in_V += 1
    elif sector == "G":
        f_in_G +=1

print(f'{f_in_A / all_fans * 100 :.2f}%')
print(f'{f_in_B / all_fans * 100 :.2f}%')
print(f'{f_in_V / all_fans * 100 :.2f}%')
print(f'{f_in_G / all_fans * 100 :.2f}%')
print(f'{percent_all_fan :.2f}%')