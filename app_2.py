from flask import Flask,render_template,request
import joblib
#from flask.wrappers import Request
#from test import abc


model = joblib.load('dib_79.pkl')
print('[INFO] model loaded')


def task():
    print('this is function')


app=Flask(__name__)
@app.route('/') # this is decorator , there should not be any gap between decorator and function if u put anything inbetween then it will not work
def hello_world():
    task()
    return render_template('home_1.html')

@app.route('/predict' , methods = ['post'])
def predict():
    preg = request.form.get('preg')
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mass')
    pedi = request.form.get('pedi')
    age = request.form.get('age')

    print(type(preg))
    output = model.predict([[preg,plas,pres,skin,test,mass,pedi,age]])
    if output[0]==1:
        print('dibatic')
    else:
        print('not dibatic')
    return 'Form Submitted'

#app.run()
app.run(debug=True) # this is go into live changes after a change we need not to close the server and run again this will run it automatically

