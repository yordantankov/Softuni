taxes = 0
total_price = 0
final_command = ""
while True:
    command = input()
    if command == "special" or command == "regular":
        final_command = command
        break

    command  = float(command)
    if command >= 0 :
        total_price += command
        taxes += command * 0.20

    else:
        print('Invalid price!')
        continue

if total_price == 0:
    print('Invalid order!')
    exit()
sum = taxes + total_price

if final_command == "special":
    sum_with_discount = sum - (sum * 0.10)
    print(f"Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f'Total price: {sum_with_discount:.2f}$')
else:
    print(f"Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f'Total price: {sum:.2f}$')
