# Relative files
import os

# Environment variables
from dotenv import load_dotenv


def getCredentials():
    load_dotenv()
    token = os.getenv('TOKEN')
    user = os.getenv('USER')

    return token, user
