import cv2

# Open the video file
cap = cv2.VideoCapture(r"C:\Users\tauro\Downloads\Renai Circulation「恋愛サーキュレーション」歌ってみた【＊なみりん】.mp4")

# Check if the video file opened successfully
if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

# Read and display the video frames
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply a Gaussian blur to the frame
    blurred_frame = cv2.GaussianBlur(gray_frame, (15, 15), 0)

    edges = cv2.Canny(gray_frame, 100, 200)
    # Display the original frame
    cv2.imshow('Original Video', frame)

    # Display the processed frame
    cv2.imshow('Processed Video', blurred_frame)
    cv2.imshow('Edges', edges)
    # Press 'q' to exit the video display
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()