count_joinery = int(input())
type_joirnery = input()
delivery = input()
if count_joinery <= 10:
    print('Invalid order')
    exit()

price = 0

if type_joirnery == "90X130":
    if count_joinery <=30:
        price = 110
    elif count_joinery > 30 and count_joinery <= 60:
        price = 110 - (110 * 0.05)
    elif count_joinery > 60:
        price = 110 - (110 * 0.08)

elif type_joirnery == "100X150":
    if count_joinery <= 40:
        price = 140
    elif count_joinery > 40 and count_joinery <= 80:
        price = 140 - (140 * 0.06)
    elif count_joinery > 80:
        price = 140 - (140 * 0.10)

elif type_joirnery == "130X180":
    if count_joinery <= 20:
        price = 190
    elif count_joinery > 20 and count_joinery <= 50:
        price = 190 - (190 * 0.07)
    elif count_joinery > 50:
        price = 190 - (190 * 0.12)

elif type_joirnery == "200X300":
    if count_joinery <= 25:
        price = 250
    elif count_joinery > 25 and count_joinery <=50:
        price = 250 - (250 * 0.09)
    elif count_joinery > 50:
        price = 250 - (250 * 0.14)

total_price = count_joinery * price
if delivery == "With delivery":
    total_price += 60

if count_joinery > 99:
    total_price -= total_price * 0.04

print(f'{total_price :.2f} BGN')