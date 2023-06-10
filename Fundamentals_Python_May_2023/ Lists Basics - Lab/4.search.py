n = int(input())
special_word = input()
all_strings = []
for i in range(n):
    string = input()
    all_strings.append(string)

print(all_strings)

filtered_strings = []

for string in all_strings:
     if special_word in string:
         filtered_strings.append(string)

print(filtered_strings)
