banned_words = input().split(", ")
given_text = input()

for word in banned_words:
    if word in given_text:
        given_text = given_text.replace(word, "*" * len(word))

print(given_text)