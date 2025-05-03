import os
import cv2

# Path where the dataset will be stored
DATA_DIR = './data'

# Create the base directory if it doesn't exist
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# Define the number of categories/classes and number of images per class
number_of_classes = 4
dataset_size = 100

# Initialize webcam capture (change the index if needed)
cap = cv2.VideoCapture(1)

for class_id in range(number_of_classes):
    # Create a folder for the current class if it doesn't exist
    class_dir = os.path.join(DATA_DIR, str(class_id))
    if not os.path.exists(class_dir):
        os.makedirs(class_dir)

    print(f'Collecting data for class {class_id}')

    # Wait for user to start capturing images
    while True:
        ret, frame = cap.read()
        cv2.putText(frame, 'Ready? Press "Q" to start capturing!', (100, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) == ord('q'):
            break

    # Capture images for the current class
    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        if not ret:
            continue
        cv2.imshow('frame', frame)
        cv2.waitKey(25)

        # Save the captured frame to the corresponding class folder
        image_path = os.path.join(class_dir, f'{counter}.jpg')
        cv2.imwrite(image_path, frame)

        counter += 1

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
