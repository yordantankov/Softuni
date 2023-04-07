price_flour_kg = float(input())
kg_flour = float(input())
kg_sugar = float(input())
cores_eggs = int(input())
package_maq = int(input())

total_price_flour = price_flour_kg * kg_flour

price_sugar_1kg = price_flour_kg - (price_flour_kg * 0.25)
sugar_price = price_sugar_1kg * kg_sugar

core_prices_eggs = price_flour_kg + (price_flour_kg * 0.10)
eggs_price = core_prices_eggs * cores_eggs

price_for_maq = price_sugar_1kg - (price_sugar_1kg * 0.80)
price_maq = price_for_maq * package_maq

total = price_maq + eggs_price + sugar_price + total_price_flour

print(f'{total :.2f}')