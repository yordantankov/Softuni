given_numbers = input().split()
float_numbers = []
for number in given_numbers:
    float_numbers.append(round(float(number)))

print(float_numbers)