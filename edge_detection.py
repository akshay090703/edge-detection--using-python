import cv2
import numpy as np

# Load the image in grayscale
image = cv2.imread('image.jpg', 0)

# Apply Sobel operator
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

# Compute the gradient magnitude and orientation
gradient_magnitude = np.sqrt(sobel_x*2 + sobel_y*2)
gradient_orientation = np.arctan2(sobel_y, sobel_x)

# Apply Canny edge detection
edges_canny = cv2.Canny(image, 100, 200)

# Display the results
cv2.imshow('Original Image', image)
cv2.imshow('Sobel X', cv2.convertScaleAbs(sobel_x))
cv2.imshow('Sobel Y', cv2.convertScaleAbs(sobel_y))
cv2.imshow('Gradient Magnitude', cv2.convertScaleAbs(gradient_magnitude))
cv2.imshow('Canny Edges', edges_canny)
cv2.waitKey(0)
cv2.destroyAllWindows()