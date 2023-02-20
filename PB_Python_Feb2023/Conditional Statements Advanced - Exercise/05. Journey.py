budjet = float(input())
season = input()

place = ""
price = 0
type_rest = ""

if budjet <= 100 :
    place = "Bulgaria"
    if season == "summer" :
        type_rest = "Camp"
        price =budjet * 0.30

    elif season == "winter" :
        type_rest = "Hotel"
        price = budjet * 0.70

elif budjet > 100 and budjet <= 1000 :
    place = "Balkans"
    if season == "summer" :
        type_rest = "Camp"
        price = budjet * 0.40
    elif season == "winter" :
        type_rest = "Hotel"
        price = budjet * 0.80

elif budjet > 1000 :
    place = "Europe"
    type_rest = "Hotel"
    price = budjet * 0.90

print(f"Somewhere in {place}")
print(f'{type_rest} - {price :.2f}')