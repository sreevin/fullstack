from flask import Flask,render_template,request

app=Flask(__name__)
@app.route('/submit')

def index():  
    return render_template('input.html')

# @app.route('/about')
# def about():
#     return 'Welcome to ABOUT page'

# @app.route('/home')
# def home():
#     return 'Welcome to HOME page'
@app.route('/Flask')
def Flask():
    return render_template('result.html')

@app.route('/Flask',methods=['GET','POST'])
def Flask():
    if(request.method=='POST'):
        getName=request.form['name']
        # getEmail=request.form['email']
        # getMob=request.form['number']
        # getSub=request.form['subject']
        # getMsg=request.form['message']
        return render_template('result.html',name=getName)
if(__name__=='__main__'):
    app.run(debug=True)