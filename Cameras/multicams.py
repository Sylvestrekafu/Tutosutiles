"""
pip install opencv-python
"""
import cv2

camera1 = cv2.VideoCapture(0)
camera2 = cv2.VideoCapture(4)

if not camera1.isOpened():
    print('erreur ...cam1')

if not camera2.isOpened():
    print('erreur.. cam2')



while True:
    ret1, frame1 = camera1.read()
    ret2, frame2 = camera2.read()


    frame = cv2.hconcat([frame1, frame2])

    cv2.imshow("Cameras",frame)



    if cv2.waitKey(1) & 0xff == ord('q'):
        break

camera1.release()
camera2.release()




