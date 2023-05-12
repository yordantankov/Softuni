type_drink = input()
sugar = input()
count_drinks = int(input())

price = 0
if type_drink == "Espresso":
    if sugar == 'Without':
        price = 0.90 - (0.90 * 0.35)

    elif sugar == 'Normal':
        price = 1.00
    elif sugar == "Extra":
        price = 1.20

    if count_drinks >= 5:
        price -= price * 0.25

elif type_drink == "Cappuccino":
    if sugar == "Without":
        price = 1.00 - (1.00 * 0.35)
    elif sugar == "Normal":
        price = 1.20
    elif sugar == "Extra":
        price = 1.60

elif type_drink == 'Tea':
    if sugar == "Without":
        price = 0.50 - (0.50 * 0.35)
    elif sugar == "Normal":
        price = 0.60
    elif sugar == "Extra":
        price = 0.70

total = count_drinks * price

if total > 15.00:
    total -= total * 0.20

print(f"You bought {count_drinks} cups of {type_drink} for {total :.2f} lv.")