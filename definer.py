
import requests

class Dictionary:

    api_url = "https://api.dictionaryapi.dev/api/v2/entries/en/"

    def __init__(self):
        pass

    def define(self, word):
        response = requests.get(Dictionary.api_url + word)
        if response.status_code != 200:
            return "404"
        return response.content

