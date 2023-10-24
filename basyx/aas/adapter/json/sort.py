import json

# Open the input file and load the JSON data
with open('aasJSONSchemaV3010.json', 'r') as f:
    data = json.load(f)

# Sort the keys alphabetically
sorted_data = dict(sorted(data.items()))

# Open the output file and write the sorted JSON data
with open('output.json', 'w') as f:
    json.dump(sorted_data, f, indent=4)