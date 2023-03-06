"""
This code will create a window with the specified name and size,
and continuously display the images from the two cameras side by side in the window.
The loop will run until the user presses the 'q' key, at which point the cameras will be released and the window will be destroyed.
"""
import cv2
import numpy as np
# Initialize the two cameras
cam1 = cv2.VideoCapture(0)
cam2 = cv2.VideoCapture(1)

# Set the window name and size
window_name = "Cameras"
window_size = (640, 480)

# Create a window to display the images
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.resizeWindow(window_name, window_size)

while True:
    # Read frames from the cameras
    ret1, frame1 = cam1.read()
    ret2, frame2 = cam2.read()

    # Check if the frames were successfully read
    if not (ret1 and ret2):
        break

    # Resize the images to fit the window size
    frame1 = cv2.resize(frame1, window_size)
    frame2 = cv2.resize(frame2, window_size)

    # Create a blank image with the same size as the window
    blank_image = np.zeros((window_size[1], window_size[0], 3), np.uint8)

    # Add the two images side by side
    combined_image = np.concatenate((frame1, frame2), axis=1)

    # Display the combined image
    cv2.imshow(window_name, combined_image)

    # Check if the user pressed 'q' to quit
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

# Release the cameras and destroy the window
cam1.release()
cam2.release()
cv2.destroyAllWindows()
