from flask import Flask,render_template
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/about',methods=['GET','POST'])
def about():
    return render_template('about.html')

@app.route('/signin',methods=['GET','POST'])
def signin():
    return render_template('signin.html')

@app.route('/signup',methods=['GET','POST'])
def signup():
    return render_template('signup.html')
