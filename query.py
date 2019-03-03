import requests
import json

# Initial call to api to check most recent version listed in the file listing (LIFO system results in it being at the first position)
versionCheck = requests.get("https://ddragon.leagueoflegends.com/api/versions.json")
recentVersion = json.loads(versionCheck.text)[0]

# Print statement to verify the current version it is on
print(recentVersion)

# Secondary api call to the overall champion file that uses most recent version to pull information
r = requests.get("http://ddragon.leagueoflegends.com/cdn/" + recentVersion + "/data/en_US/champion.json")
data = json.loads(r.text)

# Test statement to verify that champion names are being pulled properly
#for key in list(data["data"]):
champ = requests.get("http://ddragon.leagueoflegends.com/cdn/" + recentVersion + "/data/en_US/champion/" + "Azir" + ".json")

# print(json.dumps(json.loads(champ.text), indent=2))

for entry in list(data["data"]):
    champ = requests.get("http://ddragon.leagueoflegends.com/cdn/" + recentVersion + "/data/en_US/champion/" + entry + ".json")
    print(entry)
    print(json.loads(champ.text)["data"][entry]["spells"][0]["name"])
    print()


# Names of all champions can be pulled using 
# data = json.loads(r.text) 
# list(data["data"])
# where r is a request made to the champion.json file
