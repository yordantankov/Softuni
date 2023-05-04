budjet = float(input())
needed_gas = float(input())
day = input()

price_gas = needed_gas * 2.10
price_gas += 100

if day == "Saturday":
    price_gas -= price_gas * 0.10
elif day == 'Sunday':
    price_gas -= price_gas * 0.20

if price_gas <= budjet:
    diff = budjet - price_gas
    print(f"Safari time! Money left: {diff :.2f} lv.")
else:
    diff = price_gas - budjet
    print(f"Not enough money! Money needed: {diff :.2f} lv.")