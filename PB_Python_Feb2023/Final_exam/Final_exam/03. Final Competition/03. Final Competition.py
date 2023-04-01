count_dancers = int(input())
points = float(input())
season = input()
place = input()
earn = 0
if place == "Bulgaria":
    earn = count_dancers * points
    if season == "summer":
        earn -= earn * 0.05
    elif season == "winter":
        earn -= earn * 0.08

elif place == "Abroad":
    earn = count_dancers * points
    earn += earn * 0.50
    if season == "summer":
        earn -= earn * 0.10
    elif season == "winter":
        earn -= earn * 0.15

blagotvoritelnost = earn * 0.75
earn -= earn * 0.75
money_left = earn / count_dancers

print(f"Charity - {blagotvoritelnost :.2f}")
print(f"Money per dancer - {money_left :.2f}")

