#!/usr/local/bin/env python

class damage_heal:
    'Damage/heal object for the ability container'

    def __init__ (self, base, ad_percent, ap_percent, hp_percent):
        self.base = base
        self.ad_percent = ad_percent
        self.ap_percent = ap_percent
        self.hp_percent = hp_percent

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
