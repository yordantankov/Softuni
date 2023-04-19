etap = input()
type_ticket = input()
count_tickets = int(input())
pic_of_trofey = input()
price = 0

if etap == "Quarter final":
    if type_ticket == "Standard":
        price = 55.50
    elif type_ticket == "Premium":
        price = 105.20
    elif type_ticket == "VIP":
        price = 118.90

elif etap == "Semi final":
    if type_ticket == "Standard":
        price = 75.88
    elif type_ticket == "Premium":
        price = 125.22
    elif type_ticket == "VIP":
        price = 300.40

elif etap == "Final":
    if type_ticket == "Standard":
        price = 110.10
    elif type_ticket == "Premium":
        price = 160.66
    elif type_ticket == "VIP":
        price = 400.00

sum = price * count_tickets

if sum > 4000 :
    sum -= sum * 0.25
    print(f'{sum :.2f}')
    exit()
if sum > 2500:
    sum -= sum * 0.10

if pic_of_trofey == "Y":
    price_for_pic = count_tickets * 40
    sum += price_for_pic
    print(f'{sum :.2f}')

else:
    print(f'{sum :.2f}')