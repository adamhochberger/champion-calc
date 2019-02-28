#!/usr/local/bin/env python
class Component:
    'Base class for the parts of an item or ability'

    def __init__(self, kind, value, scaling_value):
      self.kind = kind
      self.value = value
      self.scaling_value = scaling_value

    """
    For Ezreal Q: Mystic Shot
    At max it would have
    Cost (mana, 28, 3)
    Cooldown (cooldown, 5.5, -0.25)
    Damage
        Flat (dmg_flat, 15, 25)
        AD % (ad_percent, 110, 0)
        AP % (ap_percent, 30, 0)

    For Ezreal W: Essence Flux
    Cost
    Cooldown
    Damage
        Flat (dmg_flat, 80, 55)
        AD % (bonus_ad_percent, 60, 0)
        AP % (ap_percent, 70, 5)
    """
      