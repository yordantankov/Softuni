first_str = input()
second_str = input()

while first_str in second_str:
    second_str = second_str.replace(first_str, "")

print(second_str)