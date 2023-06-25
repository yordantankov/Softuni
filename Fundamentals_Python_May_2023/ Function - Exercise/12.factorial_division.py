def factorial_num(num_1):

    for num in range(1, num_1):
           num_1*= num

    return num_1


first_num = int(input())
second_num = int(input())

first = factorial_num(first_num)
second = factorial_num(second_num)
total = first / second

print(f'{total :.2f}')