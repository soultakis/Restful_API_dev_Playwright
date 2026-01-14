import json

# Utility function for reading the json file
# I will use it in all requests that need to read the data from a file
# So I create a function that opens a file from a file_path (not the same for all requests)
# and returns the json output
def read_json(file_path):
    file  = open(file_path, "r")
    return json.load(file)