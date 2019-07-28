from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '34345gfcg65tyfty4d'


posts = [
    {
        'author': 'Mohit',
        'title': 'Blog 1',
        'content': 'Food',
        'date_posted': '06.04.18'

    },
    {
        'author': 'John',
        'title': 'Blog 2',
        'content': 'Tech',
        'date_posted': '25.06.14'

    }
]


# @app.route('/home')
# def home():
#     return render_template("home.html", posts=posts)

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", posts=posts)


@app.route('/about')
def about():
    return render_template("about.html", title="about")


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for('home'))
    return render_template("register.html", title="Register", form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template("login.html", title="Login", form=form)


@app.route('/profile/<name>')
def profile(name):
    return render_template("profile.html", name=name)


if __name__ == "__main__":
    app.run(debug=True)
