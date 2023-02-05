deposit_price = float(input())
deposit_time = int(input())
year_percent = float(input())

deposit_total = deposit_price * year_percent / 100
for_one_mounth = deposit_total / 12
total = deposit_price + deposit_time * for_one_mounth

print (total)