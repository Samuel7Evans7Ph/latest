import os
import sqlite3


def update_database(token_id):
    query1 = (
        f"UPDATE files SET process_status='running' where unique_string='{token_id}';"
    )

    query2 = f"select file_name from files where unique_string='{token_id}';"
    conn = sqlite3.connect("ML_Database1.db")
    cursor = conn.cursor()
    cursor.execute(query1)

    conn.commit()
    cursor.execute(query2)
    image_file_name = cursor.fetchone()
    cursor.close()
    conn.close()

    return image_file_name[0]
