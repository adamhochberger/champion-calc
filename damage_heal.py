#!/usr/local/bin/env python

class damage_heal:
    'Damage/heal object for the ability container'

    def __init__ (self, base, ad_percent, ap_percent, hp_percent):
        self.base = base
        self.ad_percent = ad_percent
        self.ap_percent = ap_percent
        self.hp_percent = hp_percent
