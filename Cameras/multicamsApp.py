"""
Here is some sample code that displays images from multiple cameras in a single window using OpenCV and Python.
 The code includes buttons that allow the user to switch between the different cameras.
 This code assumes that you have two cameras connected to your system.
  You can modify the code to add more cameras by creating additional trackbars and video capture objects.
"""
import cv2
import numpy as np

# Create a window to display the images
cv2.namedWindow("Cameras")

# Define the callback function for the buttons
def switch_camera(x):
    global current_camera
    current_camera = x

# Create buttons for switching between cameras
cv2.createTrackbar("Camera 1", "Cameras", 0, 1, switch_camera)
cv2.createTrackbar("Camera 2", "Cameras", 0, 1, switch_camera)

# Set the current camera to camera 1
current_camera = 1

# Open the first camera
cap1 = cv2.VideoCapture(0)

# Open the second camera
cap2 = cv2.VideoCapture(1)

while True:
    # Capture frame-by-frame
    if current_camera == 1:
        ret, frame = cap1.read()
    else:
        ret, frame = cap2.read()

    # Display the resulting frame
    cv2.imshow('Cameras', frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap1.release()
cap2.release()
cv2.destroyAllWindows()
