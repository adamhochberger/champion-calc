import requests
import json

r = requests.get("http://ddragon.leagueoflegends.com/cdn/9.4.1/data/en_US/champion/Azir.json")
data = json.loads(r.text)
print(json.dumps(data["data"]["Azir"]["spells"], indent=4))