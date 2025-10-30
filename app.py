from flask import Flask, request, render_template
import random
from datetime import datetime, timedelta

app = Flask(__name__)

# Home page
@app.route("/")
def index():
    return render_template("index.html")

# === UPGRADED ANNUITYBOT ===
@app.route("/annuitybot", methods=["GET", "POST"])
def annuitybot():
    response = ""
    if request.method == "POST":
        client_id = request.form["client_id"].strip()
        query = request.form["query"].lower().strip()

        if client_id != "client123":
            response = "Sorry, only client123 is supported."
        else:
            # 1. Contract Value
            if "contract value" in query:
                contract_value = random.randint(2500, 7000000)
                response = f"Your **contract value** is **${contract_value:,}**."

            # 2. Surrender Value
            elif "surrender value" in query:
                contract_value = random.randint(2500, 7000000)
                reduction = random.randint(2000, 10000)
                surrender_value = max(contract_value - reduction, 0)
                response = f"Your **surrender value** is **${surrender_value:,}** (contract: ${contract_value:,}, reduced by ${reduction:,})."

            # 3. Issue Date
            elif "issue date" in query:
                start = datetime(2000, 1, 1)
                end = datetime.now()
                days = random.randint(0, (end - start).days)
                issue_date = start + timedelta(days=days)
                response = f"Your policy **issue date** is **{issue_date.strftime('%B %d, %Y')}**."

            # 4. Beneficiaries
            elif "beneficiar" in query:
                primaries = ["Emma Johnson", "Liam Chen", "Olivia Patel", "Noah Kim"]
                contingents = ["Sophia Rivera", "Mason Lee", "Ava Wong", "Ethan Park"]
                primary = random.choice(primaries)
                contingent = random.choice(contingents)
                response = f"**Primary beneficiary**: {primary}<br>**Contingent beneficiary**: {contingent}"

            # 5. Initial Premium
            elif "initial premium" in query:
                initial_premium = random.randint(1000, 500000)
                response = f"Your **initial premium** was **${initial_premium:,}**."

            else:
                response = "I can answer: contract value, surrender value, issue date, beneficiaries, or initial premium."

        return render_template("annuitybot.html", response=response)

    return render_template("annuitybot.html", response="")

# === UPGRADED PANTRYCHEF ===
@app.route("/pantrychef", methods=["GET", "POST"])
def pantrychef():
    recipe = ""
    if request.method == "POST":
        ingredients = [i.strip().lower() for i in request.form["ingredients"].split(",")]

        # Recipe database
        recipes = {
            ("rice", "chicken", "eggs"): {
                "name": "Chicken Fried Rice",
                "add": ["soy sauce", "green onions", "oil", "garlic"],
                "steps": [
                    "Cook rice and let cool.",
                    "Scramble eggs in oil.",
                    "Stir-fry chicken and garlic.",
                    "Add rice, soy sauce, and green onions. Mix well."
                ]
            },
            ("pasta", "tomatoes"): {
                "name": "Spaghetti Marinara",
                "add": ["garlic", "olive oil", "basil", "parmesan"],
                "steps": [
                    "Boil pasta.",
                    "Sauté garlic in olive oil.",
                    "Add crushed tomatoes and simmer.",
                    "Toss with pasta and top with basil & parmesan."
                ]
            },
            ("bread", "ham", "cheese"): {
                "name": "Grilled Ham & Cheese",
                "add": ["butter", "mustard"],
                "steps": [
                    "Butter bread slices.",
                    "Add ham, cheese, and mustard.",
                    "Grill until golden and melty."
                ]
            }
        }

        # Find matching recipe
        matched = None
        for key in recipes:
            if all(item in ingredients for item in key):
                matched = recipes[key]
                break

        if matched:
            add = ", ".join(matched["add"])
            steps = "<ol><li>" + "</li><li>".join(matched["steps"]) + "</li></ol>"
            recipe = f"<h3>{matched['name']}</h3><p><strong>Added ingredients:</strong> {add}</p>{steps}"
        else:
            recipe = "<p>No full recipe found. Try: rice+chicken+eggs, pasta+tomatoes, or bread+ham+cheese.</p>"

        return render_template("pantrychef.html", recipe=recipe)

    return render_template("pantrychef.html", recipe="")

if __name__ == "__main__":
    app.run(debug=True)