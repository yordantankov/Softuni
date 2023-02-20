budjet = int(input())
season = input()
fishers_qty = int(input())
rent = 0
total_price = 0

if season == "Spring" :
    rent = 3000

    if fishers_qty <= 6:
            rent -= rent * 0.10
    elif fishers_qty > 6 and fishers_qty <= 11:
            rent -= rent * 0.15
    elif fishers_qty > 11 :
            rent -= rent * 0.25

    if fishers_qty % 2 == 0:
            rent -= rent * 0.05

elif season == "Summer" or season == "Autumn" :
    rent = 4200
    if season == "Summer" :

        if fishers_qty <= 6:
                rent -= rent * 0.10
        elif fishers_qty > 6 and fishers_qty <= 11:
                rent -= rent * 0.15
        elif fishers_qty > 11:
                rent -= rent * 0.25
        if fishers_qty % 2 == 0:
                rent -= rent * 0.05

    if season == "Autumn":

        if fishers_qty <= 6:
                rent -= rent * 0.10
        elif fishers_qty > 6 and fishers_qty <= 11:
                rent -= rent * 0.15
        elif fishers_qty > 11:
                rent -= rent * 0.25


elif season == "Winter" :
    rent = 2600

    if fishers_qty <= 6:
            rent -= rent * 0.10
    elif fishers_qty > 6 and fishers_qty <= 11:
            rent -= rent * 0.15
    elif fishers_qty > 11:
            rent -= rent * 0.25

    if fishers_qty % 2 == 0:
            rent -= rent * 0.05


if budjet >= rent :
    budjet -= rent
    print(f"Yes! You have {budjet :.2f} leva left.")

else:
    rent -= budjet
    print(f"Not enough money! You need {rent :.2f} leva.")