days = int(input())
type_room = input()
status = input()
nights = days - 1
price = 0

if type_room == "room for one person" :
    price = nights * 18.00

elif type_room == "apartment" :
    price = nights * 25.00
    if days < 10 :
        price -= price * 0.30
    elif days >= 10 and days <=15 :
        price -= price * 0.35
    elif days > 15 :
        price -= price * 0.50


elif type_room == "president apartment" :
    price = nights * 35.00
    if days < 10:
        price -= price * 0.10
    elif days >= 10 and days <= 15:
        price -= price * 0.15
    elif days > 15:
        price -= price * 0.20

if status == "positive" :
    price += price * 0.25
elif status == "negative" :
    price -= price * 0.10

print(f'{price :.2f}')