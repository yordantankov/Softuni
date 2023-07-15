numbers_of_city = int(input())
total_earn = 0

for current_city in range(1,numbers_of_city+1):
    name_of_the_city = input()
    owner_income = float(input())
    owner_expenses = float(input())

    if current_city % 5 == 0 :
        owner_income -= owner_income * 0.10

    elif current_city % 3 == 0:
        owner_expenses+= owner_expenses * 0.50

    profit = owner_income - owner_expenses
    total_earn+= profit

    print(f'In {name_of_the_city} Burger Bus earned {profit:.2f} leva.')

print(f'Burger Bus total profit: {total_earn:.2f} leva.')