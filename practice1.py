import cv2
import numpy as np

# Load an image from file
image = cv2.imread(r"C:\Users\tauro\Downloads\0052_png_jpg.rf.0c6953cf399fc96860adf1d9db139235.jpg")

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Perform edge detection using the Canny algorithm
edges = cv2.Canny(gray_image, 100, 200)

# Display the original image in a window
cv2.imshow('Original Image', image)

# Display the edges in a window
cv2.imshow('Edges', edges)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()