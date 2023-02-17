hrizantemi_qty = int(input())
rozi_qty = int(input())
laleta_qty = int(input())
season = input()
holiday_or_not = input()

flowers_qty = 0
total_sum= 0

if season == "Spring" or season == "Summer" :
    price_of_hrizantemi = 2.00
    price_of_rozi = 4.10
    price_of_laleta = 2.50

    if holiday_or_not == "Y" :
        price_of_hrizantemi += price_of_hrizantemi * 0.15
        price_of_rozi += price_of_rozi * 0.15
        price_of_laleta += price_of_laleta * 0.15

    sum_for_hrizantemi = hrizantemi_qty * price_of_hrizantemi
    sum_for_rozi = rozi_qty * price_of_rozi
    sum_for_laleta = laleta_qty * price_of_laleta
    total_sum = sum_for_laleta + sum_for_rozi + sum_for_hrizantemi
    flowers_qty = rozi_qty + hrizantemi_qty + laleta_qty


    if season == "Spring" :
        if laleta_qty > 7 :
             total_sum -= total_sum * 0.05

    if flowers_qty > 20:
        total_sum -= total_sum * 0.20



elif season == "Autumn" or season == "Winter" :
    price_of_hrizantemi = 3.75
    price_of_rozi = 4.50
    price_of_laleta = 4.15

    if holiday_or_not == "Y" :
        price_of_hrizantemi += price_of_hrizantemi * 0.15
        price_of_rozi += price_of_rozi * 0.15
        price_of_laleta += price_of_laleta * 0.15

    sum_for_hrizantemi = hrizantemi_qty * price_of_hrizantemi
    sum_for_rozi = rozi_qty * price_of_rozi
    sum_for_laleta = laleta_qty * price_of_laleta
    total_sum = sum_for_laleta + sum_for_rozi + sum_for_hrizantemi
    flowers_qty = rozi_qty + hrizantemi_qty + laleta_qty


    if season == "Winter" :
        if rozi_qty >= 10 :
            total_sum -= total_sum * 0.10

    if flowers_qty > 20:
        total_sum -= total_sum * 0.20


print(f"{(total_sum + 2) :.2f}")
