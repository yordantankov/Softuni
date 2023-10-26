def numbers(*args):
    positive_sums = 0
    negative_sums = 0
    for element in args:
        for el in element:
            if int(el) >= 0:
                positive_sums += int(el)
            else:
                negative_sums += int(el)

    if abs(negative_sums) > positive_sums:
        print(negative_sums)
        print(positive_sums)
        print("The negatives are stronger than the positives")
    else:
       print(negative_sums)
       print(positive_sums)
       print("The positives are stronger than the negatives")


some_numbers = [int(x) for x in input().split()]

numbers(some_numbers)
