from component import Component
from values import Damage_Heal
import pytest

class Test_TestComponentInit:

    # Initializer with preset values, returns dictionary
    def default_component(self):
        return Component(15, 25).values

    # Initializer with user-set values, returns dictionary
    def start_component(self, base, scale):
        return Component(base, scale).values

    # Initializer for advanced component with arg for base component, returns dictionary
    def start_adv_component(self, comp):
        return Damage_Heal("Physical", comp).values

    # Overall testing for functionality of some classes
    # Test is supposed to fail for "Magical"

    def test_component_dict(self):
        v = self.default_component()
        assert v == {"value": 15, "scale": 25}
        assert self.start_adv_component(v) == {"kind": "Physical", "base": v, "ad_%": {}, "ap_%": {}, "hp_%": {}}
        assert self.start_adv_component(v) == {"kind": "Magical", "base": v, "ad_%": {}, "ap_%": {}, "hp_%": {}}

    