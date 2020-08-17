import requests
import json
import pytest
from champion import Champion

champ = requests.get("http://ddragon.leagueoflegends.com/cdn/10.16.1/data/en_US/champion/" + "Annie" + ".json")
annie = Champion("Annie", json.loads(champ.text)["data"]["Annie"]["stats"])

stats= {
    "hp": 524,
    "hpperlevel": 88,
    "mp": 418,
    "mpperlevel": 25,
    "attackdamage": 50.41,
    "attackdamageperlevel": 2.625
}

def test_champion_hp():
    assert annie.attributes["hp"] == (stats["hp"], stats["hpperlevel"])

@pytest.mark.xfail
def test_champion_mp():
    assert annie.attributes["mp"] == (stats["mp"], stats["mpperlevel"])

def test_champion_attackdamage_level():
    assert annie.get_attr_at_level("attackdamage", 5) == stats["attackdamage"] + stats["attackdamageperlevel"] * 5

