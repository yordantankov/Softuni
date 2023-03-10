needed_sum = int(input())
cash_pay_qty = 0
card_pay_qty = 0
pay_count = 0
total_earn = 0
cash_count_pay = 0
card_count_pay = 0

while True:
    pay = input()
    if pay == "End":
        print('Failed to collect required money for charity.')
        exit()

    pay = int(pay)
    pay_count += 1

    if pay_count % 2 == 0:
        if pay < 10:
            print('Error in transaction!')
            continue
        card_pay_qty += pay
        total_earn += pay
        card_count_pay += 1
        print('Product sold!')

    else:
        if pay > 100 :
            print('Error in transaction!')
            continue
        cash_pay_qty += pay
        total_earn += pay
        cash_count_pay += 1
        print('Product sold!')

    if total_earn >= needed_sum:
        break

average_cash_pay = cash_pay_qty / cash_count_pay
average_card_pay = card_pay_qty / card_count_pay

print(f'Average CS: {average_cash_pay :.2f}')
print(f'Average CC: {average_card_pay :.2f}')