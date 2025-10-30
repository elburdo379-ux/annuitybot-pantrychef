from flask import Flask, request, render_template
import random
import json

app = Flask(__name__)

# Mock database (in memory)
db = {
    "client123": {"contract_value": 50000, "payment_status": "Active"}
}

# Home page
@app.route("/")
def index():
    return render_template("index.html")

# AnnuityBot - RANDOM contract value for client123
@app.route("/annuitybot", methods=["GET", "POST"])
def annuitybot():
    if request.method == "POST":
        client_id = request.form["client_id"]
        query = request.form["query"].lower()

        if client_id == "client123" and "contract value" in query:
            random_value = random.randint(2500, 7000000)
            response = f"Your annuity contract value is ${random_value:,}."
        else:
            response = "Sorry, I can only answer contract value for client123."
        
        return render_template("annuitybot.html", response=response)
    
    return render_template("annuitybot.html", response="")

# PantryChef - simple mock
@app.route("/pantrychef", methods=["GET", "POST"])
def pantrychef():
    if request.method == "POST":
        ingredients = request.form["ingredients"]
        response = f"Recipe for {ingredients}: Mix and cook!"
        return render_template("pantrychef.html", recipe=response)
    return render_template("pantrychef.html", recipe="")

if __name__ == "__main__":
    app.run(debug=True)