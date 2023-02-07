price_kilograms_vegetables = float(input())
price_kilograms_fruits = float(input())
total_kilograms_vegetables = int (input())
total_kilograms_fruits = int (input())

total_sum_veg = price_kilograms_vegetables *total_kilograms_vegetables
total_sum_fruits = price_kilograms_fruits * total_kilograms_fruits

sum = (total_sum_veg + total_sum_fruits) / 1.94

print(f'{sum :.2f}')
