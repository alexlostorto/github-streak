# Relative files
import os

# Reading JSON file
import json


def getCredentials():
    directory = os.path.dirname(__file__)
    with open(os.path.join(directory, "../secrets.json")) as f:
        jsonData = json.load(f)
        token = jsonData['token']
        user = jsonData['user']

    return token, user
