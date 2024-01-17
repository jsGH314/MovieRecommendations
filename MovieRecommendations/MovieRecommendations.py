from abc import abstractproperty
from movies import movies, AutocompleteFunctions
from sorts import bubble_sort


class MovieRecommendations:
    def __init__(self):
        self.favorites = []
        self.reccomendations = []
        
    def greet(self):
        print("=====================================================")
        print("||   Welcome to the Movie Recommendation Engine!   ||")
        print("=====================================================")
    
    def main_menu(self):
        print("=====================================================")
        print("                     MAIN MENU                       ")
        print("=====================================================")
        print("What would you like to do?")
        print("1. Search all movies")
        print("2. View favorites")
        print("3. View all movies")
        print("4. Exit")
        print("=====================================================")
        choice = input("Enter a number: ")      
        if choice == "1":
            return self.search()
        elif choice == "2":
            return self.view_favorites()
        elif choice == "3":
            return self.display_result(movies)
        elif choice == "4":
            print("Thank you for using the Movie Recommendation Engine!")
            exit()
            

    def search(self, movie_list = movies):
        print("=====================================================")
        print("                     SEARCH                          ")
        print("=====================================================")
        print("How would you like to search?")
        print("1. Search by title")
        print("2. Search by actor")
        print("3. Search by director")
        print("4. Search by genre")
        print("5. Search by director and actor")
        print("6. Search by director and genre")
        print("7. Search by actor and genre")
        print("8. Search by director, actor, and genre")
        print("9. Exit to main menu")
        print("=====================================================")
        choice = input("Enter a number: ")
        while choice != "9":
            if choice == "1":
                self.search_by_title(movie_list)
            elif choice == "2":
                self.search_by_actor(movie_list)
            elif choice == "3":
                self.search_by_director(movie_list)
            elif choice == "4":               
                self.search_by_genre(movie_list)
            elif choice == "5":
                self.search_by_director_and_actor(movie_list)
            elif choice == "6":
                self.search_by_director_and_genre(movie_list)
            elif choice == "7":
                self.search_by_actor_and_genre(movie_list)
            elif choice == "8":
                self.search_by_director_actor_and_genre(movie_list)
        self.main_menu()       
    
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
                        result = result[0]
                        self.add_to_favorites(result)
                        print("Movie added to favorites!")
                        self.main_menu()
                    else:    
                        movie_choice = input("Enter the number of the movie you would like to add: ")
                        result = result[(int(movie_choice) - 1)]
                        self.add_to_favorites(result)
                        print("Movie added to favorites!")
                        self.main_menu()
                elif choice == "2":
                    self.main_menu()
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
                        self.main_menu()
                    else:    
                        movie_choice = input("Enter the number of the movie you would like to add: ")
                        result = result[(int(movie_choice) - 1)]
                        self.add_to_favorites(result)
                        print("Movie added to favorites!")
                        self.main_menu()
                elif choice == "2":
                    self.main_menu()
        else:
            print("Would you like to add this movie to your favorites?")
            print("1. Yes")
            print("2. No")
            choice = input("Enter a number: ")
            if choice == "1":
                result = result[0]
                self.add_to_favorites(result)
                print("Movie added to favorites!")
                self.main_menu()
            elif choice == "2":
                self.main_menu()
            
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
            print("-----------------------------------------------------") 
            print("                 Your favorites:                     ")
            print("-----------------------------------------------------") 
            for dictionary in self.favorites:
                print(str(index + 1) + ". " + dictionary['movie_title'])
                print(f"Directed by {dictionary['director_name']}")
                print(f"Starring {dictionary['actor_1_name']}, {dictionary['actor_2_name']}, {dictionary['actor_3_name']}")
                print(f"Genres: {dictionary['genres']}")
                print("-----------------------------------------------------")  
                index += 1     
        print("What would you like to do?")
        print("1. Search Favorites")
        print("2. Sort Favorites")
        print("3. Generate Recommendations")
        print("4. Return to main menu")
        choice = input("Enter a number: ")
        if choice == "1":
            self.search(self.favorites)
        elif choice == "2":
            self.sort_result(self.favorites)
        elif choice == "3":
            print("Which movie would you like to generate recommendations for?")
            rec_choice = input("Enter a number: ")
            selected_movie = self.favorites[(int(rec_choice) - 1)]
            self.generate_recommendations(selected_movie)
        elif choice == "4":
            self.main_menu()
    
    def sort_result(self, result):
        print("How would you like to sort these movies?")
        print("1. By title ascending")
        print("2. By actor ascending")
        print("3. By director ascending")
        print("4. By genre ascending")
        print("5. By director and actor ascending")
        print("6. By director and genre ascending")
        print("7. By actor and genre ascending")
        print("8. By director, actor, and genre ascending")
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
        self.main_menu()

    def generate_recommendations(self, selected_movie):
        print("How would you like to generate recommendations?")
        print("1. By genre")
        print("2. By actor")
        print("3. By director")
        print("4. Return to main menu")
        choice = input("Enter a number: ")
        while choice != "4":
            print("-----------------------------------------------------")
            print("                 Recommendations:                    ")
            print("-----------------------------------------------------")
            if choice == "1":
                self.generate_recommendations_by_genre(selected_movie)
            elif choice == "2":
                self.generate_recommendations_by_actor(selected_movie)
            elif choice == "3":
                self.generate_recommendations_by_director(selected_movie)
        self.main_menu()

    def generate_recommendations_by_genre(self, selected_movie):
        result = []
        genres = selected_movie['genres_seperate']
        for movie in movies:
            if any(genre in movie['genres_seperate'] for genre in genres):
                result.append(movie)
        self.display_result(result)
        
    def generate_recommendations_by_actor(self, selected_movie):
        result = []
        actor = selected_movie['actor_1_name'].lower()
        for movie in movies:
            if movie['actor_1_lower'].startswith(actor.lower()) or movie['actor_2_lower'].startswith(actor.lower()) or movie['actor_3_lower'].startswith(actor.lower()):
                result.append(movie)
        self.display_result(result)
        
    def generate_recommendations_by_director(self, selected_movie):
        result = []
        director = selected_movie['director_name'].lower()
        for movie in movies:
            if movie['director_lower'].startswith(director.lower()):
                result.append(movie)
        self.display_result(result)
                                      
    #SEARCH FUNCTIONS
    def search_by_title(self, movie_list):
        result = []
        title = input("Enter a title (full or first part): ")
        for movie in movie_list:
            if movie['movie_title_lower'].startswith(title.lower()):
                result.append(movie)
        self.display_result(result)
        
    
    def search_by_actor(self, movie_list):
        result = []
        actor = input("Enter an actor's name (full or first part): ")
        for movie in movie_list:
            if movie['actor_1_lower'].startswith(actor.lower()) or movie['actor_2_lower'].startswith(actor.lower()) or movie['actor_3_lower'].startswith(actor.lower()):
                result.append(movie)
        self.display_result(result)

    def search_by_director(self, movie_list):
        result = []
        director = input("Enter a director's name (full or first part): ")
        for movie in movie_list:
            if movie['director_lower'].startswith(director.lower()):
                result.append(movie)
        self.display_result(result)
                
    def search_by_genre(self, movie_list):
        result = []
        genre = input("Enter a genre (full or first part): ")
        for movie in movie_list:
            if movie['genres_lower'].startswith(genre.lower()):
                result.append(movie)
        #return result
        self.display_result(result)
             
        
    def search_by_director_and_actor(self, movie_list):
        result = []
        director = input("Enter a director (full or first part): ")
        actor = input("Enter an actor (full or first part): ")
        for movie in movie_list:
            if movie['director_lower'].startswith(director.lower()) and (movie['actor_1_lower'].startswith(actor.lower()) or movie['actor_2_lower'].startswith(actor.lower()) or movie['actor_3_lower'].startswith(actor.lower())):
                result.append(movie)
        self.display_result(result)
        
    def search_by_director_and_genre(self, movie_list):
        result = []
        director = input("Enter a director (full or first part): ")
        genre = input("Enter a genre (full or first part): ")
        for movie in movie_list:
            if movie['director_lower'].startswith(director.lower()) and movie['genres_lower'].startswith(genre.lower()):
                result.append(movie)
        self.display_result(result)
    
    def search_by_actor_and_genre(self, movie_list):
        result = []
        actor = input("Enter an actor (full or first part): ")
        genre = input("Enter a genre (full or first part): ")
        for movie in movie_list:
            if (movie['actor_1_lower'].startswith(actor.lower()) or movie['actor_2_lower'].startswith(actor.lower()) or movie['actor_3_lower'].startswith(actor.lower())) and movie['genres_lower'].startswith(genre.lower()):
                result.append(movie)
        self.display_result(result)
        
    def search_by_director_actor_and_genre(self, movie_list):
        result = []
        director = input("Enter a director (full or first part): ")
        actor = input("Enter an actor (full or first part): ")
        genre = input("Enter a genre (full or first part): ")
        for movie in movie_list:
            if movie['director_lower'].startswith(director.lower()) and (movie['actor_1_lower'].startswith(actor.lower()) or movie['actor_2_lower'].startswith(actor.lower()) or movie['actor_3_lower'].startswith(actor.lower())) and movie['genres_lower'].startswith(genre.lower()):
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
engine.main_menu()

