bottles_qty = int(input())
preparat_ml = bottles_qty * 750
charge_count = 0
clean_plates = 0
clean_pots = 0
preparat_for_plates = 0
preparat_for_pots = 0

while True:

    dishes_qty = input()
    if dishes_qty == "End" :
        break

    charge_count += 1
    dishes_qty = int(dishes_qty)

    if charge_count < 3:
        preparat_for_plates = dishes_qty * 5
        preparat_ml -= preparat_for_plates
        clean_plates += dishes_qty

    else:
        preparat_for_pots = dishes_qty * 15
        preparat_ml -= preparat_for_pots
        charge_count = 0
        clean_pots += dishes_qty

    if preparat_ml < 0:
        print(f"Not enough detergent, {abs(preparat_ml)} ml. more necessary!")
        exit()

print(f'Detergent was enough!')
print(f'{clean_plates} dishes and {clean_pots} pots were washed.')
print(f'Leftover detergent {preparat_ml} ml.')


