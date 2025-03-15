from flask import Flask, render_template
from movie_data import movieList

app = Flask(__name__)

#Redirect homepage
@app.route('/')
def home():
    genres = movieList.keys()
    allMovies = [movie for movies in movieList.values() for movie in movies] #Flattens the sublists in dict. Ayaiai.
    return render_template('movies.html', genres=genres, movies=allMovies)

#Base page, will display all movies. 
@app.route('/movies')
def movies():
    genres = movieList.keys()
    allMovies = [movie for movies in movieList.values() for movie in movies] #Flattens the sublists in dict. Ayaiai.
    return render_template('movies.html', genres=genres, movies=allMovies)


#Route to display movies only in a specific genre
@app.route('/movies/<genre>')
def movies_via_genre(genre):
    #If the genre key is in the movie list, load the movies
    if genre in movieList:
        movies_Genre = movieList[genre] #Will return the list of movies in that genre
        return render_template('genre.html', genre=genre, movies=movies_Genre) #passes movies as list not dict
    else:
        return "Oops! No movies found for that genre!", 404


if __name__ == '__main__':
    app.run(debug=True)
