import json

# Data to be written
dictionary = {
    "id": 1,
    "name": "Alex"

}

# Serializing json
json_object = json.dumps(dictionary, indent=4)

# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)