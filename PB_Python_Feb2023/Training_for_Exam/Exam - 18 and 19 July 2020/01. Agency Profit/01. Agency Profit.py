avio_company = input()
olds_tickets = int(input())
kids_tickets = int(input())
price_for_olds = float(input())
taxes = float(input())

price_kid_ticket = price_for_olds - (price_for_olds  * 0.70)
total_kids = price_kid_ticket + taxes
price_old_ticket = price_for_olds + taxes
profit = (kids_tickets * total_kids) + (olds_tickets * price_old_ticket)

total = profit * 0.20

print(f"The profit of your agency from {avio_company} tickets is {total :.2f} lv.")