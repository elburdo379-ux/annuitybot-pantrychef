from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock response functions (fast, no heavy models)
def mock_annuity_response(client_id, question):
    if client_id == "client123":
        return "Your annuity contract value is $50,000."
    else:
        return "Client not found. Please check your ID."

def mock_recipe_response(ingredients):
    items = [i.strip() for i in ingredients.split(",") if i.strip()]
    if not items:
        return "Please provide ingredients."
    return f"Mock recipe: Combine {', '.join(items)} and bake for 20 minutes."

@app.route("/")
def index():
    return """
    <h2>AnnuityBot & PantryChef Demo</h2>
    <ul>
        <li><a href="/annuitybot">AnnuityBot</a></li>
        <li><a href="/pantrychef">PantryChef</a></li>
    </ul>
    """

@app.route("/annuitybot", methods=["GET", "POST"])
def annuitybot():
    if request.method == "GET":
        return '''
        <form method="post">
            Client ID: <input name="client_id"><br>
            Question: <input name="question" value="What's my contract value?"><br>
            <button type="submit">Ask</button>
        </form>
        '''
    client_id = request.form.get("client_id", "")
    question = request.form.get("question", "")
    response = mock_annuity_response(client_id, question)
    return jsonify({"answer": response})

@app.route("/pantrychef", methods=["GET", "POST"])
def pantrychef():
    if request.method == "GET":
        return '''
        <form method="post">
            Ingredients (comma separated): <input name="ingredients"><br>
            <button type="submit">Generate Recipe</button>
        </form>
        '''
    ingredients = request.form.get("ingredients", "")
    recipe = mock_recipe_response(ingredients)
    return jsonify({"recipe": recipe})

if __name__ == "__main__":
    # For local testing only. Production will use gunicorn on hosting platforms.
    app.run(host="0.0.0.0", port=5000, debug=True)
