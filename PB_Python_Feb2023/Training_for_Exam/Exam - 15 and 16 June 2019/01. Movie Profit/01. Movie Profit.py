movie_name = input()
days_qty = int(input())
tickets_qty = int(input())
price_ticket = float(input())
percent_for_cinema = int(input())

price_for_day = tickets_qty * price_ticket
total_earn = price_for_day * days_qty
money_for_cinema = total_earn * percent_for_cinema / 100

profit = total_earn - money_for_cinema

print(f"The profit from the movie {movie_name} is {profit :.2f} lv.")