guest_count = int(input())
price_kuvert = float(input())
budjet = float(input())

if guest_count >= 10 and guest_count <= 15:
    price_kuvert -= price_kuvert * 0.15
elif guest_count > 15 and guest_count <= 20:
    price_kuvert -= price_kuvert * 0.20
elif guest_count > 20:
    price_kuvert -= price_kuvert * 0.25

price = guest_count * price_kuvert

price_for_cake = budjet * 0.10
budjet -= price_for_cake

if budjet >= price:
    diff = budjet - price
    print(f"It is party time! {diff :.2f} leva left.")

else:
    diff = price - budjet
    print(f"No party! {diff :.2f} leva needed.")