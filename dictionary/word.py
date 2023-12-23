import json
from dataclasses import dataclass
import requests

@dataclass
class Variant:
    """Class for keeping track of a word's variants"""
    text: str
    part_of_speech: str
    definition: str

    def __repr__(self):
        return self.definition

class Word:

    api_url = "https://api.dictionaryapi.dev/api/v2/entries/en/"

    @staticmethod
    def define(query):
        # calling API to get info about word
        response = requests.get(Word.api_url + query, timeout=5)
        
        if response.status_code != 200:
            return None
        return response.content

    def __init__(self, word: str):
        self.word = word
        definition = Word.define(word)

        # if definition not found, word does not exist
        if definition is None:
            self.meanings = None
            return

        # parsing the API response to extract information next
        query_response = json.loads(definition)
        self.meanings = []

        # assembling list of meanings based on etymology by deconstructing structure of API response
        for etymology in query_response:
            curr_etymology = dict()
            
            for part_of_speech in etymology['meanings']:
                curr_etymology[part_of_speech['partOfSpeech']] = []

                for variant in part_of_speech['definitions']:
                    curr_etymology[part_of_speech['partOfSpeech']].append(Variant(word, part_of_speech['partOfSpeech'], variant['definition']))

            self.meanings.append(curr_etymology)

    # __repr__ useful for debugging
    def __repr__(self):
        info = ''
        for index, etymology in enumerate(self.meanings):
            info += f'Etymology #{index}\n'
            for part_of_speech in etymology:
                info += f'  {part_of_speech}\n'
                for word in etymology[part_of_speech]:
                    info += f'    {word}\n'
            info += '\n'
        return info
