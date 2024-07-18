import cv2
import matplotlib.pyplot as plt
import os
from deepface import DeepFace
import numpy as np


face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)


def bounding_box(img):
    grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face = face_classifier.detectMultiScale(
        grey_img, scaleFactor=1.1, minNeighbors=4, minSize=(40, 40)
    )
    count = 0
    for x, y, w, h in face:
        image = img[y : y + h, x : x + w]
        count += 1
        cv2.imwrite(os.path.join("hello0hello.jpg"), image)
        return image

    return len(face)


cap = cv2.VideoCapture(0)
count = 0
name = input("enter the name of the person")
count = 0
while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("image", frame)

    embedding_list = []

    if cv2.waitKey(1) & 0xFF == ord("a"):
        frame = bounding_box(frame)
        trained_embedding = DeepFace.represent(frame, model_name="VGG-Face")
        np.array(trained_embedding)
        embedding_list.append(trained_embedding)
        count += 1
        if count == 10:
            np.array(embedding_list)
            np.save(
                os.path.join("Database", f"{name}_embedding.npy"), trained_embedding
            )
            break


cap.release()
cv2.destroyAllWindows()
