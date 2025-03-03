from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "supersecretkey"

recipes = []
user_preferences = {}

@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")

@app.route("/preferences", methods=["POST"])
def preferences():
    session["name"] = request.form.get("name") 
    return render_template("preferences.html")

@app.route("/save_preferences", methods=["POST"])
def save_preferences():
    user_preferences["diet"] = request.form.get("diet")
    user_preferences["cuisine"] = request.form.get("cuisine")
    user_preferences["meals_per_week"] = request.form.get("meals_per_week")
    return redirect(url_for("recipe_input"))

@app.route("/recipe_input", methods=["GET", "POST"])
def recipe_input():
    if request.method == "POST":
        recipes.append({
            "name": request.form.get("recipe_name"),
            "ingredients": request.form.get("ingredients")
        })
    return render_template("recipe_input.html", recipes=recipes)

@app.route("/recipe_plan", methods=["GET"])
def recipe_plan():
    return render_template("recipe_plan.html", preferences=user_preferences, recipes=recipes)

if __name__ == "__main__":
    app.run(debug=True)
