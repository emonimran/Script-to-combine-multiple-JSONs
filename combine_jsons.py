import json
import os

# Path of the folders containing the JSON files
path = '../ForCombining/'

# Combining format
combined_json = {'description': [], 'tags': [], 'size': {}, 'objects': []}

for file in os.listdir(path):
    if file.endswith('.json'):
        # Open the json file and read the contents
        with open(os.path.join(path, file)) as f:
            data = json.load(f)
            print(data)
            for obj in data['objects']:

                if obj['classTitle'] == "Vehicle":
                    obj['classTitle'] = 'car'

                elif obj['classTitle'] == "License Plate":

                    obj['classTitle'] = 'number'

        combined_json['description'].extend(data['description'])
        combined_json['tags'].extend(data['tags'])
        combined_json['size'].update(data['size'])
        combined_json['objects'].extend(data['objects'])

# Combined JSON file
with open('combined.json', 'w') as f:
    json.dump(combined_json, f, indent=9)
