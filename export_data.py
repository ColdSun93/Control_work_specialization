import json

def Save_file(name, data_save, operat):
    with open(name, operat) as outfile:
        json.dump(data_save, outfile)