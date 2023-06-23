num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
is_valid= True
if num_1 == 0 or num_2 == 0 or num_3 == 0:
   print("zero")

elif num_1 > 0 and num_2 > 0 and num_3 > 0:
    print('positive')

elif num_1 <0  and num_2 < 0 and num_3 < 0 :
    print('positive')

else:
    print('negative')