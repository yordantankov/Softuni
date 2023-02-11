trip_price = float (input())

puzzels_qty = int(input())
dools_qty = int(input())
bears_qty = int(input())
minions_qty = int(input())
trucks_qty = int(input())

all_qty = puzzels_qty + dools_qty + bears_qty + minions_qty + trucks_qty

price_for_puzzels = puzzels_qty * 2.60
price_for_dools = dools_qty * 3.00
price_for_bears = bears_qty * 4.10
price_for_minions = minions_qty * 8.20
price_for_trucks = trucks_qty * 2.00

price_for_all = price_for_trucks + price_for_minions + price_for_bears + price_for_dools + price_for_puzzels

if all_qty >= 50 :
    price_for_all = price_for_all - (price_for_all * 0.25)

total_earn = price_for_all - (price_for_all * 0.10)

if total_earn >= trip_price :
    money_left = total_earn - trip_price
    print(f'Yes! {money_left :.2f} lv left.')
else:
    money_left = trip_price - total_earn
    print(f'Not enough money! {money_left :.2f} lv needed.')
