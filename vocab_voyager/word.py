
import json
from dataclasses import dataclass
import requests

@dataclass
class Variant:
    """Class for keeping track of a variant of a word"""
    text: str
    part_of_speech: str
    defn: str

    def __repr__(self):
        return self.defn

class Word:

    api_url = "https://api.dictionaryapi.dev/api/v2/entries/en/"

    @staticmethod
    def define(query):
        response = requests.get(Word.api_url + query, timeout=5)
        if response.status_code != 200:
            return "404"
        return response.content

    def __init__(self, word: str):
        self.word = word

        # calling define() to find definition of word
        definition = Word.define(word)

        # if definition not found, word does not exist
        if definition == '404':
            self.meanings = 404
            return

        query_response = json.loads(definition)
        self.meanings = []

        # deciphering json response
        for etymology in query_response:
            self.meanings.append(dict())

            for part_of_speech in etymology['meanings']:
                self.meanings[-1][part_of_speech['partOfSpeech']] = []
                for variant in part_of_speech['definitions']:
                    self.meanings[-1][part_of_speech['partOfSpeech']].append(Variant(word, part_of_speech['partOfSpeech'], variant['definition']))

    # method to print a word out
    def __repr__(self):
        info = ''
        cnt = 1

        for etymology in self.meanings:
            info += "Etymology #" + str(cnt) + '\n'
            for part_of_speech in etymology:
                info += ' ' * 2 + part_of_speech + '\n'
                for word in etymology[part_of_speech]:
                    info += ' ' * 4 + str(word) + '\n'
            info += '\n'
            cnt += 1
        return info



