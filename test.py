
import requests
import json

word = 'monkey'

a = requests.get(f'https://dictionaryapi.com/api/v3/references/collegiate/json/{word}?key=addbddd3-bf9d-4007-967f-6497521bac90')

b = a.json()

print(json.dumps(b, indent=4))