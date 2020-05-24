from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = '8cef6e14fc961d3d5d40a11f3d382d20'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqllite:///site.db'

db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
	password = db.Column(db.String(60), nullable=False)

	def __repr__(self):
		return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	date_posted = None



posts = [
	{
		"author": "Heisson",
		"title": "Post 1",
		"content": "First post content",
		"date_posted": "May 23, 2020"
	},
	{
		"author": "Helington",
		"title": "Post 2",
		"content": "Second post content",
		"date_posted": "March 12, 2020"
	}

]

@app.route('/')
@app.route('/home')
def home():
	return render_template("home.html", posts=posts)

@app.route('/about')
def about():
	return render_template("about.html", title="About")

@app.route("/register", methods=["GET", "POST"])
def register():
	form = RegistrationForm()

	if form.validate_on_submit():
		flash(f"Account created for {form.username.data}.", "success")
		return redirect(url_for('home'))

	return render_template("register.html", title="Register", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
	form = LoginForm()

	if form.validate_on_submit():
		if form.email.data == 'admin@blog.com' and form.password.data == 'password':
			flash(f"You have been logged in!", 'success')
			return redirect(url_for('home'))

		else:
			flash(f"Log in unsuccessful. Please check username ans password", 'danger')

	return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
	app.run(debug=True)