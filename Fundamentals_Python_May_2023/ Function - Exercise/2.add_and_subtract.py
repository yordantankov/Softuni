def sum_numbers(first, second):
    return first_num + second_num


def subtract(sum, third):
    return sum - third

def add_and_subtract(number_one, number_two, number_three):
    sum_of_first_and_second = sum_numbers(number_one, number_two)
    result = subtract(sum_of_first_and_second, number_three)
    return result

first_num = int(input())
second_num = int(input())
third_num = int(input())

print(add_and_subtract(first_num, second_num, third_num))