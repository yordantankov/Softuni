given_text = input().split()

for string in given_text:
    print(string*len(string), end="")