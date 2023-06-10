n = int(input())
even_lst = []
odd_lst = []
negative_lst = []
positive_lst = []

for i in range(n):
    num = int(input())

    if num % 2 == 0:
        even_lst.append(num)
    if num % 2 != 0:
        odd_lst.append(num)
    if num >= 0 :
        positive_lst.append(num)
    if num < 0 :
        negative_lst.append(num)

command = input()

if command == "even":
    print(even_lst)
elif command == "odd":
    print(odd_lst)
elif command == "negative":
    print(negative_lst)
elif command == "positive":
    print(positive_lst)
