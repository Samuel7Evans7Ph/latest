from deepface import DeepFace
def deep_face(img1_path,img2_path):
    result = DeepFace.verify(
  img1_path,
  img2_path)
    return result['verified']
