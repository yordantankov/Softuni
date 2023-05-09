days = int(input())
hours = int(input())
price = 0
total_price = 0
for i in range(1 ,days + 1):

    for j in range(1,hours + 1):

        if i % 2 == 0 and j % 2 != 0:
             price += 2.50

        elif i % 2 != 0 and j % 2 == 0:
                price += 1.25

        else:
            price += 1

    print(f'Day: {i} - {price :.2f} leva')
    total_price += price
    price = 0

print(f'Total: {total_price :.2f} leva')

