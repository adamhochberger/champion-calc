class Unit:
    '''
        Base class that all minions, monsters, champions are based from
        Contains an attribute member with tuples based on (stat, stat per level)
    '''

    attributes = {
        "hp": (0,0),
        "mp": (0,0),
        "movespeed": (0,0), 
        "armor": (0,0),
        "spellblock": (0,0),
        "attackrange": (0,0),
        "hpregen": (0,0),
        "mpregen": (0,0),
        "crit": (0,0),
        "attackdamage": (0,0),
        "attackspeed": (0,0)
    }


