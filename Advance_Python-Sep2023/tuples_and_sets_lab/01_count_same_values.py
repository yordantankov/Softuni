
nums = tuple(float(el) for el in input().split())

occ = {}

for num in nums:
    if num not in occ:
        occ[num] = nums.count(num)

for key, value in occ.items():
    print(f"{key} - {value} times")
