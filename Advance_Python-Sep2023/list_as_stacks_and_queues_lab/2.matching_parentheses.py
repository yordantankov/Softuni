text = input()
parantheses = []

for element in range(len(text)):
    if text[element] == "(":
        parantheses.append(element)
    elif text[element] == ")":
        start_index = parantheses.pop()
        print(text[start_index: element + 1])

