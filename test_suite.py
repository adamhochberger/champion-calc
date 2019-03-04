from component import Component
from values import Damage_Heal
import pytest

class Test_TestComponentInit:

    # Overall testing for functionality of some classes
    def test_component_dict(self):
        v = Component(15, 25)
        assert v.values == {"value": 15, "scale": 25}
        assert v.comp_at_rank(4) == 115
        assert Damage_Heal("Physical", v.values).values == {"kind": "Physical", "base": v.values, "ad_%": {}, "ap_%": {}, "hp_%": {}}

    