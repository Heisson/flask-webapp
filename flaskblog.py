from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '8cef6e14fc961d3d5d40a11f3d382d20'

posts = [
	{
		"author": "Heisson",
		"title": "Post 1",
		"content": "First post content",
		"date_postet": "May 23, 2020"
	},
	{
		"author": "Helington",
		"title": "Post 2",
		"content": "Second post content",
		"date_postet": "March 12, 2020"
	}

]

@app.route('/')
@app.route('/home')
def home():
	return render_template("home.html", posts=posts)

@app.route('/about')
def about():
	return render_template("about.html", title="About")

@app.route("/register")
def register():
	form = RegistrationForm()
	return render_template("register.html", title="Register", form=form)

@app.route("/login")
def login():
	form = LoginForm()
	return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
	app.run(debug=True)