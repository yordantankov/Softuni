hour = int(input())
day = input()

if hour >= 10 and hour <= 18:
    if day == "Monday" :
        print('open')
    elif day == 'Tuesday' :
        print('open')
    elif day == 'Wednesday':
        print('open')
    elif day == 'Thursday' :
        print('open')
    elif day == 'Friday' :
        print('open')
    elif day == 'Saturday' :
        print('open')
    else:
        print('closed')

else:
    print('closed')