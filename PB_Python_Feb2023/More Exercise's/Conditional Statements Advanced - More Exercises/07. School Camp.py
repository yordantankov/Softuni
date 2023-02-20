season = input()
type_group = input()
students_qty = int(input())
nights_qty = int(input())
sport = ""
night_price = 0

#nights price
if season == "Winter" :
    if type_group == "boys" or type_group == "girls" :
        night_price = students_qty * (nights_qty * 9.60)
    elif type_group == "mixed" :
        night_price = students_qty * (nights_qty * 10.00)
elif season == "Spring" :
    if type_group == "boys" or type_group == "girls" :
        night_price = students_qty * (nights_qty * 7.20)
    elif type_group == "mixed" :
        night_price = students_qty * (nights_qty * 9.50)
elif season == "Summer" :
    if type_group == "boys" or type_group == "girls" :
        night_price = students_qty * (nights_qty * 15.00)
    elif type_group == "mixed" :
        night_price =students_qty * (nights_qty * 20.00)

#type of sport
if season == "Winter" :
    if type_group == "girls":
        sport = "Gymnastics"
    elif type_group == "boys":
        sport = "Judo"
    elif type_group == "mixed" :
        sport = "Ski"
elif season == "Spring" :
    if type_group == "girls":
        sport = "Athletics"
    elif type_group == "boys":
        sport = "Tennis"
    elif type_group == "mixed" :
        sport = "Cycling"
elif season == "Summer" :
    if type_group == "girls":
        sport = "Volleyball"
    elif type_group == "boys":
        sport = "Football"
    elif type_group == "mixed" :
        sport = "Swimming"

#Calculation
if students_qty >= 50 :
    night_price -= night_price * 0.50
elif students_qty >= 20 and students_qty < 50:
    night_price -= night_price * 0.15
elif students_qty >= 10 and students_qty < 20 :
    night_price -= night_price * 0.05

#Output
print(f'{sport} {night_price :.2f} lv.')