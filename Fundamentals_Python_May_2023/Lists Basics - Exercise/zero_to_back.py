numbers = input().split(", ")
zeros_list = []
non_zero_list = []

for num in numbers:
    num = int(num)
    if num == 0:
        zeros_list.append(num)
    else:
        non_zero_list.append(num)

result = non_zero_list + zeros_list

print(result)
