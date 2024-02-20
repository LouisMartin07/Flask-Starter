from flask import Flask, render_template

app = Flask(__name__)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/recipes")
def signup():
    return render_template("recipes.html")

@app.route("/mealplanning")
def signup():
    return render_template("mealplanning.html")

@app.route("/grocerylistgen")
def signup():
    return render_template("grocerylistgen.html")

@app.route("/custandpref")
def signup():
    return render_template("custandpref.html")

app.run(debug=True)
