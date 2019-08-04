from flask import Flask,render_template,url_for
app = Flask(__name__)

pitches = [
    {
        'author': 'Corey Schafer',
        'title': 'Pitch Idea 1',
        'content': 'Pitch idea itself',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Pitch idea 2',
        'content': 'Pitch idea itselft',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', pitches=pitches)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)