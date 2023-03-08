import math
sum = float(input())

coins_count = 0

while True:
    sum = round(sum ,2)
    if sum >= 2:
        sum -= 2
        coins_count +=1
    elif sum >= 1:
        sum -= 1
        coins_count +=1
    elif sum >= 0.50:
        sum -= 0.50
        coins_count += 1
    elif sum >= 0.20 :
        sum -= 0.20
        coins_count +=1
    elif sum >= 0.10:
        sum -= 0.10
        coins_count +=1
    elif sum >= 0.05:
        sum -= 0.05
        coins_count +=1
    elif sum >= 0.02:
        sum -= 0.02
        coins_count += 1
    elif sum >= 0.01:
        sum -= 0.01
        coins_count += 1

    if sum == 0:
        break

print(coins_count)