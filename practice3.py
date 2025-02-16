import cv2

# Load the image
image = cv2.imread(r"C:\Users\tauro\Downloads\0052_png_jpg.rf.0c6953cf399fc96860adf1d9db139235.jpg", 0)  # 0 to load in grayscale

# Apply a binary threshold to the image
_, thresholded_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Display the original and thresholded images
cv2.imshow('Original Image', image)
cv2.imshow('Thresholded Image', thresholded_image)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()