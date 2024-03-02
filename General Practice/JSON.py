import json

data = {'name': 'John', 'age': 30, 'city': 'New York'}
json_data = json.dumps(data, indent=2)

print("JSON Data:")
print(json_data)

