money_needed = float(input())
money_status = float(input())

count_spend = 0
days = 0

while money_status < money_needed :
    command = input()
    money = float(input())
    days += 1

    if command == "spend":
        money_status -= money
        if money_status <= 0:
            money_status = 0
        count_spend += 1
        if count_spend == 5:
            print("You can't save the money.")
            print(f'{days}')
            exit()

    elif command == "save":
        count_spend = 0
        money_status += money

print(f"You saved the money for {days} days.")