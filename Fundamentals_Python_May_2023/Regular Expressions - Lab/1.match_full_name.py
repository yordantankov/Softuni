import re

names = input()

pattern = "\\b[A-Z][a-z]+ [A-Z][a-z]+\\b"

mathes = re.findall(pattern, names)

for element in mathes:
    print(element, end=" ")