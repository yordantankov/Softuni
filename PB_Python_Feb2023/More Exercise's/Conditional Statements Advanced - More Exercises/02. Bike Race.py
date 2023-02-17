juniors = int(input())
seniors = int(input())
type_of_terrain = input()

price_for_juniors = 0
price_for_seniors = 0
total_price = 0

if type_of_terrain == "trail" :
    price_for_juniors = juniors * 5.50
    price_for_seniors = seniors * 7.00
    total_price = price_for_seniors + price_for_juniors

elif type_of_terrain == "cross-country" :
    price_for_juniors = juniors * 8.00
    price_for_seniors = seniors * 9.50
    total_price = price_for_seniors + price_for_juniors
    if seniors + juniors >= 50 :
        total_price -= total_price * 0.25

elif type_of_terrain == "downhill" :
    price_for_juniors = juniors * 12.25
    price_for_seniors = seniors * 13.75
    total_price = price_for_seniors + price_for_juniors

elif type_of_terrain == "road" :
    price_for_juniors = juniors * 20.00
    price_for_seniors = seniors * 21.50
    total_price = price_for_seniors + price_for_juniors


total_price -= total_price * 0.05
print(f'{total_price :.2f}')
