budjet = float(input())
type_of_ticket = input()
people_qty = int(input())
money_left = 0
price_for_tickets = 0

#money left after paying the transport
if people_qty >= 1 and people_qty <= 4 :
    money_left = budjet - (budjet * 0.75)

elif people_qty >=5 and people_qty <= 9 :
    money_left = budjet - (budjet * 0.60)

elif people_qty >=10 and people_qty <= 24 :
    money_left = budjet - (budjet * 0.50)

elif people_qty >=25 and people_qty <= 49 :
    money_left = budjet - (budjet * 0.40)

elif people_qty >= 50 :
    money_left = budjet - (budjet * 0.25)
#price for tickets
if type_of_ticket == "VIP" :
    price_for_tickets = people_qty * 499.99
elif type_of_ticket == "Normal" :
    price_for_tickets = people_qty * 249.99

#calculation
if price_for_tickets <= money_left :
    price_for_tickets-= money_left
    print(f"Yes! You have {abs (price_for_tickets) :.2f} leva left.")

else:
    money_left -= price_for_tickets
    print(f"Not enough money! You need {abs (money_left) :.2f} leva.")