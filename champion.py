from unit import Unit

class Champion(Unit):
    def __init__(self, name, attributes):
        attr_names = ["hp", "mp", "movespeed", "armor", "spellblock", "attackrange", "hpregen", "mpregen", "crit", "attackdamage", "attackspeed"]
        self.name = name
        for stat in attr_names:
            if stat is "movespeed" or stat is "attackrange":
                self.attributes[stat] = (attributes[stat], 0)
            else:
                self.attributes[stat] = (attributes[stat], attributes[stat + "perlevel"])

    def print_info(self):
        print(self.name)
        print(self.attributes)      

    def get_attr_at_level(self, attr: str, level: int) -> float:
        value = self.attributes[attr]
        return value[0] + value[1] * level
