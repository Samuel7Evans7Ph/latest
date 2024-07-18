import os

from integrate import *

from detect import *
import sqlite3

def meta_integrate(image,image_file_name):

    #will recieve the pic from from frontend via api
    faces=start_verification(image)

    conn=sqlite3.connect("MlDatabase1.db")
    cursor=conn.cursor()

    query="UPDATE Files set no_of_faces='{faces}' where file_name='{image_file_name}'"



    #after this is run ,a directory image files will be saved with each face detected as a seperate file

    integrate()
    #this will get us all the faces and their corresponding names guessed.
    #this must be further passed via api to the frontend

    #after this the status needs to be updated as finished in the database and perhaps the name could also be stored.






    











