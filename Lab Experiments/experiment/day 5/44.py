
# Image Segmentation using Computer Vision
# Python 3.11 + OpenCV

try:
    import cv2
except ImportError:
    print("OpenCV is not installed!")
    print("Run: py -3.11 -m pip install opencv-python")
    exit()

# Step 1: Load image
image = cv2.imread("image.jpg")

if image is None:
    print("Error: image.jpg not found!")
    print("Place an image named image.jpg in the same folder.")
    exit()

print("Image loaded successfully!")

# Step 2: Display original image
cv2.imshow("Original Image", image)

# Step 3: Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

print("Grayscale conversion completed!")

# Step 4: Remove noise
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Step 5: Apply thresholding
threshold, segmented = cv2.threshold(
    blur,
    0,
    255,
    cv2.THRESH_BINARY + cv2.THRESH_OTSU
)

# Step 6: Display segmented image
cv2.imshow("Segmented Image", segmented)

# Step 7: Save output
cv2.imwrite("segmented_image.jpg", segmented)

# Step 8: Display results
print("\n===== IMAGE SEGMENTATION =====")
print("Original Image: Loaded")
print("Grayscale Conversion: Completed")
print("Noise Removal: Completed")
print("Image Segmentation: Completed")
print("Output saved as segmented_image.jpg")

# Wait and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
