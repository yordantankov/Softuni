def even_numbers (nums):
    even_nums = []
    for num in nums:
        if int(num) % 2 == 0:
            even_nums.append(int(num))
    return even_nums

numbers = input().split()

print(even_numbers(numbers))