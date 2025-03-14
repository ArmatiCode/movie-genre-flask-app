from flask import Flask, render_template

app = Flask(__name__)

@app.route('/movies')
def movies():
    return render_template('movies.html')

@app.route('/movies/<genre>')


if __name__ == '__main__':
    app.run(debug=True)
