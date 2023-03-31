count_people = int(input())
count_nights = int(input())
count_maps = int(input())
count_tickets = int(input())

price_for_nights = count_nights * 20
price_for_maps = count_maps * 1.60
price_for_tickets = count_tickets * 6
total = price_for_tickets + price_for_maps + price_for_nights
sum = total * count_people
sum += sum * 0.25

print(f'{sum :.2f}')

