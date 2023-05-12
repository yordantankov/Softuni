wanted_budjet = float(input())
price = 0
total = 0
while True:
    coctail = input()
    if coctail == "Party!":
        break

    count_coctails = int(input())

    price = len(coctail)

    sum =  price * count_coctails

    if sum % 2 != 0:
        sum -= sum * 0.25

    total += sum

    if total >= wanted_budjet:
        print('Target acquired.')
        print(f'Club income - {total :.2f} leva.')
        exit()

diff = wanted_budjet - total
print(f'We need {diff :.2f} leva more.')
print(f'Club income - {total :.2f} leva.')