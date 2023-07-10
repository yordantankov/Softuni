products = {}
command = input()
while command != "statistics":
    command = command.split(": ")
    key, value = command[0], int(command[1])
    if key in products:
        products[key] += value
        command = input()
        continue
    products[key] = value
    command = input()

print("Products in stock:")
for element,quantity in products.items():
    print(f"- {element}: {quantity}")

print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")