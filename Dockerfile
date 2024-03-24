# Utilisez une image de base qui contient Python
FROM python:3.12

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez les fichiers de votre application dans le conteneur
COPY . /app

# Installez les dépendances Python
RUN pip install -r requirements.txt

# Exposez le port sur lequel votre application Flask fonctionne
EXPOSE 5000

# Commande pour exécuter l'application Flask
CMD python ./app.py
