import cv2
import numpy as np

# Define the lower and upper bounds for the ball's color in HSV
# Replace these values with the ones you found using the trackbars
lower_color = np.array([30, 150, 50])
upper_color = np.array([50, 255, 255])

# Load an image from file
image = cv2.imread(r"C:\Users\tauro\Downloads\0052_png_jpg.rf.0c6953cf399fc96860adf1d9db139235.jpg")

# Check if the image was loaded successfully
if image is None:
    print("Error: Could not load image.")
    exit()

# Convert the image to HSV color space
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

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

    # Draw the circle and centroid on the image
    cv2.circle(image, center, radius, (0, 255, 0), 2)
    cv2.circle(image, center, 5, (0, 0, 255), -1)

    # Implement logic to move the robot towards the ball
    # For example, you can use the center coordinates to determine the direction
    if center[0] < image.shape[1] // 3:
        print("Move Left")
    elif center[0] > 2 * image.shape[1] // 3:
        print("Move Right")
    else:
        print("Move Forward")

# Display the image and mask
cv2.imshow('Image', image)
cv2.imshow('Mask', mask)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()