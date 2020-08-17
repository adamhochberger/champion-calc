import requests
import json
import pytest
from champion import Champion

class Test_TestComponentInit:
    v = Component([15, 40, 65, 90, 115])
    # Overall testing for functionality of some classes
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

