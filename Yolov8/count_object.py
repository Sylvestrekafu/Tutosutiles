import streamlit as st
from ultralytics import YOLO
import cv2
import tempfile
import numpy as np

# Load the YOLO model
model = YOLO('yolov8n.pt')

st.title("Object Detection, Tracking and Counting App")

def draw_boxes(image, results):
    for *xyxy, conf, cls in results:
        label = f'{model.names[int(cls)]} {conf:.2f}'
        cv2.rectangle(image, (int(xyxy[0]), int(xyxy[1])), (int(xyxy[2]), int(xyxy[3])), (0, 255, 0), 2)
        cv2.putText(image, label, (int(xyxy[0]), int(xyxy[1] - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2, cv2.LINE_AA)
    return image

media_option = st.radio("Choose the media type:", options=["Image", "Video", "Camera"])

if media_option == "Image":
    # Upload image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), -1)
        results = model(image).xyxy[0].cpu().numpy()
        st.image(draw_boxes(image, results), channels='BGR')

elif media_option == "Video":
    # Process video
    video_file_buffer = st.file_uploader("Upload video", type=["mp4", "mov", "avi"], key="video")
    tffile = tempfile.NamedTemporaryFile(delete=False)
    if video_file_buffer:
        tffile.write(video_file_buffer.read())
        cap = cv2.VideoCapture(tffile.name)

        stframe = st.empty()

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            results = model(frame).xyxy[0].cpu().numpy()
            stframe.image(draw_boxes(frame, results), channels='BGR')

elif media_option == "Camera":
    # Process camera feed
    if st.button('Start Camera'):
        st.text('Accessing camera...')
        cap = cv2.VideoCapture(0)

        stframe = st.empty()

        while True:
            ret, frame = cap.read()
            results = model(frame).xyxy[0].cpu().numpy()
            stframe.image(draw_boxes(frame, results), channels='BGR')
