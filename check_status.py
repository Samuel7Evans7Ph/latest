import os
import sqlite3


def present_status(token_id):

    query = f"select process_status from files where unique_string='{token_id}';"

    conn = sqlite3.connect("ML_Database1.db")
    cursor = conn.cursor()
    cursor.execute(query)
    status = cursor.fetchone()

    conn.commit()

    return status
