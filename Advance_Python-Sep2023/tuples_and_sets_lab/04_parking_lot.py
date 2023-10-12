n = int(input())
parking_lot = set()
for _ in range(n):
    car, plate = input().split(", ")
    if car == "IN":
        parking_lot.add(plate)
    elif car == "OUT":
        parking_lot.remove(plate)

if parking_lot:
    for car in parking_lot:
        print(car)
else:
    print("Parking Lot is Empty")