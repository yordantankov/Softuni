def odd_and_even (num):
    odd_sum = 0
    even_sum = 0
    for current_num in num:
        if int(current_num) % 2 == 0:
            even_sum += int(current_num)
        else:
            odd_sum+= int(current_num)
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"

number = input()

print(odd_and_even(number))