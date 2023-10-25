__author__ = "rizkyhaksono"
__copyright__ = "Copyright 2023, Malang"

from functools import reduce

movies = [
    {"title": "Avengers: Endgame", "year": 2019, "rating": 8.4, "genre": "Action"},
    {"title": "Parasite", "year": 2019, "rating": 8.6, "genre": "Drama"},
    {"title": "Nomadland", "year": 2020, "rating": 7.3, "genre": "Drama"},
    {"title": "Dune", "year": 2021, "rating": 7.9, "genre": "Sci-Fi"},
    {"title": "Spider-Man: No Way Home", "year": 2021, "rating": 7.6, "genre": "Action"},
    {"title": "The French Dispatch", "year": 2021, "rating": 7.0, "genre": "Comedy"},
    {"title": "A Quiet Place Part II", "year": 2020, "rating": 7.4, "genre": "Horror"},
    {"title": "No Time to Die", "year": 2021, "rating": 6.8, "genre": "Action"},
    {"title": "The Power of the Dog", "year": 2021, "rating": 7.3, "genre": "Drama"},
    {"title": "Eternals", "year": 2021, "rating": 6.4, "genre": "Action"},
    {"title": "The Last Duel", "year": 2021, "rating": 7.0, "genre": "Drama"},
]

# Menampilkan data dari film yang dipilih (data berisi title, year, rating, dan genre)
selected_movies = list(map(lambda x: {"title": x["title"], "year": x["year"], "rating": x["rating"], "genre": x["genre"]}, movies))
print("Data Film yang Dipilih:")
print(selected_movies)

# Jumlah film berdasarkan genre
def count_movies_by_genre(genre):
    return len(list(filter(lambda x: x["genre"] == genre, movies)))

genres = set(map(lambda x: x["genre"], movies))
genre_counts = {genre: count_movies_by_genre(genre) for genre in genres}
print("Jumlah Film Berdasarkan Genre:")
print(genre_counts)

# Rata-rata rating film berdasarkan tahun rilis
def average_rating_by_year(year):
    movies_in_year = list(filter(lambda x: x["year"] == year, movies))
    total_ratings = reduce(lambda x, y: x + y["rating"], movies_in_year, 0)
    return total_ratings / len(movies_in_year) if len(movies_in_year) > 0 else 0.0

years = set(map(lambda x: x["year"], movies))
average_ratings = {year: average_rating_by_year(year) for year in years}
print("Rata-rata Rating Film Berdasarkan Tahun Rilis:")
print(average_ratings)

# Film dengan rating tertinggi
highest_rated_movie = max(movies, key=lambda x: x["rating"])
print("Film dengan Rating Tertinggi:")
print(highest_rated_movie)
