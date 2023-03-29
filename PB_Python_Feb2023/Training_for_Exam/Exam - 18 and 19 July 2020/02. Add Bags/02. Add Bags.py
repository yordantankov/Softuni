price_for_bags_over_20kg = float(input())
kg_of_bags = float(input())
days_to_the_trip = int(input())
bags_quantity = int(input())
price_for_bags = 0
if kg_of_bags < 10:
    price_for_bags = price_for_bags_over_20kg * 0.20
elif kg_of_bags >= 10 and kg_of_bags <= 20:
    price_for_bags = price_for_bags_over_20kg / 2
elif kg_of_bags > 20:
    price_for_bags = price_for_bags_over_20kg

if days_to_the_trip > 30:
    price_for_bags += price_for_bags * 0.10
elif days_to_the_trip >= 7 and days_to_the_trip <= 30:
    price_for_bags += price_for_bags * 0.15
elif days_to_the_trip < 7:
    price_for_bags += price_for_bags * 0.40

total_price = price_for_bags * bags_quantity

print(f"The total price of bags is: {total_price :.2f} lv.")