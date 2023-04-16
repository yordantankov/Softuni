import math

tennis_rocket_price = float(input())
count_tennis_rocket = int(input())
count_shoes = int(input())

price_for_tennis_rockets = tennis_rocket_price * count_tennis_rocket

price_for_shoes  = tennis_rocket_price / 6
total_shoes = price_for_shoes * count_shoes

sum = total_shoes + price_for_tennis_rockets
clothes  = sum * 0.20
total = clothes + sum

print(f"Price to be paid by Djokovic {math.floor(total / 8 )}")
print(f"Price to be paid by sponsors {math.ceil(total * 7 / 8)}")