price_for_strawberry = float(input())
bannanas_kg = float(input())
oranges_kg = float(input())
raspberries_kg = float(input())
strawberry_kg = float(input())

total_strawberry = price_for_strawberry * strawberry_kg

price_for_raspberrie = price_for_strawberry / 2
total_raspberrie = price_for_raspberrie * raspberries_kg

price_orange = price_for_raspberrie - (price_for_raspberrie * 0.40)
total_orange = price_orange * oranges_kg

price_bannana = price_for_raspberrie - (price_for_raspberrie * 0.80)
total_bannana = price_bannana * bannanas_kg

total = total_bannana + total_orange + total_raspberrie + total_strawberry

print(f'{total :.2f}')