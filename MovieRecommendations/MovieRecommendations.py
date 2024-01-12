from abc import abstractproperty
from movies import movies
from sorts import bubble_sort

class MovieRecommendations:
    def __init__(self):
        self.favorites = []
        
    def greet(self):
        print("=====================================================")
        print("||   Welcome to the Movie Recommendation Engine!   ||")
        print("=====================================================")
    
    def options(self):
        print("                     MAIN MENU                       ")
        print("=====================================================")
        print("What would you like to do?")
        print("1. Search by title")
        print("2. Search by actor")
        print("3. Search by director")
        print("4. Search by genre")
        print("5. Search by director and actor")
        print("6. Search by director and genre")
        print("7. Search by actor and genre")
        print("8. Search by director, actor, and genre")
        print("9. View favorites")
        print("10. View all movies")
        print("11. Exit")
        print("=====================================================")
        return input("Enter a number: ")
    
    def display_result(self, result):
        count = 0
        if len(result) == 0:
            print("No results found")
        else:
            print("-----------------------------------------------------")
            for movie in result:
                count += 1
                print(f"{count}. {movie['movie_title']}")
                print(f"Directed by {movie['director_name']}")
                print(f"Starring {movie['actor_1_name']}, {movie['actor_2_name']}, {movie['actor_3_name']}")
                print(f"Genres: {movie['genres']}")
                print("-----------------------------------------------------")
        if len(result) > 1:
            print("Would you like to sort these movies?")
            print("1. Yes")
            print("2. No")
            sort_choice = input("Enter a number: ")
            if sort_choice == "1":
                result = self.sort_result(result)
                count = 0
                print("-----------------------------------------------------")
                for movie in result:
                    count += 1
                    print(f"{count}. {movie['movie_title']}")
                    print(f"Directed by {movie['director_name']}")
                    print(f"Starring {movie['actor_1_name']}, {movie['actor_2_name']}, {movie['actor_3_name']}")
                    print(f"Genres: {movie['genres']}")
                    print("-----------------------------------------------------")
                print("Would you like to add any of these movies to your favorites?")
                print("1. Yes")
                print("2. No")
                choice = input("Enter a number: ")
                if choice == "1":
                   if len(result) == 1:  
                    movie_choice = input("Enter the number of the movie you would like to add: ")
                    result = result[(int(movie_choice) - 1)]
                    self.add_to_favorites(result)
                    print("Movie added to favorites!")
                elif choice == "2":
                    self.search()
            elif sort_choice == "2":               
                print("Would you like to add any of these movies to your favorites?")
                print("1. Yes")
                print("2. No")
                choice = input("Enter a number: ")
                if choice == "1":
                    if len(result) == 1:
                        result = result[0]
                        self.add_to_favorites(result)
                        print("Movie added to favorites!")
                    else:    
                        movie_choice = input("Enter the number of the movie you would like to add: ")
                        result = result[(int(movie_choice) - 1)]
                        self.add_to_favorites(result)
                        print("Movie added to favorites!")
                elif choice == "2":
                    self.search()
    
    def add_to_favorites(self, result):
            self.favorites.append(result)
            
    def view_favorites(self):
        index = 0
        if len(self.favorites) == 0:
            print("-----------------------------------------------------") 
            print("             You have no favorites!                  ")
            print("-----------------------------------------------------") 
            return self.search()
        else:
            print("Your favorites:")
            for dictionary in self.favorites:
                print(str(index + 1) + ". " + dictionary['movie_title'])
                print(f"Directed by {dictionary['director_name']}")
                print(f"Starring {dictionary['actor_1_name']}, {dictionary['actor_2_name']}, {dictionary['actor_3_name']}")
                print(f"Genres: {dictionary['genres']}")
                print("-----------------------------------------------------")  
                index += 1     
        print("Would you like to sort your favorites?")
        print("1. Yes")
        print("2. No")
        choice = input("Enter a number: ")
        if choice == "1":
            self.sort_result(self.favorites)
        elif choice == "2":
            self.search()
        
    
    def sort_result(self, result):
        print("How would you like to sort these movies?")
        print("1. By title")
        print("2. By actor")
        print("3. By director")
        print("4. By genre")
        print("5. By director and actor")
        print("6. By director and genre")
        print("7. By actor and genre")
        print("8. By director, actor, and genre")
        print("9. Return to main menu")
        choice = input("Enter a number: ")
        while choice != 9:
            if choice == "1":
                result = bubble_sort(result, self.by_title)        
            elif choice == "2":
                result = bubble_sort(result, self.by_actor)
            elif choice == "3":
                result = bubble_sort(result, self.by_director)
            elif choice == "4":
                result = bubble_sort(result, self.by_genre)
            elif choice == "5":
                result = bubble_sort(result, self.by_director_and_actor)
            elif choice == "6":
                result = bubble_sort(result, self.by_director_and_genre)
            elif choice == "7":
                result = bubble_sort(result, self.by_actor_and_genre)
            elif choice == "8":
                result = bubble_sort(result, self.by_director_actor_and_genre)
            return result
            #self.view_favorites()
            #elif choice == "9":

        self.search()
            #return
            
        #self.view_favorites()
        
    def search(self):
        choice = self.options()
        while choice != "11":
            if choice == "1":
                self.search_by_title()
            elif choice == "2":
                self.search_by_actor()
            elif choice == "3":
                self.search_by_director()
            elif choice == "4":               
                self.display_result(self.search_by_genre())
            elif choice == "5":
                self.search_by_director_and_actor()
            elif choice == "6":
                self.search_by_director_and_genre()
            elif choice == "7":
                self.search_by_actor_and_genre()
            elif choice == "8":
                self.search_by_director_actor_and_genre()
            elif choice == "9":
                self.view_favorites()
            elif choice == "10":
                self.display_result(movies)
        print("Thank you for using the Movie Recommendation Engine!")
        exit()
        
        
    #SEARCH FUNCTIONS
    def search_by_title(self):
        result = []
        title = input("Enter a title: ")
        for movie in movies:
            if movie['movie_title_lower'] == title.lower():
                result.append(movie)
        self.display_result(result)
    
    def search_by_actor(self):
        result = []
        actor = input("Enter an actor: ")
        for movie in movies:
            if movie['actor_1_lower'] == actor.lower() or movie['actor_2_lower'] == actor.lower() or movie['actor_3_lower'] == actor.lower():
                result.append(movie)
        self.display_result(result)

    def search_by_director(self):
        result = []
        director = input("Enter a director: ")
        for movie in movies:
            if movie['director_lower'] == director.lower():
                result.append(movie)
        self.display_result(result)
                
    def search_by_genre(self):
        result = []
        genre = input("Enter a genre: ")
        for movie in movies:
            if genre.lower() in movie['genres_lower']:
                result.append(movie)
        return result
        #self.display_result(result)
        
    def search_by_director_and_actor(self):
        result = []
        director = input("Enter a director: ")
        actor = input("Enter an actor: ")
        for movie in movies:
            if movie['director_lower'] == director.lower() and (movie['actor_1_lower'] == actor.lower() or movie['actor_2_lower'] == actor.lower() or movie['actor_3_lower'] == actor.lower()):
                result.append(movie)
        self.display_result(result)
        
    def search_by_director_and_genre(self):
        result = []
        director = input("Enter a director: ")
        genre = input("Enter a genre: ")
        for movie in movies:
            if movie['director_lower'] == director.lower() and genre.lower() in movie['genres_lower']:
                result.append(movie)
        self.display_result(result)
    
    def search_by_actor_and_genre(self):
        result = []
        actor = input("Enter an actor: ")
        genre = input("Enter a genre: ")
        for movie in movies:
            if (movie['actor_1_lower'] == actor.lower() or movie['actor_2_lower'] == actor.lower() or movie['actor_3_lower'] == actor.lower()) and genre.lower() in movie['genres_lower']:
                result.append(movie)
        self.display_result(result)
        
    def search_by_director_actor_and_genre(self):
        result = []
        director = input("Enter a director: ")
        actor = input("Enter an actor: ")
        genre = input("Enter a genre: ")
        for movie in movies:
            if movie['director_lower'] == director.lower() and (movie['actor_1_lower'] == actor.lower() or movie['actor_2_lower'] == actor.lower() or movie['actor_3_lower'] == actor.lower()) and genre.lower() in movie['genres_lower']:
                result.append(movie)
        self.display_result(result)
       
    #COMPARISON FUNCTIONS
    def by_title(self, movie_a, movie_b):
        return movie_a['movie_title_lower'] > movie_b['movie_title_lower']

    def by_actor(self, movie_a, movie_b):
        return movie_a['actor_1_lower'] > movie_b['actor_1_lower']

    def by_director(self, movie_a, movie_b):
        return movie_a['director_lower'] > movie_b['director_lower']

    def by_genre(self, movie_a, movie_b):
        return movie_a['genres_lower'] > movie_b['genres_lower']
    
    def by_director_and_actor(self, movie_a, movie_b):
        if movie_a['director_lower'] == movie_b['director_lower']:
            return movie_a['actor_1_lower'] > movie_b['actor_1_lower']
        else:
            return movie_a['director_lower'] > movie_b['director_lower']
    
    def by_director_and_genre(self, movie_a, movie_b):
        if movie_a['director_lower'] == movie_b['director_lower']:
            return movie_a['genres_lower'] > movie_b['genres_lower']
        else:
            return movie_a['director_lower'] > movie_b['director_lower']
    
    def by_actor_and_genre(self, movie_a, movie_b):
        if movie_a['actor_1_lower'] == movie_b['actor_1_lower']:
            return movie_a['genres_lower'] > movie_b['genres_lower']
        else:
            return movie_a['actor_1_lower'] > movie_b['actor_1_lower']
        
    def by_director_actor_and_genre(self, movie_a, movie_b):
        if movie_a['director_lower'] == movie_b['director_lower']:
            if movie_a['actor_1_lower'] == movie_b['actor_1_lower']:
                return movie_a['genres_lower'] > movie_b['genres_lower']
            else:
                return movie_a['actor_1_lower'] > movie_b['actor_1_lower']
        else:
            return movie_a['director_lower'] > movie_b['director_lower']

#RUN PROGRAM
engine = MovieRecommendations()
engine.greet()
engine.search()

