import csv
import sqlite3
import os

def sql_to_csv(db_file, table_name, csv_file):
   if not os.path.exists(db_file):
       raise FileNotFoundError(f"Database file '{db_file}' not found")
   
   conn = sqlite3.connect(db_file)
   cursor = conn.cursor()
   
   cursor.execute(f"SELECT * FROM {table_name}")
   rows = cursor.fetchall()
   
   cursor.execute(f"PRAGMA table_info({table_name})")
   columns = [column[1] for column in cursor.fetchall()]
   
   with open(csv_file, mode='w', encoding='utf-8', newline='') as csv_file:
       writer = csv.writer(csv_file)
       writer.writerow(columns)
       writer.writerows(rows)
   
   conn.close()

if __name__ == "__main__":
   sql_to_csv("database.db", "table_name", "output.csv")
