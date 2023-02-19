budjet = float(input())
season = input()
class_car = ""
price = 0
type_car = ""

if budjet <= 100 :
    class_car = "Economy class"
    if season == "Summer" :
        type_car = "Cabrio"
        price = budjet * 0.35
    elif season == "Winter" :
        type_car = "Jeep"
        price = budjet * 0.65

elif budjet > 100 and budjet <= 500:
    class_car = "Compact class"
    if season == "Summer" :
        type_car = "Cabrio"
        price = budjet * 0.45
    elif season == "Winter" :
        type_car = "Jeep"
        price = budjet * 0.80

elif budjet > 500 :
    class_car = "Luxury class"
    if season == "Summer" or season == "Winter":
        type_car = "Jeep"
        price = budjet * 0.90

print(f"{class_car}")
print(f"{type_car} - {price :.2f}")

