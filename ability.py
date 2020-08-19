#!/usr/local/bin python
import json

class Ability:
    'Endpoint for API will be here: http://cdn.merakianalytics.com/riot/lol/resources/{PATCH}/en-US/champions/{CHAMPION.json'
    'Base class for the ability container'
    ''' Structure for ability is of this form (subject to change based on components)
        name: str
        description: str
        image: img

        effects - dictionary with arrays of minimum, maximum damage, health modifiers, damage types, etc
    
    '''
    def __init__(self):
        print()
