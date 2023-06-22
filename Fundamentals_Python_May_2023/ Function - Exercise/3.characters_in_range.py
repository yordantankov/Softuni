def range_character (char_1, char_2):
      character = []
      for char in range(ord(char_1) + 1, ord(char_2)):
          character.append(chr(char))
      return character


first_character = input()
second_character = input()
result = range_character(first_character, second_character)

print(" ".join(result))
