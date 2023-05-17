import math
import sys

powerful_word = ''
sum = 0
highest_sum = -sys.maxsize
while True:
    word = input()
    if word == "End of words":
        break

    for i in range(len(word)):
       char_letter = ord(word[i])
       sum += char_letter


    if word[0] == "A" or word[0] =="a" or word[0] == "E" or word[0] == "e" or word[0] =="i" or word[0] =="I" or word[0] == "O" or word[0] =="o" or word[0] =="U" or word[0] =="u" or word[0] =="Y" or word[0] =="y":
        sum *= len(word)
    else:
        sum /= len(word)
        sum = math.floor(sum)

    if sum > highest_sum:
        highest_sum = sum
        powerful_word = word
    sum = 0
print(f"The most powerful word is {powerful_word} - {highest_sum}" )
