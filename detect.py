import cv2
import tensorflow as tf
import os

import numpy as np

from PIL import Image

import io


def bounding_box(img, face_classifier):
    grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face = face_classifier.detectMultiScale(
        grey_img, scaleFactor=1.1, minNeighbors=4, minSize=(40, 40)
    )
    print(
        "The number of faces are",
        len(face),
    )
    count = 0
    for x, y, w, h in face:
        file_name = str(count) + ".jpg"
        save_path = os.path.join("Image_Files", file_name)
        image = img[y : y + h, x : x + w]
        count += 1
        cv2.imwrite(save_path, image)

    return len(face)


def load_image_into_numpy_array(data):
    return np.array(Image.open(io.BytesIO(data)))


def start_verification(image):

    face_classifier = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )
    no_of_faces = bounding_box(image, face_classifier)
    cv2.waitKey(0)

    cv2.destroyAllWindows()

    return no_of_faces
