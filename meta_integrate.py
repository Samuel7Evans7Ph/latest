import os

from integrate import *

from detect import *
import sqlite3


def meta_integrate(image, image_file_name):

    faces = start_verification(image)
    conn = sqlite3.connect("MlDatabase1.db")
    cursor = conn.cursor()
    query = "UPDATE Files set no_of_faces='{faces}' where file_name='{image_file_name}'"
    integrate()
