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

def count_movies_by_genre(movies):
    def count_genre(genre):
        genre_count = len(list(filter(lambda movie: movie["genre"] == genre, movies)))
        return genre, genre_count
    genre_counts = dict(map(count_genre, set(movie["genre"] for movie in movies)))
    return genre_counts

def average_rating_by_year(movies):
    def average_by_year(year):
        year_movies = list(filter(lambda movie: movie["year"] == year, movies))
        if not year_movies:
            return year, 0.0
        total_rating = reduce(lambda x, y: x + y["rating"], year_movies, 0)
        avg_rating = total_rating / len(year_movies)
        return year, avg_rating
    avg_ratings = dict(map(average_by_year, set(movie["year"] for movie in movies)))
    return avg_ratings

def highest_rated_movie(movies):
    return max(movies, key=lambda movie: movie["rating"])

def find_movie_by_title(movies):
    def find_movie(title):
        return next(filter(lambda movie: movie["title"] == title, movies), None)
    return find_movie

def menu():
    while True:
        print("\nPilih tugas yang ingin dilakukan:")
        print("1. Menghitung jumlah film berdasarkan genre")
        print("2. Menghitung rata-rata rating film berdasarkan tahun rilis")
        print("3. Menemukan film dengan rating tertinggi")
        print("4. Cari judul film untuk menampilkan informasi rating, tahun rilis, dan genre")
        print("5. Selesai")

        choice = input("Masukkan nomor tugas (1/2/3/4/5): ")

        if choice == "1":
            genre_counts = count_movies_by_genre(movies)
            print("Jumlah film berdasarkan genre:")
            print(genre_counts)
        elif choice == "2":
            avg_ratings = average_rating_by_year(movies)
            print("Rata-rata Rating Film Berdasarkan Tahun Rilis:")
            print(avg_ratings)
        elif choice == "3":
            highest_rated = highest_rated_movie(movies)
            print(f"Film dengan rating tertinggi:")
            print(f"Judul: {highest_rated['title']}")
            print(f"Rating: {highest_rated['rating']}")
            print(f"Tahun Rilis: {highest_rated['year']}")
            print(f"Genre: {highest_rated['genre']}")
        elif choice == "4":
            selected_movie_title = input("Masukkan judul film yang ingin ditampilkan: ")
            find_movie = find_movie_by_title(movies)
            selected_movie = find_movie(selected_movie_title)
            if selected_movie:
                print(f"Informasi Film: {selected_movie['title']}")
                print(f"Rating: {selected_movie['rating']}")
                print(f"Tahun Rilis: {selected_movie['year']}")
                print(f"Genre: {selected_movie['genre']}")
            else:
                print("Film dengan judul tersebut tidak ditemukan.")
        elif choice.lower() == "5":
            break
        else:
            print("Pilihan tidak valid. Silakan pilih tugas yang sesuai.")

menu()
