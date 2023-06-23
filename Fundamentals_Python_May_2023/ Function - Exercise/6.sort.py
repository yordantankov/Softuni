nums = input().split()
nums_digits = []
for num in nums:
    nums_digits.append(int(num))
sorted_nums = sorted(nums_digits)

print(sorted_nums)
