
# Object Detection using a Pre-trained Model
# MobileNet SSD + OpenCV
# Compatible with Python 3.11

import cv2
import numpy as np
import os
import urllib.request

print("===== OBJECT DETECTION SYSTEM =====")

# Create model folder
os.makedirs("models", exist_ok=True)

# Model file paths
prototxt = "models/deploy.prototxt"
model = "models/mobilenet.caffemodel"

# Download model files automatically
prototxt_url = (
    "https://raw.githubusercontent.com/"
    "chuanqi305/MobileNet-SSD/master/deploy.prototxt"
)

model_url = (
    "https://raw.githubusercontent.com/"
    "chuanqi305/MobileNet-SSD/master/"
    "mobilenet_iter_73000.caffemodel"
)

try:
    if not os.path.exists(prototxt):
        print("Downloading model configuration...")
        urllib.request.urlretrieve(prototxt_url, prototxt)

    if not os.path.exists(model):
        print("Downloading pre-trained model...")
        urllib.request.urlretrieve(model_url, model)

except Exception as e:
    print("Model download failed:", e)
    print("Check your internet connection.")
    raise SystemExit

# Object class names
CLASSES = [
    "background", "aeroplane", "bicycle", "bird",
    "boat", "bottle", "bus", "car", "cat", "chair",
    "cow", "diningtable", "dog", "horse",
    "motorbike", "person", "pottedplant",
    "sheep", "sofa", "train", "tvmonitor"
]

# Load pre-trained model
net = cv2.dnn.readNetFromCaffe(prototxt, model)

print("Pre-trained model loaded successfully!")

# Load input image
image = cv2.imread("image.jpg")

if image is None:
    print("Error: image.jpg not found!")
    print("Place image.jpg in the same folder as this program.")
    raise SystemExit

# Get image dimensions
(h, w) = image.shape[:2]

# Prepare image for model
blob = cv2.dnn.blobFromImage(
    image,
    0.007843,
    (300, 300),
    127.5
)

# Perform object detection
net.setInput(blob)
detections = net.forward()

print("\nDetected Objects:")

count = 0

# Process detection results
for i in range(detections.shape[2]):

    confidence = detections[0, 0, i, 2]

    # Confidence threshold
    if confidence > 0.50:

        class_id = int(detections[0, 0, i, 1])

        # Get bounding box coordinates
        box = detections[0, 0, i, 3:7] * np.array(
            [w, h, w, h]
        )

        (startX, startY, endX, endY) = box.astype("int")

        label = CLASSES[class_id]

        # Draw rectangle
        cv2.rectangle(
            image,
            (startX, startY),
            (endX, endY),
            (0, 255, 0),
            2
        )

        # Display label and confidence
        text = label + ": " + str(round(confidence * 100, 2)) + "%"

        cv2.putText(
            image,
            text,
            (startX, max(startY - 10, 20)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 0, 255),
            2
        )

        print(text)
        count += 1

# Display total objects
print("\nTotal Objects Detected:", count)

# Save output image
cv2.imwrite("detected_output.jpg", image)

# Display result
cv2.imshow("Object Detection Result", image)

print("\nDetection Completed Successfully!")
print("Output saved as detected_output.jpg")

cv2.waitKey(0)
cv2.destroyAllWindows()
