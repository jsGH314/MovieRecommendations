import csv

my_file = open('movie.csv', 'r')
reader = csv.DictReader(my_file)
movies = list()
for movie in reader:
    movie['director_lower'] = movie['director_name'].lower()
    movie['actor_1_lower'] = movie['actor_1_name'].lower()
    movie['actor_2_lower'] = movie['actor_2_name'].lower()
    movie['actor_3_lower'] = movie['actor_3_name'].lower()
    movie['genres_lower'] = movie['genres'].lower()
    movie['movie_title_lower'] = movie['movie_title'].lower()
    movies.append(movie)
 