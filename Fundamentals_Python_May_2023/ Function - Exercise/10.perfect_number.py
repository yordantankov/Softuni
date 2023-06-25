def perfect_num (given_num):
    sum = 0
    for num in  range(1, given_num):
         if given_num % num == 0:
             sum+= num
    if given_num == sum:
        return (f'We have a perfect number!')
    else:
        return (f"It's not so perfect.")

number = int(input())

print(perfect_num(number))