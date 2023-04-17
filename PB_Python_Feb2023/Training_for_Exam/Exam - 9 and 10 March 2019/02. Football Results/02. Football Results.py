result_1st = input()
result_2nd = input()
result_3rd = input()

win = 0
lost = 0
even = 0

if ord(result_1st[0]) > ord(result_1st[2]):
    win += 1
elif ord(result_1st[0]) < ord(result_1st[2]):
    lost += 1
else:
    even += 1

if ord(result_2nd[0]) > ord(result_2nd[2]):
    win += 1
elif ord(result_2nd[0]) < ord(result_2nd[2]):
    lost += 1
else:
    even += 1

if ord(result_3rd[0]) > ord(result_3rd[2]):
    win += 1
elif ord(result_3rd[0]) < ord(result_3rd[2]):
    lost += 1
else:
    even += 1

print(f"Team won {win} games.")
print(f"Team lost {lost} games.")
print(f"Drawn games: {even}")