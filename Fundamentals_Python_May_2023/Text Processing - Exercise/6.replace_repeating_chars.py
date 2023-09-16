given_text = input()
new_word = ""

for element in given_text:
    if element not in new_word:
        new_word += element
    elif element != new_word[-1]:
        new_word+= element

print(new_word)
