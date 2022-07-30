"""BASIC FLASK APP ARCHITECTURE.
1.Import Flask class from the flask module.
2.Initialize the flask app.
3.Set the route to the home/index page.
4.Write a view function.
5.Set-up the server.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1> Hello Sexy Ms Dollar Baby, Welcome to Flask!</h1>'

if __name__ == '__main__':
    app.run(debug = True)