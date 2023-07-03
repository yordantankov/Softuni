def polindromes(texts):
    for text in texts:
        if text == "".join(reversed(text)):
            polindrome_words.append(text)
    return polindrome_words


words = input().split()
searched_polindromes = input()
polindrome_words = []
result = polindromes(words)
print(result)
print(f'Found palindrome {polindrome_words.count(searched_polindromes)} times')
