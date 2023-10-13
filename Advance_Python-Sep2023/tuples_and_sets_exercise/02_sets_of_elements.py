numbers = input().split()
n, m = numbers[0], numbers[1]
set_1 = set()
set_2 = set()
for element in range(int(n)):
    number = int(input())
    set_1.add(number)

for element in range(int(m)):
    number = int(input())
    set_2.add(number)

for el in set_1:
    if el in set_2:
        print(el)
