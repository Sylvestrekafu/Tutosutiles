from ultralytics import YOLO
import os

# Define paths
dataset_path = 'C:\Users\SYLVESTRE APETCHO\PycharmProjects\Yolov5\Yolov5\datasets\Donnees'
config_path = 'path/to/your/config.yaml'

# Initialize the model
model = YOLO('yolov8',  # Or the appropriate model name
             pretrained=True,
             classes=number_of_classes)

# Train the model
model.train(data=config_path,
            epochs=100,
            batch_size=16,
            imgsz=640,  # Image size
            project='runs/train',  # Directory to save results
            name='yolov8_experiment',  # Name of the experiment
            exist_ok=True)  # Overwrite existing results

# Save the final model
model.save(os.path.join('runs/train/yolov8_experiment', 'final_model.pt'))
