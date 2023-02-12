kilometers = int(input())
time_of_the_day = input()

starting_price = 0
total_price = 0

if kilometers <= 19:
    starting_price = 0.70
    if time_of_the_day == "day":
        starting_price += 0.09
        total_price = kilometers * starting_price + 0.70
        print(f'{total_price :.2f}')
    elif time_of_the_day == "night":
        starting_price += 0.20
        total_price = kilometers * starting_price + 0.70
        print(f'{total_price :.2f}')

if kilometers >= 20 and kilometers < 100:
    starting_price = 0.09
    total_price = kilometers * starting_price
    print(f'{total_price :.2f}')

if kilometers >= 100:
    starting_price = 0.06
    total_price = kilometers * starting_price
    print(f'{total_price :.2f}')