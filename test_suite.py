from component import Component
from values import Damage_Heal
import pytest

class Test_TestComponentInit:
    v = Component([15, 40, 65, 90, 115])
    # Overall testing for functionality of some classes

    def test_component_values(self):
        assert self.v.values == {"value": [15, 40, 65, 90, 115]}

    def test_component_rank(self):
        assert self.v.comp_at_rank(5) == 115

    def test_component_dict(self):
        assert Damage_Heal("Physical", self.v.values).values == {"kind": "Physical", 
        "base": self.v.values, "ad_%": {}, "ap_%": {}, "hp_%": {}}

    