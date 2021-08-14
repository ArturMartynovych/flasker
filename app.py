from flask import Flask, render_template

# Create a Flask Instance
app = Flask(__name__)


# Create a route decorator
@app.route('/')
# FILTERS Jinja2
# safe
# capitalize
# lower
# upper
# title
# trim
# striptags
def index():
    myName = "Artur"
    someStuff = "This is bold text"

    favoritePizza = ["Pepperoni", "Cheese", "Mushrooms", 41]
    return render_template("index.html",
                           myName=myName,
                           someStuff=someStuff,
                           favoritePizza=favoritePizza)


# localhost:5000/user/artur
@app.route('/user/<name>')
def user(name):
    return render_template("user.html", user_name=name)


@app.errorhandler(404)
def pageNotFound(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def pageNotFound(e):
    return render_template("500.html"), 505


if __name__ == '__main__':
    app.run()
