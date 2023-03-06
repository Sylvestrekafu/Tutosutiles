from ultralytics import YOLO

# Load a model
model = YOLO('yolov8n-pose.pt')  # load an official model
#model = YOLO('path/to/best.pt')  # load a custom model

# Predict with the model
results = model('activ.jpg')  # predict on an image