number = int(input())
diff = set()
rows = 0
points = 0
odd_numbers = set()
even_numbers = set()
for num in range(number):
    name = input()
    rows += 1
    points = 0
    for word in name:
        points += ord(word)

    points = int(points / rows)
    if points % 2 == 0:
        even_numbers.add(points)
    else:
        odd_numbers.add(points)
sum_odd = sum(odd_numbers)
sum_even = sum(even_numbers)

if sum_odd == sum_even:
    print(", ".join(str(el) for el in odd_numbers.union(even_numbers)))
elif sum_odd > sum_even:
    print(", ".join(str(el) for el in odd_numbers.difference(even_numbers)))
else:
    print(", ".join(str(el) for el in odd_numbers.symmetric_difference(even_numbers)))
