from flask import Flask
## WSGI Application
app=Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to my first FLASK App 2'
    
@app.route('/members')
def members():
    return 'Welcome to my first FLASK App 2 members page'

if __name__=='__main__':
    app.run(debug=True)