import math
days_count = int(input())
first_day_mileage = float(input())
total_mileage = 0
for i in range(0,days_count+1):
    if i == 0:
        mileage = first_day_mileage
        continue
    percent_up = int(input())

    mileage += mileage * percent_up / 100
    total_mileage += mileage

total_mileage += first_day_mileage
if total_mileage >= 1000:
    diff = total_mileage - 1000
    print(f"You've done a great job running {math.ceil(diff)} more kilometers!")
else:
    diff = 1000 - total_mileage
    print(f"Sorry Mrs. Ivanova, you need to run {math.ceil(diff)} more kilometers")
