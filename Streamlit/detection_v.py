import streamlit as st
import torch
import numpy as np
from PIL import Image, ImageDraw
import cv2  # Import OpenCV for video processing
import tempfile  # To create temporary file paths for video processing

@st.cache_resource()
def load_model(model_name):
    model = torch.hub.load('ultralytics/yolov5', model_name, pretrained=True)
    return model

def run_detection_image(model, img, conf_threshold, iou_threshold):
    model.conf = conf_threshold  # Set confidence threshold
    model.iou = iou_threshold  # Set IoU threshold
    results = model(img, size=640)
    return results

def draw_boxes(img, detections, box_color, box_width):
    for *xyxy, conf, cls in reversed(detections):
        xyxy = [int(x) for x in xyxy]  # Convert to int
        ImageDraw.Draw(img).rectangle(xyxy, outline=box_color, width=box_width)
    return img

def count_classes(results, class_names):
    class_counts = {}
    for det in results.xyxy[0]:  # Loop through detections
        class_id = int(det[5])
        class_name = class_names[class_id]
        class_counts[class_name] = class_counts.get(class_name, 0) + 1
    return class_counts
def hex_to_rgb(hex_color):
    """Converts a hexadecimal color string to an RGB tuple."""
    hex_color = hex_color.lstrip('#')  # Remove '#' if it exists
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def run_detection_video(model, video_path, conf_threshold, iou_threshold, hex_box_color, box_width):
    cap = cv2.VideoCapture(video_path)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    codec = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('output.mp4', codec, fps, (width, height))
    rgb_box_color = hex_to_rgb(hex_box_color)  # Convert hexadecimal to RGB

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        results = model(frame, size=640)
        for *xyxy, conf, cls in reversed(results.xyxy[0]):
            xyxy = [int(x) for x in xyxy]  # Convert to int
            cv2.rectangle(frame, (xyxy[0], xyxy[1]), (xyxy[2], xyxy[3]), rgb_box_color, box_width)
        out.write(frame)

    cap.release()
    out.release()

    return 'output.mp4'

def main():
    st.title("Détection d'objets avec YOLOv5")

    # Model selection and threshold configuration
    model_choice = st.sidebar.selectbox("Choisissez le modèle YOLOv5", ["yolov5s", "yolov5m", "yolov5l", "yolov5x"])
    conf_threshold = st.sidebar.slider("Seuil de confiance", 0.0, 1.0, 0.25)
    iou_threshold = st.sidebar.slider("Seuil IoU", 0.0, 1.0, 0.45)

    # Box color and width
    box_color = st.sidebar.color_picker("Choisissez la couleur de la boîte", '#FF0000')
    box_width = st.sidebar.slider("Épaisseur de la boîte", 1, 10, 2)

    model = load_model(model_choice)

    # Image and video upload and processing
    upload_type = st.radio("Choisissez le type de fichier à télécharger", ("Images", "Vidéo"))
    if upload_type == "Images":
        files = st.file_uploader("Téléchargez des images", type=["jpg", "jpeg", "png", "bmp", "gif"], accept_multiple_files=True)
        if files:
            class_names = model.module.names if hasattr(model, 'module') else model.names
            for file in files:
                image = Image.open(file).convert('RGB')
                st.image(image, caption=f"Image chargée: {file.name}", use_column_width=True)  # Display uploaded image

                results = run_detection_image(model, np.array(image), conf_threshold, iou_threshold)

                annotated_image = image.copy()
                annotated_image = draw_boxes(annotated_image, results.xyxy[0], box_color, box_width)
                st.image(annotated_image, caption=f"Image avec détections: {file.name}", use_column_width=True)

                # Display detected class counts in a table
                class_counts = count_classes(results, class_names)
                st.write("Nombre d'objets détectés par classe:")
                st.table(class_counts.items())
    elif upload_type == "Vidéo":
        file = st.file_uploader("Téléchargez une vidéo", type=["mp4", "avi", "mov", "mkv"])
        if file:
            tfile = tempfile.NamedTemporaryFile(delete=False)
            tfile.write(file.read())
            video_path = run_detection_video(model, tfile.name, conf_threshold, iou_threshold, box_color, box_width)
            st.video(video_path)

if __name__ == "__main__":
    main()
