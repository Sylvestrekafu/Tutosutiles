# Utiliser une image de base officielle Python
FROM python:3.10-rc-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le répertoire Streamlit_and_Yolov5 dans le conteneur, en supposant que le Dockerfile est dans Streamlit_and_Yolov5/Docker
COPY ../ ./

# Installer les dépendances
RUN pip install --no-cache-dir streamlit torch numpy Pillow

# Exposer le port sur lequel l'application va tourner
EXPOSE 8501

# Commande pour exécuter l'application Streamlit, en supposant que detection_v5.py se trouve dans le répertoire Streamlit_and_Yolov5
CMD ["streamlit", "run", "detection_v5.py"]
