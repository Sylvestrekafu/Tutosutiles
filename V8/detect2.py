import cv2
from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO('yolov8n.pt')


camera1 = cv2.VideoCapture(0)
camera2 = cv2.VideoCapture(2)

if not camera1.isOpened():
    print('Erreur ...cam1')

if not camera2.isOpened():
    print('Erreur.. cam2')

while True:
    ret1, frame1 = camera1.read()
    ret2, frame2 = camera2.read()

    if ret1 and ret2:
        # Appliquer YOLOv5 aux deux images
        results1 = model(frame1)
        results2 = model(frame2)

        # Récupérer les images avec les détections
        frame1 = results1[0].plot()
        frame2 = results2[0].plot()

        # Concaténer les images pour l'affichage
        frame = cv2.hconcat([frame1, frame2])
        cv2.imshow("Cameras", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera1.release()
camera2.release()
cv2.destroyAllWindows()
