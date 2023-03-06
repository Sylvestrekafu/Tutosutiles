"""
This code will open two video capture objects, one for each camera, and display the frames side by side in a single window.
 It will also write the frames to two separate video files, "cam1.avi" and "cam2.avi". The loop will continue until the user presses the "q" key,
at which point the video capture and video writer objects will be released and all the windows will be destroyed.
"""
import cv2


# Set up the video capture objects for each camera
cam1 = cv2.VideoCapture(0)
cam2 = cv2.VideoCapture(1)

# Set the window name
window_name = "Multi-Camera Display"

# Create a named window
cv2.namedWindow(window_name)

# Set up the position of the windows for the two cameras
cv2.moveWindow(window_name, 0, 1)

# Set the width and height of the frames
frame_width = int(cam1.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam1.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Set up the video writers for each camera
out1 = cv2.VideoWriter("cam1.avi", cv2.VideoWriter_fourcc(*'MJPG'), 30, (frame_width, frame_height))
out2 = cv2.VideoWriter("cam2.avi", cv2.VideoWriter_fourcc(*'MJPG'), 30, (frame_width, frame_height))

# Start the main loop
while True:
    # Read the frames from each camera
    ret1, frame1 = cam1.read()
    ret2, frame2 = cam2.read()

    # Check if the frames are valid
    if not ret1 or not ret2:
        break

    # Write the frames to the video writers
    out1.write(frame1)
    out2.write(frame2)

    # Display the frames side by side
    cv2.imshow(window_name, cv2.hconcat([frame1, frame2]))

    # Check if the user pressed "q" to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the video capture and video writer objects
cam1.release()
cam2.release()
out1.release()
out2.release()

# Destroy all the windows
cv2.destroyAllWindows()
