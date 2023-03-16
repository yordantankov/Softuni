movie_name = input()
type = input()
bought_tickets = int(input())
price = 0
if movie_name == "A Star Is Born":
    if type == "normal":
        price = bought_tickets * 7.50
    elif type == "luxury":
        price = bought_tickets * 10.50
    elif type == "ultra luxury":
        price = bought_tickets * 13.50

elif movie_name == "Bohemian Rhapsody":
    if type == "normal":
        price = bought_tickets * 7.35
    elif type == "luxury":
        price = bought_tickets * 9.45
    elif type == "ultra luxury":
        price = bought_tickets * 12.75

elif movie_name == "Green Book":
    if type == "normal":
        price = bought_tickets * 8.15
    elif type == "luxury":
        price = bought_tickets * 10.25
    elif type == "ultra luxury":
        price = bought_tickets * 13.25

elif movie_name == "The Favourite":
    if type == "normal":
        price = bought_tickets * 8.75
    elif type == "luxury":
        price = bought_tickets * 11.55
    elif type == "ultra luxury":
        price = bought_tickets * 13.95

print(f'{movie_name} -> {price :.2f} lv.')
