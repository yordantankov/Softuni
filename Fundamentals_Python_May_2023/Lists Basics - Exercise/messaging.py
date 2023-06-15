numbers = input().split()
text = input()

message = ""

for number in numbers:
    index = sum(int(digit) for digit in number)
    while index >= len(text):
        index -= len(text)
    char = text[index]
    message += char
    text = text[:index] + text[index+1:]

print(message)