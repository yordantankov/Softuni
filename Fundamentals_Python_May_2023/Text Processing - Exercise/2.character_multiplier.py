def calculate_sum(str1, str2):
    total_sum = 0
    length = min(len(str1), len(str2))

    for index in range(length):
        char1 = str1[index]
        char2 = str2[index]
        total_sum += ord(char1) * ord(char2)

    if len(str1) > length:
        remaining_chars = str1[length:]
        for char in remaining_chars:
            total_sum += ord(char)

    if len(str2) > length:
        remaining_chars = str2[length:]
        for char in remaining_chars:
            total_sum += ord(char)

    return total_sum

command = input()
str1, str2 = command.split()
result = calculate_sum(str1, str2)
print(result)