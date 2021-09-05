from flask import Flask,render_template
from test import abc
def task():
    print('this is function')


app=Flask(__name__)
@app.route('/') # this is decorator , there should not be any gap between decorator and function if u put anything inbetween then it will not work
def hello_world():
    task()
    return render_template('home.html')

@app.route('/hello')
def welcome():
    return render_template('home.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/galarry')
def gallary():
    return render_template('gallary.html')

#app.run()
app.run(debug=True) # this is go into live changes after a change we need not to close the server and run again this will run it automatically


# for practice we can "https://www.w3schools.com/html/"