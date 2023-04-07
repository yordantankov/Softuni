easter_bread = int(input())
cores_eggs = int(input())
kg_cockies = int(input())

price_bread = easter_bread * 3.20
cockie_price = kg_cockies * 5.40
price_eggs = cores_eggs * 4.35
single_eggs = cores_eggs * 12
paint_for_eggs = single_eggs * 0.15

total = price_eggs + cockie_price + price_bread + paint_for_eggs

print(f'{total :.2f}')