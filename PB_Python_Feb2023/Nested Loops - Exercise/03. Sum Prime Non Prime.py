prime_nums = 0
non_prime_nums = 0

while True:
    is_prime = True
    number = input()

    if number == "stop":
        break

    number = int(number)

    if number < 0 :
        print("Number is negative")
        continue
    for i in range(2 , number):
        if number % i == 0:
            is_prime = False
            break
    if number > 0:
        if is_prime:
            prime_nums += number
        else:
            non_prime_nums += number


print(f'Sum of all prime numbers is: {prime_nums}')
print(f'Sum of all non prime numbers is: {non_prime_nums}')

