number = float(input())
while number >= 0:
    num_x2 = number * 2
    print(f"Result: {num_x2:.2f}")
    number = float(input())
else:
    print("Negative number!")