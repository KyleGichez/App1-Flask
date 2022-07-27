# App1-Flask
This is my first flask app I have coded while learning to set a basic flask app. Here is the Flask installation process.
```
python3.6 -m venv --without-pip virtual =====>>> Setting up a vitual environment.(virtual)
source virtual/bin/activate =======>>>> Activating the virtual environment.
(virtual)sexymsdollarbaby@SexyMsDollarBaby:$   =========>>>> Confirm if the virtual environment has been set correctly by checking the start of your terminal.
(virtual)sexymsdollarbaby@SexyMsDollarBaby:$ deactivate  ==========>>>> Deactivate the virtual environment.
curl https://bootstrap.pypa.io/get-pip.py | python   =========>>>> Install the latest version of pip.
pip install flask =======>>>> Install Flask into our project.

````

## Basic Flask App Architecture
From the flask module import Flask class.
```
from flask import Flask
```

Create an app instance using the name variable.

```app = Flask(__name__)

```

Routes in flask are defined using the @app.route() decorator.
```
@app.route('/') - indicates the homepage.
````
A view function is the handler of the route.
```
@app.route('/')
def index():
    return '<h1>Hello Sexy Ms Dollar Baby, Welcome to Flask!'</h1>
```

Setting up the server
```
if __name__ == '__main__':
app.run(debug = True)
```
The run() method is used to launch the flask development server.
Always set the debug mode to True - Activates the debugger and the reloader.
