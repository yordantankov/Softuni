num = float(input())

if num == 0:
    print('zero')
elif num > 0 :
    if num < 1 :
        print('small positive')
    elif num < 1000000:
        print('positive')
    else:
        print('large positive')
else:
    if num > -1 :
        print('small negative')
    elif abs(num) > 1000000:
        print('large negative')
    else:
        print('negative')
