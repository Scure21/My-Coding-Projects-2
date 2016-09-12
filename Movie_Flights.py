def Movies_Flight(flight_length,movie_lengths):
    #flight_length = 240  (4h)
    #movie_legths = [140,90,130,100,60]
    
    
    
    for index in xrange(len(movie_lengths)):
            current_movie, rest_of_movies = movie_lengths[index], movie_lengths[index+1:]
            print current_movie, rest_of_movies
            second_movie = (flight_length) - current_movie
            if second_movie in rest_of_movies:
                return True
            else:
                return False
        