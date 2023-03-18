import sys

movies_qty = int(input())
lowest_reiting = sys.maxsize
highest_reiting = -sys.maxsize
movie_with_highest_rating = ""
movie_with_lowest_rating = ""
total_reitings = 0

for i in range(0 , movies_qty):
    movie_name = input()
    reiting = float(input())
    total_reitings += reiting

    if reiting > highest_reiting:
        movie_with_highest_rating = movie_name
        highest_reiting = reiting

    if reiting < lowest_reiting:
        movie_with_lowest_rating = movie_name
        lowest_reiting = reiting

print(f'{movie_with_highest_rating} is with highest rating: {highest_reiting :.1f}')
print(f'{movie_with_lowest_rating} is with lowest rating: {lowest_reiting :.1f}')

average_rating = total_reitings / movies_qty
print(f'Average rating: {average_rating :.1f}')