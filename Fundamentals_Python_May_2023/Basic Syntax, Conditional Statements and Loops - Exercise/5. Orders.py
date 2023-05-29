count_orders = int(input())

price = 0
total_price = 0
for i in range(count_orders):
    price_for_capsule = float(input())
    days = int(input())
    needed_capsules_per_day = int(input())

    if price_for_capsule < 0.01 or price_for_capsule > 100 :
        continue
    elif days < 1 or days > 31:
        continue
    elif needed_capsules_per_day < 1 or needed_capsules_per_day > 2000:
        continue
    total_price_for_capsule = needed_capsules_per_day * price_for_capsule
    price_per_day = total_price_for_capsule * days
    price+= price_per_day
    total_price += price

    print(f'The price for the coffee is: ${price :.2f}')
    price = 0

print(f'Total: ${total_price :.2f}')


