import math

days_to_relax = int (input())

minutes_to_play_when_relax = days_to_relax * 127

work_days_to_play = (365 - days_to_relax) * 63
total = minutes_to_play_when_relax + work_days_to_play

if total <= 30000 :
    abstotal = 30000 - total
    print("Tom sleeps well")
    print(f'{ math.floor (abstotal / 60)} hours and {abstotal % 60} minutes less for play')

elif total >30000 :
    abstotal = total - 30000
    print("Tom will run away")
    print (f'{math.floor(abstotal / 60)} hours and {abstotal % 60} minutes more for play')


