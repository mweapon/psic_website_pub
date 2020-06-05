from flask import Flask, render_template
app = Flask(__name__, template_folder='pages')

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/schools')
def schools():
    return render_template('schools.html')

@app.route('/therapies')
def therapies():
    return render_template('therapies.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/business')
def business():
    return render_template('business.html')

if __name__ == '__main__':
	app.run(debug=True)