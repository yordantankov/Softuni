budjet = float(input())
season = input()
price = 0
resting_type = ""
place = ""

if budjet <= 1000 :
    resting_type = "Camp"
    if season == "Summer" :
        place = "Alaska"
        price = budjet * 0.65
    elif season == "Winter" :
        place = "Morocco"
        price = budjet * 0.45

elif budjet > 1000 and budjet <= 3000 :
    resting_type = "Hut"
    if season == "Summer" :
        place = "Alaska"
        price = budjet * 0.80
    elif season == "Winter" :
        place = "Morocco"
        price = budjet * 0.60

elif budjet > 3000 :
    resting_type = "Hotel"
    if season == "Summer" :
        place = "Alaska"
    elif season == "Winter" :
        place = "Morocco"
    price = budjet * 0.90

print(f"{place} - {resting_type} - {price :.2f}")

