budjet = float(input())
money_earnd_per_day = float(input())
total_cost = float(input())
present_price = float(input())

saved_money = budjet * 5
earn = money_earnd_per_day * 5
total_save = saved_money + earn
total_save -= total_cost

if total_save >= present_price:
    print(f"Profit: {total_save :.2f} BGN, the gift has been purchased.")

else:
    diff = present_price - total_save
    print(f"Insufficient money: {diff :.2f} BGN.")