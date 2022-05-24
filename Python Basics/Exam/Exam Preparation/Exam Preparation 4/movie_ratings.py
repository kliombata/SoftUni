import sys

num_films = int(input())
current_movie_name = ""
current_movie_ranking = 0

highest_rating = -sys.maxsize
lowest_rating = sys.maxsize
highest_rated_movie = ""
lowest_rated_movie = ""
rating_counter = 0
average_rating = 0
movie_counter = 0

while num_films >= 0:

    current_movie_name = input()
    current_movie_ranking = float(input())
    rating_counter += current_movie_ranking

    if current_movie_ranking > highest_rating:
        highest_rating = current_movie_ranking
        highest_rated_movie = current_movie_name

    if current_movie_ranking < lowest_rating:
        lowest_rating = current_movie_ranking
        lowest_rated_movie = current_movie_name

    num_films -= 1

average_rating = rating_counter / num_films

print(f"{highest_rated_movie} is with highest rating: {highest_rating:.2d}")
print(f"{lowest_rated_movie} is with lowest rating: {lowest_rating:.2d}")
print(f"Average rating: {average_rating:.2d}")
