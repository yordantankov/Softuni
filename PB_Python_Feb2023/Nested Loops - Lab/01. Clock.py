for h in range (0, 23+1):
    for m in range (0 , 59 + 1):
        if m < 10:
            print(f'{h}:0{m}')
        else:
           print(f'{h}:{m}')