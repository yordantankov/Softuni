city = input()
commission = float(input())
total = 0

if city == "Sofia" :
    if commission >= 0 and commission <= 500 :
        total = commission * 0.05
    elif commission > 500 and commission <= 1000 :
        total = commission * 0.07
    elif commission > 1000 and commission <=10000 :
        total = commission * 0.08
    elif commission > 10000 :
        total = commission * 0.12
    else:
        print('error')
        exit()

elif city == "Varna" :
    if commission >= 0 and commission <= 500 :
        total = commission * 4.5 / 100
    elif commission >500 and commission <= 1000 :
        total = commission * 7.5 / 100
    elif commission > 1000 and commission <=10000 :
        total = commission * 0.10
    elif commission > 10000:
        total = commission * 0.13
    else:
        print('error')
        exit()

elif city == "Plovdiv" :
    if commission >= 0 and commission <= 500 :
        total = commission * 5.5 / 100
    elif commission > 500 and commission <= 1000 :
        total = commission * 0.08
    elif commission > 1000 and commission <= 10000 :
        total = commission * 0.12
    elif commission > 10000:
        total = commission * 14.5 / 100
    else:
        print('error')
        exit()

else:
    print('error')
    exit()

print(f'{total :.2f}')