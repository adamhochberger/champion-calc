#!/usr/local/bin/env python
class Ability:
    'Base class for the ability container'

    def __init__(self, name, description, component_list):
      self.name = name
      self.description = description
      self.component_list = component_list

    """
    Using example
    For Ezreal Q: Mystic Shot
    At max it would have
    Cost (mana, 28, 3)
    Cooldown (cooldown, 5.5, -0.25)
    Damage
        Flat (dmg_flat, 15, 25)
        AD % (ad_percent, 110, 0)
        AP % (ap_percent, 30, 0)

    Ability("Mystic Shot", "filler text", [Cost, Cooldown, Damage]
    For Ezreal W: Essence Flux
    Cost
    Cooldown
    Damage
        Flat (dmg_flat, 80, 55)
        AD % (bonus_ad_percent, 60, 0)
        AP % (ap_percent, 70, 5)
    """
      
