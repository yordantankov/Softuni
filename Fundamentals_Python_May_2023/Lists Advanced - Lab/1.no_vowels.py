def sorter_text (texts):
    unuasaly_word = ["a", 'o',"u", 'e', 'i', 'A', 'O', 'U', "E", 'I']
    sorted_word = []
    for text in texts:
        if text not in unuasaly_word:
            sorted_word.append(text)
    return sorted_word
some_text = input()

result = sorter_text(some_text)

print("".join(result))
