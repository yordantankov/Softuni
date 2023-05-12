city = input()
type_package = input()
vip = input()
days = int(input())
price = 0

if days < 1:
    print('Days must be positive number!')
    exit()

if city == "Bansko" or city == "Borovets":
    if type_package == "noEquipment":
        price = 80
        if vip == 'yes':
           price -= price * 0.05

    elif type_package == "withEquipment":
        price = 100
        if vip == "yes":
            price -= price * 0.10

    else:
        print('Invalid input!')
        exit()

elif city == "Varna" or city == "Burgas":
    if type_package == "noBreakfast":
        price = 100
        if vip == 'yes':
            price -= price * 0.07

    elif type_package == "withBreakfast":
        price = 130
        if vip == "yes":
            price -= price * 0.12

    else:
        print('Invalid input!')
        exit()

else:
    print('Invalid input!')
    exit()

total = days * price
if days > 7 :
    total -= price
print(f"The price is {total :.2f}lv! Have a nice time!")
