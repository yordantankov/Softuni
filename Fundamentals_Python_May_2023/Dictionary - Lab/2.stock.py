product = input().split()
products = { }
for element in range(0, len(product), 2):
    stock = product[element]
    value = product[element + 1]
    products[stock] = int(value)

product_to_search = input().split()

for element in product_to_search:
    if element in products:
        print(f"We have {products[element]} of {element} left")
    else:
        print(f"Sorry, we don't have {element}")
