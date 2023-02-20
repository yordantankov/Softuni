type_flowers = input()
flowers_qty = int(input())
budjet = int(input())
total_price = 0

if type_flowers == "Roses" :
    total_price = flowers_qty * 5
    if flowers_qty > 80 :
        total_price -= total_price * 0.10

elif type_flowers == "Dahlias" :
    total_price = flowers_qty * 3.80
    if flowers_qty > 90 :
        total_price -= total_price * 0.15

elif type_flowers == "Tulips" :
    total_price = flowers_qty * 2.80
    if flowers_qty > 80 :
        total_price -= total_price * 0.15

elif type_flowers == "Narcissus" :
    total_price = flowers_qty * 3.00
    if flowers_qty < 120 :
        total_price += total_price * 0.15

elif type_flowers == "Gladiolus" :
    total_price = flowers_qty * 2.50
    if flowers_qty < 80 :
        total_price += total_price * 0.20

if total_price <= budjet :
    budjet -= total_price
    print(f"Hey, you have a great garden with {flowers_qty} {type_flowers} and {budjet :.2f} leva left.")

else:
    total_price -= budjet
    print(f"Not enough money, you need {total_price :.2f} leva more.")