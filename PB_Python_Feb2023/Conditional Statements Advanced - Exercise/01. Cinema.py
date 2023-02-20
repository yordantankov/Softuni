type_cinema = input()
lines = int (input())
columns = int(input())
total_price = 0
all_places = lines * columns

if type_cinema =="Premiere" :
    total_price = all_places * 12.00
elif type_cinema == "Normal" :
    total_price = all_places * 7.50
elif type_cinema == "Discount" :
    total_price = all_places * 5.00

print(f'{total_price :.2f} leva')
