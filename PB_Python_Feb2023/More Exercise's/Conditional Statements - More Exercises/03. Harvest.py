import math

square_meters = int(input())
grape_per_meter =  float(input())
needed_liters_wine = int (input())
workers = int(input())

harvest = square_meters * grape_per_meter
harvest_for_wine =  harvest * 0.40
harvest_left = harvest - harvest_for_wine
wine_liters = harvest_for_wine / 2.5

if wine_liters < needed_liters_wine:
    needed_liters_wine -= wine_liters
    print(f'It will be a tough winter! More {math.floor(needed_liters_wine)} liters wine needed.')

else:
    wine_left = wine_liters - needed_liters_wine
    wine_for_workers = wine_left / workers
    print(f'Good harvest this year! Total wine: {math.floor(wine_liters)} liters.')
    print(f'{math.ceil(wine_left)} liters left -> {math.ceil(wine_for_workers)} liters per person.')


