import streamlit as st  # Web application framework
import torch  # Deep learning framework
from PIL import Image, ImageDraw, ImageFont  # Image processing library
import numpy as np  # Numerical operations library

@st.cache_resource()
def load_model(model_name):
    """
    Charge une version spécifique de YOLOv5 à partir des fichiers de poids locaux.

    Args:
    model_name (str): Nom de la version du modèle YOLOv5 à charger ('n', 's', 'm').

    Returns:
    model: Le modèle YOLOv5 chargé.
    """
    # Chemins vers les fichiers de poids locaux

    weights_paths = {
        "n": "yolov5n.pt",  # Mettez à jour avec le chemin réel
        "s": "yolov5s.pt",  # Mettez à jour avec le chemin réel
        "m": "yolov5m.pt"   # Mettez à jour avec le chemin réel
    }

    weights_path = weights_paths[model_name]



    try:
        # Charger le modèle avec les poids personnalisés
        model = torch.hub.load('ultralytics/yolov5', 'custom', path=weights_path, force_reload=True)
    except Exception as e:
        st.error(f"Erreur lors du chargement des poids du modèle : {e}")
        model = None

    return model
def run_detection_image(model, img, conf_threshold, iou_threshold):
    """
    Runs object detection on an image using the specified YOLOv5 model.

    Args:
    model: The YOLOv5 model to use for detection.
    img (numpy.ndarray): The image on which to perform detection.
    conf_threshold (float): The confidence threshold for detections.
    iou_threshold (float): The Intersection over Union (IoU) threshold for non-maximum suppression.

    Returns:
    results: The detection results containing bounding boxes, classes, and scores.
    """
    if model is None:
        st.error("Le modèle n'a pas pu être chargé.")
        return None

    model.conf = conf_threshold  # Set confidence threshold
    model.iou = iou_threshold  # Set IoU threshold
    results = model(img)
    return results

def draw_boxes(img, detections, box_color, box_width, class_names):
    """
    Draws bounding boxes with labels on the image for each detection.

    Args:
    img (PIL.Image.Image): The image to draw bounding boxes on.
    detections: Detection results from the YOLOv5 model.
    box_color (str): Color of the bounding boxes.
    box_width (int): Width of the bounding boxes.
    class_names (list): List of class names corresponding to the model's detection classes.
    """
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()  # Load default font
    for *xyxy, conf, cls in reversed(detections):
        xyxy = [int(x) for x in xyxy]  # Convert coordinates to integers
        label = f"{class_names[int(cls)]} {conf:.2f}"  # Create label with class name and confidence score
        draw.rectangle(xyxy, outline=box_color, width=box_width)
        draw.text((xyxy[0], xyxy[1] - 10), label, fill=box_color, font=font)

def count_classes(results, class_names):
    """
    Counts the number of detected objects for each class.

    Args:
    results: The detection results from the YOLOv5 model.
    class_names (list): List of class names corresponding to the model's detection classes.

    Returns:
    class_counts (dict): A dictionary with class names as keys and counts as values.
    """
    class_counts = {}
    for det in results.xyxy[0]:  # Loop through detections
        class_id = int(det[5])
        class_name = class_names[class_id]
        class_counts[class_name] = class_counts.get(class_name, 0) + 1
    return class_counts

def main():
    """
    Main function to run the Streamlit application for YOLOv5 object detection.
    """
    st.title("Object Detection with YOLOv5")

    # Sidebar options for model selection and thresholds
    model_choice = st.sidebar.selectbox("Choisir le modèle YOLOv5", ["n", "s", "m"])


    conf_threshold = st.sidebar.slider("Confidence Threshold", 0.0, 1.0, 0.25)
    iou_threshold = st.sidebar.slider("IoU Threshold", 0.0, 1.0, 0.45)

    # Sidebar options for box drawing
    box_color = st.sidebar.color_picker("Choose Box Color", '#FF0000')
    box_width = st.sidebar.slider("Box Width", 1, 10, 2)

    # Load selected model
    model = load_model(model_choice)

    # File uploader for images
    uploaded_files = st.file_uploader("Upload Images", type=["jpg", "jpeg", "png", "bmp", "gif"], accept_multiple_files=True)
    if uploaded_files:
        for uploaded_file in uploaded_files:
            image = Image.open(uploaded_file).convert('RGB')
            st.image(image, caption=f"Uploaded Image: {uploaded_file.name}", use_column_width=True)

            # Run detection and draw boxes on the image
            img_array = np.array(image)
            results = run_detection_image(model, img_array, conf_threshold, iou_threshold)

            #results = run_detection_image(model, np.array(image), conf_threshold, iou_threshold)
            if results.xyxy[0].numel() == 0:  # Check if there are any detections
                st.write("No detections.")
            else:
                draw_boxes(image, results.xyxy[0], box_color, box_width, model.names)
                st.image(image, caption=f"Image with Detections: {uploaded_file.name}", use_column_width=True)

                # Count and display the number of objects detected per class
                class_counts = count_classes(results, model.names)
                st.write("Detected Objects Count by Class:")
                st.table(class_counts.items())

if __name__ == "__main__":
    main()