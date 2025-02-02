from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html',  active_page='home')

@app.route('/about')
def about():
    return render_template('about.html', active_page = 'about')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', active_page = 'portfolio')

@app.route('/contact')
def contact():
    return render_template('contact.html', active_page = 'contact')

if __name__ == '__main__':
    app.run(debug=True)
