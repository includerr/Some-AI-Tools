import json
import sqlite3
import os

def sql_to_json(db_file, table_name, json_file):
   if not os.path.exists(db_file):
       raise FileNotFoundError(f"Database file '{db_file}' not found")
   
   conn = sqlite3.connect(db_file)
   cursor = conn.cursor()
   
   cursor.execute(f"SELECT * FROM {table_name}")
   rows = cursor.fetchall()
   
   cursor.execute(f"PRAGMA table_info({table_name})")
   columns = [column[1] for column in cursor.fetchall()]
   
   data = [dict(zip(columns, row)) for row in rows]
   
   with open(json_file, mode='w', encoding='utf-8') as json_file:
       json.dump(data, json_file, indent=4)
   
   conn.close()

if __name__ == "__main__":
   sql_to_json("database.db", "table_name", "output.json")
