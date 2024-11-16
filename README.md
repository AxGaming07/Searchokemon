Searchokemon
Searchokemon est une application innovante qui permet aux utilisateurs de gérer leurs cartes Pokémon, d'identifier leurs noms à partir d'images, et de calculer leur prix moyen à l'aide de l'API eBay. Avec une interface simple et intuitive, Searchokemon combine la reconnaissance d'image et la puissance des API pour aider les collectionneurs à évaluer leur collection.

Fonctionnalités
Reconnaissance des cartes Pokémon : Utilise l'API Google Vision pour identifier les cartes à partir d'une image téléchargée.
Évaluation des prix : Recherchez le prix moyen des cartes via l'API eBay, directement depuis votre compte eBay.
Gestion des comptes eBay : Chaque utilisateur peut lier son propre compte eBay pour des recherches personnalisées.
Calcul des prix multiples : Ajoutez plusieurs cartes pour obtenir le prix total de votre collection.
Prérequis
Clé API Google Vision :
Créez un projet sur Google Cloud Console.
Activez l'API Vision et téléchargez une clé JSON.
Compte eBay Developer :
Inscrivez-vous sur eBay Developer Program.
Configurez une application OAuth pour obtenir un Client ID et un Client Secret.
Python 3.x avec les bibliothèques suivantes :
bash
Copier le code
pip install requests google-cloud-vision Flask
Installation
Clonez ce dépôt :
bash
Copier le code
git clone https://github.com/votre-utilisateur/Searchokemon.git
cd Searchokemon
Placez votre clé JSON pour Google Vision dans le dossier du projet.
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
Accédez à l'application à l'adresse : http://localhost:5000.
Utilisation
Connexion à eBay :
Cliquez sur "Connectez-vous à eBay" pour autoriser l'application.
Téléchargement d'une carte :
Téléchargez une image de votre carte Pokémon.
Résultat :
L'application identifiera la carte et affichera son prix moyen estimé.
Contributions
Les contributions sont les bienvenues ! Si vous avez des idées pour améliorer Searchokemon, ouvrez une issue ou soumettez une pull request.

Licence
Ce projet est sous licence MIT. Consultez le fichier LICENSE pour plus de détails.

Searchokemon - Attrapez-les tous, évaluez-les tous ! 🌟






