import math

price_of_skumriq = float(input())
price_of_caca = float(input())
kg_of_palamut = float(input())
kg_of_safrid = float(input())
kg_of_midi = int (input())
price_of_midi = 7.50

price_of_palamut = (price_of_skumriq + (price_of_skumriq * 0.60)) * kg_of_palamut
total_price_for_midi = price_of_midi * kg_of_midi
price_of_safrid = (price_of_caca + (price_of_caca * 0.80)) * kg_of_safrid

total = price_of_palamut +price_of_safrid + total_price_for_midi
print(f"{total :.2f}")
