text = input()
new_text = []
for word in text:
    for element in word:
        ascii_val = ord(element)
        the_word = ascii_val + 3
        new_text.append(chr(the_word))

for el in new_text:
    print("".join(el), end="")


