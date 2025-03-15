from flask import Flask, render_template
from movie_data import movieList

app = Flask(__name__)

#Redirect homepage
@app.route('/')
def home():
    return render_template('movies.html')

#Base route - Will display all movies and genres
@app.route('/movies')
def movies():
    return render_template('movies.html', genres=movieList.values())


#Route to display movies only in a specific genre
@app.route('/movies/<genre>')
def movies_via_genre(genre):
    #If the genre key is in the movie list, load the movies
    if genre in movieList:
        movies_Genre = movieList[genre] #Will return the list of movies in that genre
        return render_template('genre.html', genre=genre, movies=movies_Genre) #passes movies as list not dict
    else:
        return "Oops! No movies found for that genre!"


if __name__ == '__main__':
    app.run(debug=True)
