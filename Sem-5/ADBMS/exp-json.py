import json
from pprint import pprint

data = {
    "name": "John Doe",
    "age": 25,
    "city": "Exampleville",
    "is_student": False,
    "grades": [85, 90, 78],
}

fileWrite = open("file1.txt", "w")
json.dump(data, fileWrite, indent=2)
fileWrite.close()

fileRead = open("file1.txt", "r")
loaded_data = json.load(fileRead)
fileRead.close()

# print(dict(loaded_data)["name"])

print("\nLoaded Python data from file:")
pprint(loaded_data)
