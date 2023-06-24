def polindrome_num (nums):
    if nums == nums [::-1]:
        return True
    return False

numbers = input().split(", ")

for number in numbers:
    print(polindrome_num(number))

