year_tax = int(input())

price_for_shoes = year_tax - (year_tax * 0.40)
price_for_clothes = price_for_shoes -(price_for_shoes * 0.20)
price_for_ball = price_for_clothes / 4
price_for_accessories = price_for_ball /5

total = year_tax + price_for_shoes + price_for_accessories + price_for_ball + price_for_clothes

print (total)
