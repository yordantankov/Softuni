is_digit = ""
is_string= ""
is_letters = ""
given_text = input()

for element in given_text:
    if element.isdigit():
        is_digit += element
    elif element.isalpha():
        is_string += element
    else:
        is_letters += element

print(is_digit)
print(is_string)
print(is_letters)

