import math
count_people = int(input())
tax = float(input())
price_for_shezlong = float(input())
price_for_umbrella = float(input())

price_tax = count_people * tax

people_for_shezlong = math.ceil(count_people * 0.75)
total_price_shezlong = people_for_shezlong * price_for_shezlong

needed_umbrelas = math.ceil(count_people / 2)
total_price_umbrelas = needed_umbrelas * price_for_umbrella

total = total_price_umbrelas + total_price_shezlong + price_tax

print(f'{total :.2f} lv.')