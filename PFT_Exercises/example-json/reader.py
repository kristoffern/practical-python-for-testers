import json
from pprint import pprint
f = open('storage.json', 'r')
avians = json.loads(f.read())

pprint(avians)  # Pretty!
