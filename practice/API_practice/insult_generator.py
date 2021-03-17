import json

import requests

insult_json = requests.get(
    'https://evilinsult.com/generate_insult.php?lang=en&type=json').json()

print(insult_json['insult'])