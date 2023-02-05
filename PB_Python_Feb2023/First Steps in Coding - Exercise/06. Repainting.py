needed_nylon = int(input())
needed_paint = int(input())
needed_thinner = int(input())
hours_for_work = int(input())

sum_for_nylon = (needed_nylon + 2) * 1.50
sum_for_paint = needed_paint * 14.50
sum_for_thinner = needed_thinner * 5.00

total_paint_price = sum_for_paint + (sum_for_paint * 0.10)

total = sum_for_nylon + total_paint_price + sum_for_thinner + 0.40

price_for_workers = total * 0.30
total_for_workers = price_for_workers * hours_for_work

absolute = total_for_workers + total

print (absolute)
