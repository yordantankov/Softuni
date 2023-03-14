num1 = int(input())
num2 = int(input())

for num in range(num1 , num2 + 1):
    even_nums = 0
    odd_nums = 0
    num_to_string = str(num)
    for index, digit in enumerate (num_to_string):
        if index % 2 == 0:
            odd_nums += int(digit)
        else:
            even_nums += int(digit)
    if even_nums == odd_nums :
        print(num , end= " ")