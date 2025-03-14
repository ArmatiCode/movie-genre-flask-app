from flask import Flask

app = Flask(__name__)

@app.route('/')
def placeHolder():
    return "Let's begin coding =)"

if __name__ == '__main__':
    app.run(debug=True)
