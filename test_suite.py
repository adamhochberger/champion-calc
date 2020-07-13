from component import Component
from values import Damage_Heal
import pytest

class Test_TestComponentInit:
    v = Component([15, 40, 65, 90, 115])
    # Overall testing for functionality of some classes

    def test_component_values(self):
        assert self.v.scaling == {"value": [15, 40, 65, 90, 115]}

    def test_component_rank(self):
        assert self.v.scaling["value"][4] == 115

    def test_component_dict(self):
        assert Damage_Heal("Physical", self.v.scaling).scaling == {"kind": "Physical", 
        "base": self.v.scaling, "ad_%": Component().scaling, "ap_%": Component().scaling, "hp_%": Component().scaling}

    