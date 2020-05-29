from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return "<h1>Home Page!<h1>"

@app.route('/about')
def about():
    return "<h1>About Page!<h1>"

@app.route('/schools')
def schools():
    return "<h1>Schools Page!<h1>"

@app.route('/services')
def services():
    return "<h1>Services Page!<h1>"

@app.route('/contact')
def contact():
    return "<h1>Contact Page!<h1>"

@app.route('/business')
def business():
    return "<h1>business Page!<h1>"

if __name__ == '__main__':
	app.run(debug=True)