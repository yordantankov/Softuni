chiken_menu = int(input())
fish_menu = int(input())
vegetarian_menu = int(input())

price_for_chiken = chiken_menu * 10.35
price_for_fish = fish_menu * 12.40
price_for_vegetarian = vegetarian_menu * 8.15

total_price_for_menus = price_for_fish + price_for_chiken + price_for_vegetarian
price_for_desert= total_price_for_menus * 0.20

total_sum = total_price_for_menus + price_for_desert + 2.50

print(total_sum)