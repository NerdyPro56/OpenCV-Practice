import cv2
import numpy as np

# Define the lower and upper bounds for the ball's color in HSV
lower_color = np.array([30, 150, 50])
upper_color = np.array([50, 255, 255])

# Capture video from the camera
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a mask for the ball's color
    mask = cv2.inRange(hsv, lower_color, upper_color)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # If contours are found, find the largest one
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        (x, y), radius = cv2.minEnclosingCircle(largest_contour)
        center = (int(x), int(y))
        radius = int(radius)

        # Draw the circle and centroid on the frame
        cv2.circle(frame, center, radius, (0, 255, 0), 2)
        cv2.circle(frame, center, 5, (0, 0, 255), -1)

        # Implement logic to move the robot towards the ball
        # For example, you can use the center coordinates to determine the direction
        if center[0] < frame.shape[1] // 3:
            print("Move Left")
        elif center[0] > 2 * frame.shape[1] // 3:
            print("Move Right")
        else:
            print("Move Forward")

    # Display the frame
    cv2.imshow('Frame', frame)
    cv2.imshow('Mask', mask)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()