import os

# import cv2
import numpy as np
from tensorflow.keras.models import model_from_json
import tensorflow as tf
import pickle


from deepface import DeepFace


def preprocess(file_path):
    byte_img = tf.io.read_file(file_path)
    img = tf.io.decode_jpeg(byte_img)
    img = tf.image.resize(img, (100, 100))
    img = img / 255

    return img


def verify(detection_threshold, verification_threshold, input_image, input_img_path):
    max_confidence = 0

    person_name = ""
    input_embedding = DeepFace.represent(input_img_path, model_name="VGG-Face")
    input_embedding = input_embedding[0]["embedding"]
    for name in os.listdir("Database"):
        count = 0
        embedding_list = np.load(os.path.join("Database", name), allow_pickle=True)
        for embedding in embedding_list:
            validation_embedding = embedding["embedding"]
            similarity = DeepFace.verify(input_embedding, validation_embedding)
            if similarity["verified"]:
                count += 1

        new_conf = count / len(embedding_list)

        if new_conf > max_confidence:
            max_confidence = new_conf
            person_name = name

    if max_confidence < verification_threshold:
        return "Nobody"
    else:
        return person_name


def integrate():

    for files in os.listdir("Image_Files"):
        input_img = preprocess(os.path.join("Image_Files", files))
        input_img_path = os.path.join("Image_Files", files)
        detection_threshold = 0.5
        verification_threshold = 0.5
        person_name = verify(
            detection_threshold, verification_threshold, input_img, input_img_path
        )
        if person_name != "Nobody":
            person_name = person_name[:-14]
        print(person_name)


if __name__ == "__main__":
    main()
