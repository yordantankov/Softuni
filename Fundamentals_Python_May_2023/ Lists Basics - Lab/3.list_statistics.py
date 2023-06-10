n = int(input())

positive_list = []
negative_list = []
negative_sum = 0
positive_count = 0
for i in range(n):
    num = int(input())

    if num >= 0 :
        positive_list.append(num)
        positive_count += 1
    else:
        negative_list.append(num)
        negative_sum += num

print(positive_list)
print(negative_list)

print(f'Count of positives: {positive_count}')
print(f'Sum of negatives: {negative_sum}')
