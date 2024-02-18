import streamlit as st
import cv2
import torch
import numpy as np
from PIL import Image

# Charger le modèle YOLOv5
model = torch.hub.load('ultralytics/yolov5', 'yolov5l', pretrained=True)

# Initialisation de la caméra (remplacer par la capture de vidéo Streamlit si disponible)
# Pour l'instant, cette fonctionnalité n'est pas directement supportée par Streamlit, mais vous pouvez utiliser des images téléchargées ou des vidéos stockées.

def load_camera(camera_id):
    cap = cv2.VideoCapture(camera_id)
    if not cap.isOpened():
        st.error(f'Erreur... caméra {camera_id} non accessible')
    return cap

# Fonction pour lire et détecter les objets dans un seul cadre
def detect_objects(frame):
    results = model(frame)
    frame = results.render()[0]
    return frame

# Fonction principale de l'application Streamlit
def main():
    st.title("Détection d'objets en temps réel avec YOLOv5")

    # Sélection de la source de la caméra (pour la démo, vous pouvez utiliser des fichiers téléchargés)
    # cam_input = st.selectbox("Choisir la caméra", options=[0, 1, 2, 3, 4, 5], index=0)

    uploaded_file = st.file_uploader("Choisir une image ou une vidéo", type=["jpg", "jpeg", "png", "mp4"])
    if uploaded_file is not None:
        bytes_data = uploaded_file.read()
        st.sidebar.text("Fichier chargé !")

        if uploaded_file.type.startswith('image/'):
            # Pour les images
            st.sidebar.image(bytes_data)
            frame = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = detect_objects(frame)
            st.image(frame, caption="Résultat de la détection", use_column_width=True)
        elif uploaded_file.type.startswith('video/'):
            # Pour les vidéos (traitement frame par frame)
            st.sidebar.text("Traitement de la vidéo...")
            # Code pour traiter la vidéo frame par frame ici
            # Note : Streamlit ne supporte pas la lecture vidéo en direct dans le navigateur pour le moment

if __name__ == '__main__':
    main()
