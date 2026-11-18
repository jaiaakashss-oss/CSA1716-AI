
import cv2
import face_recognition
import os
import numpy as np

# Create folder for known faces
folder = "known_faces"

if not os.path.exists(folder):
    os.makedirs(folder)
    print("Created known_faces folder.")
    print("Add face images and run the program again.")
    exit()

# Store face data
known_encodings = []
known_names = []

# Load known faces
for file in os.listdir(folder):

    if file.lower().endswith((".jpg", ".jpeg", ".png")):

        image = face_recognition.load_image_file(
            os.path.join(folder, file)
        )

        encoding = face_recognition.face_encodings(image)

        if encoding:
            known_encodings.append(encoding[0])
            known_names.append(os.path.splitext(file)[0])
            print("Face loaded:", file)

print("\nStarting Face Recognition...")

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Webcam not found!")
    exit()

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # Resize frame
    small_frame = cv2.resize(
        frame, (0, 0), fx=0.25, fy=0.25
    )

    # Convert image
    rgb_frame = cv2.cvtColor(
        small_frame, cv2.COLOR_BGR2RGB
    )

    # Detect faces
    locations = face_recognition.face_locations(rgb_frame)

    encodings = face_recognition.face_encodings(
        rgb_frame, locations
    )

    # Recognize faces
    for encoding, location in zip(encodings, locations):

        name = "Unknown"

        if known_encodings:

            distances = face_recognition.face_distance(
                known_encodings, encoding
            )

            best_match = np.argmin(distances)

            if distances[best_match] < 0.50:
                name = known_names[best_match]

        # Face position
        top, right, bottom, left = location

        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw rectangle
        cv2.rectangle(
            frame,
            (left, top),
            (right, bottom),
            (0, 255, 0),
            2
        )

        # Display name
        cv2.putText(
            frame,
            name,
            (left, top - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (0, 255, 0),
            2
        )

    # Show output
    cv2.imshow("Face Recognition", frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Close camera
cap.release()
cv2.destroyAllWindows()

print("Face Recognition Completed")
