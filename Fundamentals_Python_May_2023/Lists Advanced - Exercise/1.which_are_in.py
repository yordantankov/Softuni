first_text = input().split(", ")
second_text = input().split(", ")

match_word = []
for text in first_text:
    for filter_text in second_text:
      if text in filter_text:
          match_word.append(text)
          break

print(match_word)