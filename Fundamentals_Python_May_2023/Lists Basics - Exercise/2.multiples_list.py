factor = int(input())
count = int(input())
my_list = []
for i in range(1,count+1):
    new_num = factor * i
    my_list.append(new_num)

print(my_list)