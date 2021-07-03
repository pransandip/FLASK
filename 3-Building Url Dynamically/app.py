## Building URL Dynamically
## Variable Rules & URL Building

from flask import Flask,redirect,url_for

app=Flask(__name__)

@app.route('/')
def welcome():
    return '<html><body><h2>Welcome to my App</h2></body></html>'

@app.route('/success/<int:score>')
def success(score):
    return "App succeed and App score is " + str(score)
    
@app.route('/fail/<int:score>')
def fail(score):
    return 'App Failed and App score is '+str(score)

## Result checker
@app.route('/results/<int:marks>')
def results(marks):
    result=""
    if marks<50:
        result='fail'
    else:
        result='success'
    return redirect(url_for(result,score=marks))


if __name__=="__main__":
    app.run(debug=True)