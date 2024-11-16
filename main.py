from flask import Flask, request, redirect, render_template, session, jsonify
import os
from auth import get_auth_url, get_access_token
from vision import recognize_card
import requests

app = Flask(__name__)
app.secret_key = "SECRET_KEY"  # Remplace par une clé secrète

# Route pour la page d'accueil
@app.route("/")
def index():
    return render_template("index.html")

# Route pour l'authentification eBay
@app.route("/login")
def login():
    auth_url = get_auth_url()
    return redirect(auth_url)

# Callback après la connexion eBay
@app.route("/callback")
def callback():
    auth_code = request.args.get("code")
    tokens = get_access_token(auth_code)
    if tokens:
        session["access_token"] = tokens["access_token"]
        return redirect("/")
    return "Erreur lors de la connexion à eBay", 400

# Route pour télécharger une image et obtenir le prix moyen
@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return "Aucun fichier téléchargé", 400

    file = request.files["file"]
    image_path = os.path.join("uploads", file.filename)
    file.save(image_path)

    card_name = recognize_card(image_path)
    if not card_name:
        return "Carte non reconnue", 400

    # Recherche sur eBay
    access_token = session.get("access_token")
    if not access_token:
        return redirect("/login")

    price = search_ebay(card_name, access_token)
    return jsonify({"card_name": card_name, "average_price": price})

# Fonction de recherche sur eBay
def search_ebay(card_name, access_token):
    url = "https://api.ebay.com/buy/browse/v1/item_summary/search"
    headers = {"Authorization": f"Bearer {access_token}"}
    params = {"q": card_name, "limit": 10}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        items = response.json().get("itemSummaries", [])
        prices = [float(item["price"]["value"]) for item in items if "price" in item]
        return sum(prices) / len(prices) if prices else 0
    return 0

if __name__ == "__main__":
    os.makedirs("uploads", exist_ok=True)
    app.run(debug=True)
