from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
        return render_template("home.html")

@app.route("/login", method = ['POST', 'GET'])
def login():
        return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/recipes")
def recipes():
    return render_template("recipes.html")

@app.route("/mealplanning")
def mealplanning():
    return render_template("mealplanning.html")

@app.route("/grocerylistgen")
def grocerylistgen():
    return render_template("grocerylistgen.html")

@app.route("/custandpref")
def custandpref():
    return render_template("custandpref.html")

app.run(debug=True)


