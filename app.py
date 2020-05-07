from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/discussion')
def discussion():
    return render_template('login.html')

@app.route('/ancientgreece')
def ancientgreece():
    return render_template('greece.html')

@app.route('/italianrenaissance')
def italianrenaissance():
    return render_template('italy.html')

@app.route('/account')
def account():
    return render_template('account.html')
