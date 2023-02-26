n = int(input())
odd_num = 0
even_num = 0
for i in range (1, n+1 ):
    num = int(input())
    if i % 2 == 0:
        even_num += num
    else:
        odd_num += num

if even_num == odd_num:
    print('Yes')
    print(f'Sum = {even_num}')
else:
    diff = abs(even_num - odd_num)
    print('No')
    print(f'Diff = {diff}')