import cv2
import tensorflow as tf
import os
# import matplotlib.pyplot as plt

import numpy as np

from PIL import Image

import io

def bounding_box(img,face_classifier):
    grey_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #cv2.imwrite(os.path.join("Image_Files","hello.jpg"),img)
    face=face_classifier.detectMultiScale(grey_img,scaleFactor=1.1,minNeighbors=4,minSize=(40,40))

    print("The number of faces are",len(face),)
    #os.makedirs("Image_Files")
    count=0
    for (x,y,w,h) in face:
        #cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,4),1)
        file_name=str(count)+'.jpg'
        save_path=os.path.join("Image_Files",file_name)
        image=img[y:y+h,x:x+w]
        count+=1
        #print(image)
        cv2.imwrite(save_path,image)
    


    return len(face)

def load_image_into_numpy_array(data):
    return np.array(Image.open(io.BytesIO(data)))



def start_verification(image):


    img_path='/home/opentrends/Downloads/5.jpg'
    # print("here")
    #video_capture=cv2.VideoCapture('/home/opentrends/Downloads/3.mp4')
    face_classifier=cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_frontalface_default.xml")
    # while True:

        # result,vid_frame=video_capture.read()
        # if not result:
        #     break
    #image_np = load_image_into_numpy_array(image)
    #input_tensor = tf.convert_to_tensor(image_np)  
    #cv2.imwrite(os.path.join("Image_Files","5.jpg"),image_np)

    no_of_faces=bounding_box(image,face_classifier)
    #cv2.imshow("loading",img_path)
    cv2.waitKey(0)

    cv2.destroyAllWindows()

        # gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        

    
        # print("Number of faces detected:", len(face))


        # for (x, y, w, h) in face:
        #     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4)

    #img_rgb = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    return no_of_faces


    # video_capture.release()
    # cv2.destroyAllWindows()


