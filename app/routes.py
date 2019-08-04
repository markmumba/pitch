from app.models import User,Post
from flask import ,render_template,url_for,flash,redirect
from app.forms import RegistrationForm,LoginForm





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

@app.route("/register", methods = ['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def Login():
    form=LoginForm()
    if form.email.data == 'markmumba01@gmail.com' and form.password.data =='password':
        flash('You have been logged in!' , 'success')
        return redirect (url_for('home'))
    else:
        flash('cannot')

    return render_template('login.html', title='Login' ,form = form)






