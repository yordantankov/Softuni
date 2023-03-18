rent = float(input())

cake = rent * 0.20
drinks = cake - (cake * 0.45)
animator = rent / 3

total = rent + drinks + cake + animator

print(f'{total :.1f}')