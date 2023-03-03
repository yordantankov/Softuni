months = int(input())
total_price = 0
bill_for_water = 0
bill_for_ele = 0
bill_for_internet = 0
other_bills = 0

for i in range(0, months):
    bill_for_el = float(input())
    bill_for_ele += bill_for_el
    bill_for_water += 20
    bill_for_internet += 15
    other_bills += (bill_for_el + 15 + 20) + ((bill_for_el + 15 + 20) * 0.20)

total_price = bill_for_water + bill_for_internet + bill_for_ele + other_bills
print(f'Electricity: {bill_for_ele :.2f} lv')
print(f'Water: {bill_for_water :.2f} lv')
print(f'Internet: {bill_for_internet :.2f} lv')
print(f'Other: {other_bills :.2f} lv')
print(f'Average: {total_price / months :.2f} lv')