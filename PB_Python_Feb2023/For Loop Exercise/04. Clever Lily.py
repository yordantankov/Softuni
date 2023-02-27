ages_of_Lili = int(input())
wash_machine_price = float(input())
toy_price = int(input())

toy_count = 0
money = 0
second_money = 0
ages = 0
counter = 0
for i in range (0, ages_of_Lili):
    ages += 1
    if ages % 2 == 0:
        money = money + 10
        second_money = second_money + money
        counter += 1

    else:
        toy_count += 1


toy_earn = toy_count * toy_price
second_money += toy_earn
second_money -= counter

if second_money >= wash_machine_price :
    diff = second_money - wash_machine_price
    print(f'Yes! {diff :.2f}')
else:
    diff = wash_machine_price - second_money
    print(f'No! {diff :.2f}')
