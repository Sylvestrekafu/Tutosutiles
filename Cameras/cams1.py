import cv2
import torch

# Charger le modèle YOLOv5
model = torch.hub.load('ultralytics/yolov5', 'yolov5x', pretrained=True)

camera1 = cv2.VideoCapture(0)
camera2 = cv2.VideoCapture(4)

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
        frame1 = results1.render()[0]
        frame2 = results2.render()[0]

        # Concaténer les images pour l'affichage
        frame = cv2.hconcat([frame1, frame2])
        cv2.imshow("Cameras", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera1.release()
camera2.release()
cv2.destroyAllWindows()
