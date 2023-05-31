
budget = float(input())
kg_flour_price = float(input())

pack_eggs_price = kg_flour_price * 0.75
price_liter_milk = kg_flour_price + (kg_flour_price * 0.25)

product_price = kg_flour_price + pack_eggs_price + (price_liter_milk * 0.25)
loaves = 0
colored_eggs= 0
while True:
    if budget < product_price :
        break
    budget -= product_price

    loaves += 1
    colored_eggs += 3
    if loaves % 3 == 0:
        colored_eggs -= loaves - 2


print(f"You made {loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget :.2f}BGN left.")