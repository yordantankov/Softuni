cargo_qty = int(input())
price_for_microbus = 0
price_for_truck = 0
price_for_train = 0
tons = 0
tons_mic = 0
tons_truck = 0
tons_train = 0
for i in range (0, cargo_qty):
    tons_of_cargo = int(input())

    if tons_of_cargo <= 3:
        price_for_microbus += tons_of_cargo * 200
        tons_mic += tons_of_cargo
    elif tons_of_cargo >= 4 and tons_of_cargo <= 11:
        price_for_truck += tons_of_cargo * 175
        tons_truck += tons_of_cargo
    elif tons_of_cargo > 11:
        price_for_train += tons_of_cargo * 120
        tons_train += tons_of_cargo
    tons += tons_of_cargo

total_price = price_for_train + price_for_truck + price_for_microbus
average_price = total_price / tons
print(f'{average_price :.2f}')
print(f'{tons_mic / tons * 100 :.2f}%')
print(f'{tons_truck / tons * 100 :.2f}%')
print(f'{tons_train / tons * 100 :.2f}%')

