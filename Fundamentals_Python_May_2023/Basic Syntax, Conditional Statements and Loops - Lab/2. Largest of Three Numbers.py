import sys

num1 = int(input())
num2 = int(input())
num3 = int(input())
max_num = -sys.maxsize

if num1 > max_num:
    max_num = num1
if num2 > max_num:
    max_num = num2
if num3 > max_num:
    max_num = num3

print(max_num)