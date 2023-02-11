budjet = float (input())
statist_qty = int(input())
price_for_clothes = float(input())

decor = budjet * 0.10
total_price_for_clothes = statist_qty * price_for_clothes

if statist_qty > 150 :
    total_price_for_clothes-= total_price_for_clothes * 0.10

total_price = total_price_for_clothes + decor

if total_price > budjet :
    total_price-= budjet
    print("Not enough money!")
    print(f'Wingard needs {total_price :.2f} leva more.')
else:
    budjet -= total_price
    print("Action!")
    print(f'Wingard starts filming with {budjet :.2f} leva left')