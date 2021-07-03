## Integrate HTML with Flask
## HTTP verb GET and POST

from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res='Passed'
    else:
        res='Failed'

    return render_template('result.html',new_score=res)
    
@app.route('/fail/<int:score>')
def fail(score):
    return 'App Failed and App score is '+str(score)

## Result checker submit html page
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        datascience=float(request.form['datascience'])
        total_score=(science+maths+c+datascience)/4
    result=""
    if total_score>50:
        result='success'
    else:
        result='fail'
    
    return redirect(url_for(result,score=total_score))


if __name__=="__main__":
    app.run(debug=True)