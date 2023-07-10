given_text = input().split(", ")
dict_text = {}

for element in given_text:
    key = element
    value = ord(element)
    dict_text[key] = value

print(dict_text)