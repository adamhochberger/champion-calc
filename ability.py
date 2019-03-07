#!/usr/local/bin python
import json

class Ability:
    'Base class for the ability container'
    ''' Structure for ability is of this form (subject to change based on components)
    {
        "name": "Mystic Shot",
        "description": "filler",
        "rank": 1,
        "max_rank": 5,
        "components": {
        "cost": {
            "value": [28, 31, 34, 37, 40]
        },
        "cd": {
            "value": [5.5, 5.25, 5.0, 4.75, 4.5]
        },
        "dmg": {
            "kind": "Physical",
            "base": {
                "value": [15, 40, 65, 90, 115]
            },
            "ad_%": {
                "value": [110, 110, 110, 110, 110]
            },
            "ap_%": {
                "value": [30, 30, 30, 30, 30]
            },
            "hp_%": {}
        }
    }
}

    
    '''
    def __init__(self, name, description, rank, max_rank, components):
        self.values = {"name": name, "description": description, "rank": rank, "max_rank": max_rank, "components": components}
    


    def print_ability(self):
        print(json.dumps(self.values, sort_keys=False, indent=4))
    
    '''
    def print_at_rank(self, value):
        if value > 0 and value < self.max_rank:
            for item in self.components:
                item.print_comp_at_rank()     
                '''     

    """
    Using example
    For Ezreal Q: Mystic Shot
    At max it would have
    Cost (mana, 28, 3)
    Cooldown (cooldown, 5.5, -0.25)
    Damage (base_dmg, ad_%, ap_%)
        base_dmg = Component(dmg_flat, 15, 25)
        ad_% = Component(ad_percent, 110, 0)
        ap_% = Component(ap_percent, 30, 0)

    Ability("Mystic Shot", "filler text", [Cost, Cooldown, Damage]
    """
      
