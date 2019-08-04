from flask_login import login_user,logout_user,login_required
from flask import render_template,url_for,flash,redirect
from app import app
from app.forms import RegistrationForm, LoginForm
from app.models import User,Post




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
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(' Your account has been created!', 'success')
        return redirect(url_for('Login'))
    return render_template('register.html', title='Register', form=form)



@app.route("/login")
def Login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember.data)
             return redirect(request.args.get('next') or url_for('home'))
        flash('Invalid username or Password')
    title = "login"
    return render_template('login.html',form = form,title=title)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route('/account')
def account():
    return render_template('account.html'title ='Account')




