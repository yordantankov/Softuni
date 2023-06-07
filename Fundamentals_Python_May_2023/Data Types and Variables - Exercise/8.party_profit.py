group = int(input())
days = int(input())
coins = 0

for day in range(1, days+1):
    if day % 10 == 0:
        group -= 2
    if day % 15 == 0:
        group += 5

    coins+= 50
    coins -= group * 2
    if day % 3 == 0:
        coins -= group * 3

    if day % 5 == 0:
        coins += group * 20
        if day % 3 == 0:
            coins -= group * 2

coin_per_companion = int(coins / group)
print(f"{group} companions received {coin_per_companion} coins each.")