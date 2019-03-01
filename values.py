#!/usr/local/bin/env python

class Damage_Heal:
    '''
    Damage/heal object for the ability container
    Has components for base damage, ad%, ap%, hp%
    '''

    def __init__ (self, kind, base={}, ad_percent={}, ap_percent={}, hp_percent={}):
        self.values = {"kind": kind, "base": base, "ad_%": ad_percent, "ap_%": ap_percent, "hp_%": hp_percent}

    def print_comp(self):
        print(str(self.values))
    
    def print_comp_at_rank(self, rank):
        for item in self.values:
            print(item, end=' ')
            print(item.value)

class Buff_Debuff:
    'Buff/debuff object for the ability container'

    def __init__ (self, kind, flat, percent):
        self.kind = kind
        self.flat = flat
        self.percent = percent
    
    def print_comp(self, comp_list):
        for item in comp_list:
            item.print_comp()

class Flat:
    'Flat object for the object container'

    def __init__ (self, base, scale):
        self.base = base
        self.scale = scale

class Percent:
    'Percent object for containers'

    def __init__ (self, kind, base, scale):
        self.kind = kind
        self.base = base
        self.scale = scale
