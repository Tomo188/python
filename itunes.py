import json
from textwrap import indent
import requests
import sys
from say import godbye

resp = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1]
)
# print(json.dumps(resp.json(), indent=2))
o = resp.json()


for result in o["results"]:
    print(result["trackName"])

print(godbye(sys.argv[1]))
print(__name__)
