import streamlit as st
import torch
import cv2
import numpy as np
from PIL import Image

# Charger le modèle YOLOv5
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

def detect(img):
    # Pass the image directly to YOLOv5's model
    results = model(img)
    # Convert the resulting predictions into a format suitable for display
    results_img = results.render()[0]
    results_img_pil = Image.fromarray(results_img)
    return results_img_pil

def count_objects(results):
    # Get the predicted class names
    names = results.names
    # Get the detected classes from the prediction results
    pred_classes = results.pred[0][:, -1].int().tolist()
    # Count occurrences of each class
    count_dict = {}
    for cls in pred_classes:
        cls_name = names[int(cls)]
        count_dict[cls_name] = count_dict.get(cls_name, 0) + 1
    return count_dict


st.title("Détection et Tracking d'Objets avec YOLOv5")

# Menu de choix de source
option = st.selectbox('Choisissez une source', ('Image', 'Vidéo', 'Caméra'))

if option == 'Image':
    uploaded_files = st.file_uploader("Choisissez une image", type=["jpg", "png", "jpeg"], accept_multiple_files=True)
    if uploaded_files:
        for uploaded_file in uploaded_files:
            image = Image.open(uploaded_file)
            st.image(image, caption=f'Image Uploadée: {uploaded_file.name}', use_column_width=True)
            if st.button(f'Détecter {uploaded_file.name}'):
                output = detect(image)
                st.image(output, caption=f'Image Avec Détections de {uploaded_file.name}.', use_column_width=True)



                col1, col2 = st.columns(2)

                with col1:
                    st.image(image, caption='Image Uploadée.', use_column_width=True)
                with col2:
                    st.image(output, caption='Image Avec Détections.', use_column_width=True)



elif option == 'Vidéo':
    uploaded_video = st.file_uploader("Choisissez une vidéo", type=["mp4", "avi", "mov", "mkv"])
    if uploaded_video:
        st.video(uploaded_video, caption='Vidéo uploadée.', use_column_width=True)
        if st.button('Détecter sur Vidéo'):
            # ... [le reste du code pour traiter la vidéo]

            col1, col2 = st.beta_columns(2)

            with col1:
                st.video(uploaded_video, caption='Vidéo originale.', use_column_width=True)
            with col2:
                st.video('output.avi', caption='Vidéo avec détections.', use_column_width=True)


def create_cap():
    return cv2.VideoCapture(0)

if 'cap' not in st.session_state:
    st.session_state.cap = create_cap()

cap = st.session_state.cap

if option == 'Caméra':
    st.write("Flux de la caméra :")
    frame_placeholder = st.empty()
    detect_btn = st.button('Détecter')

    while True:
        ret, frame = cap.read()
        if not ret:
            st.write("Erreur de capture depuis la caméra")
            break
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(frame_rgb)

        # Si le bouton détecter est pressé
        if detect_btn:
            output_img = detect(img_pil)
            frame_placeholder.image(output_img, caption='Résultat de la détection', use_column_width=True)
        else:
            frame_placeholder.image(img_pil, caption='Capture depuis la caméra', use_column_width=True)
