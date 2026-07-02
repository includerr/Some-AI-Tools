import json

def json_to_jsonl(json_file, jsonl_file):
   with open(json_file, mode='r', encoding='utf-8') as json_file:
       data = json.load(json_file)
   
   if isinstance(data, list):
       with open(jsonl_file, mode='w', encoding='utf-8') as jsonl_file:
           for item in data:
               jsonl_file.write(json.dumps(item) + '\n')
   else:
       with open(jsonl_file, mode='w', encoding='utf-8') as jsonl_file:
           jsonl_file.write(json.dumps(data) + '\n')

if __name__ == "__main__":
   json_to_jsonl("input.json", "output.jsonl")
