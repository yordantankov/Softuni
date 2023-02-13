fuel_type = input()
fuel_qty = float(input())
club_card = input()
price = 0
total_price = 0

if fuel_type == "Gasoline" :
    price = 2.22

    if club_card == "Yes":
        price -= 0.18

    total_price = fuel_qty * price

    if fuel_qty >= 20 and fuel_qty <=25 :
        total_price -= total_price * 0.08
    elif fuel_qty > 25:
        total_price -= total_price * 0.10

elif fuel_type == "Diesel" :
    price = 2.33

    if club_card == "Yes":
        price -= 0.12

    total_price = fuel_qty * price

    if fuel_qty >= 20 and fuel_qty <=25 :
        total_price -= total_price * 0.08
    elif fuel_qty > 25:
        total_price -= total_price * 0.10

elif fuel_type == "Gas" :
    price = 0.93

    if club_card == "Yes":
        price -= 0.08

    total_price = fuel_qty * price

    if fuel_qty >= 20 and fuel_qty <=25 :
        total_price -= total_price * 0.08
    elif fuel_qty > 25:
        total_price -= total_price * 0.10

print(f'{total_price :.2f} lv.')