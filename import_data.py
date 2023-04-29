import controller as cont
import json


def Open_file(name):
    with open(name) as json_file:
        data = json.load(json_file)
    return data