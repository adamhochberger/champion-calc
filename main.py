from component import Component
from values import Damage_Heal, Buff_Debuff
from ability import Ability

def main():
    '''
     Main Test function that will be used to debug (reduce clutter in ability since that will be a smaller scope)
    '''

    cost = Component([28, 31, 34, 37, 40]).scaling
    cd = Component([5.5, 5.25, 5.0, 4.75, 4.5]).scaling
    base_dmg = Component([15, 40, 65, 90, 115]).scaling
    ad = Component([110, 110, 110, 110, 110]).scaling
    ap = Component([30, 30, 30, 30, 30]).scaling

    dmg = Damage_Heal("Physical", base_dmg, ad, ap)
    a1 = Ability("Mystic Shot", "filler", 1, 5, {"cost": cost, "cd": cd, "dmg": dmg.scaling})
    dmg.print_comp_at_rank(5)
    a1.print_ability()

if __name__== "__main__":
    main()