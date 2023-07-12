command = input()
revered_word = ""
while command != "end":
    for char in reversed(command):
        revered_word += char
    print(f'{command} = {revered_word}')
    revered_word = ""
    command = input()