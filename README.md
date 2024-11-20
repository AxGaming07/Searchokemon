# 🎴 **Searchokemon**

> *Attrapez-les tous, évaluez-les tous !*

**Searchokemon** est une application conçue pour les collectionneurs de cartes Pokémon. Grâce à la reconnaissance d'image et à la recherche automatisée des prix via eBay, vous pouvez facilement évaluer votre collection et gérer vos cartes comme un maître Pokémon. 🐾

---

## ✨ **Fonctionnalités**

- 🔍 **Reconnaissance d'image** : Identifiez vos cartes Pokémon à partir d'une simple photo grâce à Google Vision.  
- 💸 **Évaluation des prix** : Calculez le prix moyen de vos cartes en vous basant sur des annonces eBay en temps réel.  
- 🔗 **Connexion eBay sécurisée** : Liez votre propre compte eBay pour des recherches personnalisées.  
- 📊 **Gestion avancée** : Ajoutez plusieurs cartes et obtenez une estimation globale de votre collection.  

---

## 🚀 **Prérequis**

Avant de commencer, assurez-vous d'avoir :

1. Une **clé API Google Vision** :  
   - [Créer un projet Google Cloud](https://console.cloud.google.com/).  
   - Activer l'API Vision et télécharger une clé JSON.  

2. Un **compte eBay Developer** :  
   - [S'inscrire au programme développeur eBay](https://developer.ebay.com/).  
   - Créer une application et configurer OAuth (avec `Client ID` et `Client Secret`).  

3. **Python 3.x** avec les bibliothèques suivantes installées :
   ```bash
   pip install requests google-cloud-vision Flask
⚙️ Installation
Clonez ce dépôt :

bash
Copier le code
git clone https://github.com/votre-utilisateur/Searchokemon.git
cd Searchokemon
Ajoutez votre clé JSON de Google Vision dans le dossier racine du projet.

Configurez vos identifiants eBay dans auth.py :

python
Copier le code
CLIENT_ID = "Votre_Client_ID"
CLIENT_SECRET = "Votre_Client_Secret"
REDIRECT_URI = "http://localhost:5000/callback"
Lancez l'application :

bash
Copier le code
python main.py
Ouvrez votre navigateur à l'adresse suivante : http://localhost:5000.

🧑‍💻 Utilisation
1️⃣ Connectez-vous à eBay
Cliquez sur "Connectez-vous à eBay" pour autoriser l'application à accéder à vos données.

2️⃣ Ajoutez une carte
Téléchargez une photo de votre carte Pokémon.
L'application identifiera automatiquement la carte grâce à Google Vision.
3️⃣ Calculez les prix
Une fois la carte reconnue, Searchokemon utilisera votre compte eBay pour rechercher les annonces correspondantes.
Vous obtiendrez le prix moyen de votre carte en quelques secondes.
📂 Structure du Projet
graphql
Copier le code
Searchokemon/
├── main.py           # Serveur principal Flask
├── auth.py           # Gestion de l'authentification OAuth eBay
├── vision.py         # Reconnaissance des cartes avec Google Vision
├── templates/        # Fichiers HTML pour l'interface
├── uploads/          # Dossier pour les images téléchargées
└── LICENSE           # Fichier de licence
🤝 Contributions
Les contributions sont les bienvenues ! 🎉

🚀 Si vous avez une idée pour améliorer Searchokemon, ouvrez une issue.
🛠️ Si vous souhaitez contribuer directement, soumettez une pull request.
📜 Licence
Ce projet est sous licence MIT. Consultez le fichier LICENSE pour plus d'informations.

🌟 Attrapez-les tous !
Avec Searchokemon, la gestion de vos cartes Pokémon n'a jamais été aussi simple. Que vous soyez un collectionneur amateur ou un expert, cet outil est fait pour vous. Profitez-en ! 🎮


Image illustrative - Non incluse dans le projet.

markdown
Copier le code

### Pour utiliser le fichier :
1. **Crée un fichier nommé `README.md`.**
2. **Copie et colle ce contenu dans ce fichier.**
3. **Ajoute-le à ton dépôt GitHub avec les commandes suivantes si tu utilises Git** :
   ```bash
   git add README.md
   git commit -m "Ajout du README"
   git push
