import csv
import json

def json_to_csv(json_file, csv_file):
   with open(json_file, mode='r', encoding='utf-8') as json_file:
       data = json.load(json_file)
   
   if isinstance(data, list) and data:
       header = data[0].keys()
       with open(csv_file, mode='w', encoding='utf-8', newline='') as csv_file:
           writer = csv.DictWriter(csv_file, fieldnames=header)
           writer.writeheader()
           writer.writerows(data)
   elif isinstance(data, dict):
       header = data.keys()
       with open(csv_file, mode='w', encoding='utf-8', newline='') as csv_file:
           writer = csv.DictWriter(csv_file, fieldnames=header)
           writer.writeheader()
           writer.writerow(data)

if __name__ == "__main__":
   json_to_csv("input.json", "output.csv")
