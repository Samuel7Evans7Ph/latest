import os
#import cv2
import numpy as np
from tensorflow.keras.models import model_from_json
import tensorflow as tf
import pickle

#from layers import L1Dist

#from trial import *

from deepface import DeepFace

# Load the model architecture
#mode=tf.keras.models.load_model(model_path,custom_objects={'L1Dist':L1Dist})

#model = tf.keras.models.load_model(model_path, custom_objects={'L1Dist': L1Dist})
#model=tf.keras.models.load_model('c_siamese_model6.keras.zip')
def preprocess(file_path):
    byte_img=tf.io.read_file(file_path)

    img=tf.io.decode_jpeg(byte_img)

    img=tf.image.resize(img,(100,100))

    img=img/255

    return img


def verify(detection_threshold,verification_threshold,input_image,input_img_path):
    max_confidence=0

    person_name=""
   # print("hello")
    input_embedding=DeepFace.represent(input_img_path,model_name='VGG-Face')

    input_embedding=input_embedding[0]["embedding"]
    #print(len(input_embedding))

    for name in os.listdir('Database'):
        count=0
        #print(count)
        #print("this is embedding",embedding)
       # for validation_embedding in embedding:
        embedding_list=np.load(os.path.join('Database',name),allow_pickle=True)
        #print("lenght",len(embedding_list))
        for embedding in embedding_list:
            #print(embedding[0])
            validation_embedding=embedding["embedding"]
# Convert validation_embedding to a list of floats
            similarity=DeepFace.verify(input_embedding,validation_embedding)
            #print(similarity)
            if similarity['verified']:
                count+=1
                #print("ahi")
        
        new_conf=count/len(embedding_list)
            #print(new_conf,"this is the confidence")

        #:/print(new_conf)
        if new_conf>max_confidence:
            max_confidence=new_conf
            person_name=name
        
    if max_confidence<verification_threshold:
        return "Nobody"
    else:
        return person_name


def integrate():

    #with open('model_architecture.json','r') as json_file:
     #   loaded_model_json=json_file.read()
      #  model=model_from_json(loaded_model_json,custom_objects={'L1Dist':L1Dist})
    
    #model.load_weights('model_weights.h5')
    
    
    model_path = '/home/evans_sam/temp/siamese_model.keras'
    
    
    person_names=[] 
    for files in os.listdir('Image_Files'):
    
        input_img=preprocess(os.path.join('Image_Files',files))
    
        input_img_path=os.path.join('Image_Files',files)
        detection_threshold=0.5
    
        verification_threshold=0.5
        
    
        person_name=verify(detection_threshold,verification_threshold,input_img,input_img_path)
        if person_name!='Nobody':
            person_name=person_name[:-14]   
            #person_names.append(person_name[:-14])
        print(person_name)
    
    

if __name__=="__main__":
    main()








   # self.verification.text='verified' if verified ==True else 'Unverified'
