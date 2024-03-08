import json

# Function to read dictionaries from a text file
def read_prefs_from_file(filename):
    file = open(filename, 'r')
    data = file.read()
    preferences = json.loads(data)
    file.close()
    return preferences
