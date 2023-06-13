numbers_str = input().split()
numbers = []

for num in numbers_str:
    numbers.append(int(num))

remover = int(input())

for _ in range(remover):
    numbers.remove(min(numbers))

print(*numbers, sep=", ")