budjet = float(input())
GPU_qty = int(input())
CPU_qty = int(input())
RAM_qty = int (input())

GPU_price= GPU_qty * 250
CPU_price = CPU_qty * (GPU_price * 0.35)
RAM_price= RAM_qty * (GPU_price * 0.10)

total_price = GPU_price + CPU_price + RAM_price

if GPU_qty > CPU_qty:
    total_price -= total_price * 0.15

if total_price <= budjet:
    budjet -= total_price
    print (f'You have {budjet :.2f} leva left!')
else:
    total_price -= budjet
    print(f'Not enough money! You need {total_price :.2f} leva more!')