budjet = float(input())
count_nights = int(input())
price_for_night = float(input())
percent_additional_costs = int(input())

if count_nights > 7 :
    price_for_night -= price_for_night * 0.05

total_price_for_nights = price_for_night * count_nights

additional_cost = budjet * percent_additional_costs / 100

budjet -= additional_cost + total_price_for_nights

if budjet >= 0:
    print(f"Ivanovi will be left with {budjet :.2f} leva after vacation.")

else:
    budjet = abs(budjet)
    print(f'{budjet :.2f} leva needed.')