import requests
import json

# Configuration OAuth eBay
CLIENT_ID = "TON_CLIENT_ID"
CLIENT_SECRET = "TON_CLIENT_SECRET"
REDIRECT_URI = "TON_REDIRECT_URI"  # Exemple : http://localhost:5000/callback

def get_auth_url():
    """Génère l'URL pour l'authentification eBay."""
    base_url = "https://auth.ebay.com/oauth2/authorize"
    scope = "https://api.ebay.com/oauth/api_scope"
    return f"{base_url}?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&response_type=code&scope={scope}"

def get_access_token(auth_code):
    """Échange le code d'autorisation contre un jeton d'accès."""
    url = "https://api.ebay.com/identity/v1/oauth2/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "grant_type": "authorization_code",
        "code": auth_code,
        "redirect_uri": REDIRECT_URI,
    }
    response = requests.post(url, auth=(CLIENT_ID, CLIENT_SECRET), headers=headers, data=data)
    if response.status_code == 200:
        return response.json()
    else:
        print("Erreur lors de l'obtention du token :", response.text)
        return None
