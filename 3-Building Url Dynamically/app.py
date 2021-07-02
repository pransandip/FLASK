## Building URL Dynamically
## Variable Rules & URL Building

from flask import Flask

app=Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to my App'

@app.route('/success/<int:score>')
def score():
    return 'Welcome to my App'


if __name__=="__main__":
    app.run(debug=True)