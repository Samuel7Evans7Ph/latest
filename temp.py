import sqlite3
import uuid


def add_file_path(file_name):
    # Connect to the SQLite database
    conn = sqlite3.connect("ML_Database1.db")
    cursor = conn.cursor()
    unique_string = uuid.uuid4()
    query_stmt = f"INSERT INTO files (file_name, process_status,unique_string) VALUES ( '{file_name}', 'In Progress','{unique_string}');"
    cursor.execute(query_stmt)
    conn.commit()
    cursor.close()
    conn.close()
    return unique_string
