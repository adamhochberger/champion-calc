from component import Component
from values import Damage_Heal, Buff_Debuff
from ability import Ability

def main():
    '''
     Main Test function that will be used to debug (reduce clutter in ability since that will be a smaller scope)
    '''

    cost = Component(28, 3).values
    cd = Component(5.5, -0.25).values
    base_dmg = Component(15, 25).values
    ad = Component(110, 0).values
    ap = Component(30, 0).values

    dmg = Damage_Heal("Physical", base_dmg, ad, ap).values
    a1 = Ability("Mystic Shot", "filler", 1, 5, {"cost": cost, "cd": cd, "dmg": dmg})
    a1.print_ability()

if __name__== "__main__":
    main()