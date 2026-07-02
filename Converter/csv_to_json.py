import csv
import json

def csv_to_json(csv_file, json_file):
   with open(csv_file, mode='r', encoding='utf-8') as csv_file:
       csv_reader = csv.reader(csv_file)
       header = next(csv_reader)
       data = []
       for row in csv_reader:
           if row:
               data.append(dict(zip(header, row)))
   
   with open(json_file, mode='w', encoding='utf-8') as json_file:
       json.dump(data, json_file, indent=4)

if __name__ == "__main__":
   csv_to_json("input.csv", "output.json")
