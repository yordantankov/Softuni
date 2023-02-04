area = float(input())
price_for_area = 7.61 * area
discount = price_for_area * 0.18
total_price = price_for_area - discount

print(f'The final price is: {total_price} lv.')
print(f'The discount is: {discount} lv.')