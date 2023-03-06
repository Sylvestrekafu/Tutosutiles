import streamlit as st
import torch
import cv2
from PIL import Image
import tempfile
import numpy as np


import streamlit as st
import torch
import numpy as np
from PIL import Image

@st.cache_resource()
def load_model(model_name):
    model = torch.hub.load('ultralytics/yolov5', model_name, pretrained=True)
    return model

def run_detection_image(model, img, conf_threshold, iou_threshold):
    model.conf = conf_threshold  # Définir le seuil de confiance
    model.iou = iou_threshold    # Définir le seuil IoU
    results = model(img, size=640)
    return results

def count_classes(results, class_names):
    class_counts = {}
    for det in results.xyxy[0]:  # Parcourir les détections
        class_id = int(det[5])
        class_name = class_names[class_id]
        if class_name in class_counts:
            class_counts[class_name] += 1
        else:
            class_counts[class_name] = 1
    return class_counts

def main():
    st.title("Détection d'objets avec YOLOv5")

    # Sélection du modèle YOLOv5 et configuration des seuils
    model_choice = st.sidebar.selectbox("Choisissez le modèle YOLOv5", ["yolov5s", "yolov5m", "yolov5l", "yolov5x"])
    conf_threshold = st.sidebar.slider("Seuil de confiance", 0.0, 1.0, 0.25)
    iou_threshold = st.sidebar.slider("Seuil IoU", 0.0, 1.0, 0.45)  # Ajout d'un contrôle pour le seuil IoU

    model = load_model(model_choice)

    # Téléchargement et traitement des images
    files = st.file_uploader("Téléchargez des images", type=["jpg", "jpeg", "png"], accept_multiple_files=True)
    if files:
        class_names = model.module.names if hasattr(model, 'module') else model.names
        for file in files:
            image = Image.open(file).convert('RGB')
            st.image(image, caption=f"Image originale: {file.name}", use_column_width=True)

            # Exécution de la détection d'objets
            results = run_detection_image(model, np.array(image), conf_threshold, iou_threshold)
            annotated_images = results.render()
            for annotated_image in annotated_images:
                st.image(annotated_image, caption=f"Image avec détections: {file.name}", use_column_width=True)

            # Compter et afficher le nombre d'objets détectés par classe
            class_counts = count_classes(results, class_names)
            st.write("Nombre d'objets détectés par classe:")
            for class_name, count in class_counts.items():
                st.write(f"{class_name}: {count}")

if __name__ == "__main__":
    main()
#
# ###############################################################"""
# @st.cache_resource()
# def load_model(model_name):
#     model = torch.hub.load('ultralytics/yolov5', model_name, pretrained=True)
#     return model
#
# def run_detection_image(model, img, conf_threshold):
#     model.conf = conf_threshold
#     results = model(img, size=640)
#     return results
#
#
# def count_classes(results, class_names):
#     class_counts = {}
#     for det in results.xyxy[0]:
#         class_id = int(det[5])
#         class_name = class_names[class_id]
#         if class_name in class_counts:
#             class_counts[class_name] += 1
#         else:
#             class_counts[class_name] = 1
#     return class_counts
#
#
# def main():
#     st.title("Détection d'objets avec YOLOv5")
#
#     # Sélection du modèle YOLOv5 à utiliser
#     model_choice = st.sidebar.selectbox("Choisissez le modèle YOLOv5", ["yolov5s", "yolov5m", "yolov5l", "yolov5x"])
#     conf_threshold = st.sidebar.slider("Seuil de confiance", 0.0, 1.0, 0.25)  # Réglage du seuil de confiance
#     model = load_model(model_choice)
#
#     # Téléchargement et traitement des images
#     files = st.file_uploader("Téléchargez des images", type=["jpg", "jpeg", "png"], accept_multiple_files=True)
#     if files:
#         class_names = model.module.names if hasattr(model, 'module') else model.names
#         for file in files:
#             image = Image.open(file).convert('RGB')
#             st.image(image, caption=f"Image originale: {file.name}", use_column_width=True)
#
#             # Exécution de la détection d'objets
#             results = run_detection_image(model, np.array(image), conf_threshold)
#             annotated_images = results.render()  # Obtention des images annotées
#             for annotated_image in annotated_images:
#                 st.image(annotated_image, caption=f"Image avec détections: {file.name}", use_column_width=True)
#
#             # Compter le nombre d'objets détectés par classe
#
#             class_counts = count_classes(results, class_names)
#             st.write("Nombre d'objets détectés par classe:")
#             for class_name, count in class_counts.items():
#                 st.write(f"{class_name}: {count}")
#
# if __name__ == "__main__":
#     main()
