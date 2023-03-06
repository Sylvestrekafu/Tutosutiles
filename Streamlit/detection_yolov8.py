import streamlit as st
from ultralytics import YOLO
from PIL import Image, ImageDraw
import tempfile

def load_model(model_name):
    model = YOLO(model_name)
    return model


def draw_boxes(image, detections):
    draw = ImageDraw.Draw(image)
    for det in detections:
        # Supposons que det contienne [x1, y1, x2, y2, conf, cls]
        x1, y1, x2, y2, conf, cls = det[:6]
        draw.rectangle([x1, y1, x2, y2], outline="red", width=2)
        draw.text((x1, y1 - 10), f"{model.names[int(cls)]} {conf:.2f}", fill="red")
    return image


def main():
    st.title("Détection d'objets avec YOLOv8")

    model_choice = st.sidebar.selectbox("Choisissez le modèle YOLOv8",
                                        ["yolov8s.pt", "yolov8m.pt", "yolov8l.pt", "yolov8x.pt"])
    model = load_model(model_choice)

    conf_threshold = st.sidebar.slider("Seuil de confiance", 0.0, 1.0, 0.25)
    iou_threshold = st.sidebar.slider("Seuil IOU", 0.0, 1.0, 0.45)

    files = st.file_uploader("Téléchargez des images", type=["jpg", "jpeg", "png"], accept_multiple_files=True)
    if files:
        for file in files:
            image = Image.open(file).convert('RGB')
            st.image(image, caption='Image téléchargée', use_column_width=True)

            with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
                image.save(temp_file.name)
                results = model(temp_file.name, conf=conf_threshold, iou=iou_threshold, show=False)

                # Dessinez manuellement les boîtes englobantes sur l'image
                if hasattr(results, 'pred') and len(results.pred[0]):
                    detected_image = draw_boxes(image, results.pred[0])
                    st.image(detected_image, caption='Image avec détections', use_column_width=True)
                else:
                    st.write("Aucune détection.")


if __name__ == "__main__":
    main()
