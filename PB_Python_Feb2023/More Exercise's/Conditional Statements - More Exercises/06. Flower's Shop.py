import math

magnolias_qty = int(input())
hyacinths_qty = int(input())
roses_qty = int(input())
cactus_qty = int(input())
price_for_present = float(input())

price_magnolias = magnolias_qty * 3.25
price_hyacinth = hyacinths_qty * 4.00
price_roses = roses_qty * 3.50
price_cactus = cactus_qty * 8.00

all_price = price_roses + price_cactus + price_hyacinth + price_magnolias
price_with_tax = all_price - (all_price * 0.05)

if price_with_tax >= price_for_present:
    price_with_tax -= price_for_present
    print(f"She is left with {math.floor(price_with_tax)} leva.")
else:
    price_for_present -= price_with_tax
    print(f"She will have to borrow {math.ceil(price_for_present)} leva.")