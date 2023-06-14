items = input().split("|")
budget = float(input())
sell_prices = []
profit = 0
train_ticket = 150
for item in items:
    type, buying_price = item.split("->")
    buying_price = float(buying_price)
    price_is_valid = False
    if type == "Clothes":
        if buying_price <= 50.00:
            price_is_valid = True
    elif type == "Shoes":
        if buying_price <= 35.00:
            price_is_valid = True
    elif type == "Accessories":
        if buying_price <= 20.50:
            price_is_valid = True
    if price_is_valid:
       if budget >= buying_price:
           budget -= buying_price
           sell_price = buying_price * 1.40
           profit+= sell_price - buying_price
           sell_prices.append(sell_price)

for sell in sell_prices:
    print(f"{sell:.2f}", end=" ")
print()

print(f'Profit: {profit:.2f}')
total_income = budget + sum(sell_prices)

if total_income >= train_ticket:
    print('Hello, France!')
else:
    print("Not enough money.")
