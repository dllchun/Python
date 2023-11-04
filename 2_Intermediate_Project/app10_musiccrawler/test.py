import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "data.db")


connection = sqlite3.connect(db_path, timeout=10)
cursor = connection.cursor()
values = [
    ("test", "test", "2028-03-11"),
    ("test1", "test2", "2028-03-12"),
]
query = "INSERT INTO events VALUES(?,?,?)"
cursor.executemany(query, values)
connection.commit()


cursor.execute("SELECT * FROM events")
row = cursor.fetchall()
print(row)
