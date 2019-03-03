#!/usr/local/bin/env python

class Damage_Heal:
    '''
    Damage/heal object for the ability container
    Has components for base damage, ad%, ap%, hp%
    This object simplifies the initialization process as more dictionaries are added together to represent an ability
    TODO: Re-implement print_comp_at_rank()
    '''

    # Init that takes in at minimum what kind of values it is processing (damage, healing, possible buffs) and then other indicators of damage
    # All variables other than kind are Component variables and represent a dictionary of information
    def __init__ (self, kind, base={}, ad_percent={}, ap_percent={}, hp_percent={}):
        self.values = {"kind": kind, "base": base, "ad_%": ad_percent, "ap_%": ap_percent, "hp_%": hp_percent}

    # Print debug statement to ensure that values are expected (can be used with assert later)
    def print_comp(self):
        print(str(self.values))
    
    # Secondary print that represents values of container at a rank (uses flat_value + scale * rank)
    def print_comp_at_rank(self, rank):
        for item in self.values:
            print(item, end=' ')
            print(item.value)

class Buff_Debuff:
    '''Buff/debuff object for the ability container
        This object may be represented by damage_heal in the future and a better name would represent all of them
        TODO: Finish implementation of damage_heal object and replicate or extend functionality to buff_debuff
    '''

    def __init__ (self, kind, flat, percent):
        self.kind = kind
        self.flat = flat
        self.percent = percent
    
    def print_comp(self, comp_list):
        for item in comp_list:
            item.print_comp()


class Flat:
    '''Flat object for the object container
        May be outdated because the component class uses a more representative dict structure
        TODO: Clean up code if necessary
    '''

    def __init__ (self, base, scale):
        self.base = base
        self.scale = scale

class Percent:
    '''Percent object for containers
        May be outdated because the component class uses a more representative dict structure
        TODO: Clean up code if necessary
    '''

    def __init__ (self, kind, base, scale):
        self.kind = kind
        self.base = base
        self.scale = scale
