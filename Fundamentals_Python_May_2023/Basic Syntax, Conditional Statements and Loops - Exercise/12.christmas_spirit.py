quantity_decoration = int(input())
days_left = int(input())

spirit = 0
budget = 0

for i in range(1, days_left + 1):
    if i % 11 == 0:
        quantity_decoration += 2
    if i % 2 == 0:
        budget += quantity_decoration * 2
        spirit += 5
    if i % 3 == 0:
        budget += (quantity_decoration * 5) + (quantity_decoration * 3)
        spirit += 13

    if i % 5 == 0:
        budget += quantity_decoration * 15
        spirit += 17
        if  i % 3 == 0:
            spirit += 30

    if i % 10 == 0:
        spirit -= 20
        budget += 5+3+15


if days_left % 10 == 0:
    spirit -= 30

print(f'Total cost: {budget}')
print(f'Total spirit: {spirit}')