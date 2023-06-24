numbers = input().split()
nums_in_digit = []
for num in numbers:
    nums_in_digit.append(int(num))

print(f"The minimum number is {min(nums_in_digit)}")
print(f"The maximum number is {max(nums_in_digit)}")
print(f"The sum number is: {sum(nums_in_digit)}")