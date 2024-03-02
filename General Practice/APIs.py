import requests
import sys
import json
response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + argv[1])

o=response.json()
#print(json.dumps(o, indent=2))
for result in o["results"]:
    print(result["trackName"])
