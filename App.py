from flask import Flask

app=Flask(__name__)
@app.route('/')

def index():  
    return 'Welcome to flask'

@app.route('/about')
def about():
    return 'Welcome to ABOUT page'

@app.route('/home')
def home():
    return 'Welcome to HOME page'

if(__name__=='__main__'):
    app.run(debug=True)


