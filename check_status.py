import os
import sqlite3




def present_status(image_file_path):

    image_file_path=os.path.join("Uploaded_Images",image_file_path)
    query=f"select process_status from files where unique_string='{image_file_path}';"
    
    conn=sqlite3.connect('ML_Database1.db')
    cursor=conn.cursor()
    cursor.execute(query)
    status=cursor.fetchone()
    print("is this working")
    print(status)

    conn.commit()

    return status 

