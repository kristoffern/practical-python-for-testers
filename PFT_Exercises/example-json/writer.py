import json
birds = {
    "parrot": {"state": "pining", "origin": "Norway"},
    "swallow": {"state": "unladen", "origin": "Africa"}
}


f = open('storage.json', 'w')
json.dump(birds, f, sort_keys=True, indent=4)
f.close()
