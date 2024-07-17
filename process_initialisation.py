import sqlite3
from meta_integrate import *
import cv2
import os

def initialise(image_file_name):
    #image_file_name=os.path.join("Uploaded_Images",image_file_name)
    img=cv2.imread(image_file_name)
    no_of_faces=meta_integrate(img,image_file_name)

#    for i in range(100):
 
 #print(i)

    conn=sqlite3.connect('ML_Database1.db')
    cursor=conn.cursor()
    query2 =f"UPDATE files SET process_status='done' where file_name='{image_file_name}';"

    cursor.execute(query2)
    query3 =f"UPDATE files SET no_of_faces='{no_of_faces}' where file_name='{image_file_name}';"
    #cursor.execute(query2)
    conn.commit()
    cursor.close()
    conn.close()


   # print("hai")



    
    return



