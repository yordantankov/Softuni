budget_for_film = float(input())
destination = input()
season_set = input()
count_days = int(input())
price = 0

if destination == "Dubai":
    if season_set == "Winter":
        price = 45000
    elif season_set == "Summer":
        price = 40000

elif destination == "Sofia":
    if season_set == "Winter":
        price = 17000
    elif season_set == "Summer":
        price = 12500

elif destination == "London":
    if season_set == "Winter":
        price = 24000
    elif season_set == "Summer":
        price = 20250

total = price * count_days

if destination == "Dubai":
    total -= total * 0.30

if destination == "Sofia":
    total += total * 0.25

if total <= budget_for_film:
    diff = budget_for_film - total
    print(f"The budget for the movie is enough! We have {diff :.2f} leva left!")
else:
    diff = total - budget_for_film
    print(f"The director needs {diff :.2f} leva more!")
