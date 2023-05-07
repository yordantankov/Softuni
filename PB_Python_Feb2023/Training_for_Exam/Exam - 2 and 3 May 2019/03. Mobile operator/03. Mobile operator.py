time_of_contract = input()
type_contract = input()
internet = input()
months_for_pay = int(input())
price = 0
total = 0
if time_of_contract == "one":
    if type_contract == "Small":
        price = 9.98
    elif type_contract == 'Middle':
        price = 18.99
    elif type_contract == "Large":
        price = 25.98
    elif type_contract == "ExtraLarge":
        price = 35.99

    if internet == "yes":
        if price <= 10.00:
            price += 5.50
        elif price > 10.00 and price <= 30.00:
            price += 4.35
        elif price > 30.00:
            price += 3.85

    total = months_for_pay * price

elif time_of_contract == "two":
    if type_contract == "Small":
        price = 8.58
    elif type_contract == 'Middle':
        price = 17.09
    elif type_contract == "Large":
        price = 23.59
    elif type_contract == "ExtraLarge":
        price = 31.79

    if internet == "yes":
        if price <= 10.00:
            price += 5.50
        elif price > 10.00 and price <= 30.00:
            price += 4.35
        elif price > 30.00:
            price += 3.85

    total = months_for_pay * price
    total -= total * 0.0375

print(f'{total :.2f} lv.')