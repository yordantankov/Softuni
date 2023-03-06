total = 0
command = input()
increase = 0
while command != 'NoMoreMoney':
    command = float(command)
    if command < 0:
        print('Invalid operation!')
        print(f'Total: {total :.2f}')
        exit()
    total += float(command)
    increase = float(command)
    print(f'Increase: {increase :.2f}')
    command = input()

print(f'Total: {total :.2f}')