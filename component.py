#!/usr/local/bin/env python
class Component:
    '''Base class for the parts of an item or ability
        Uses base dict structure to replicate pieces of an ability that are combined in the damage_heal class
        TODO: Further test print_comp_at_rank()
    '''

    def __init__(self, value, scaling_value):
      self.values = {"value": value, "scale": scaling_value}

    def print_comp(self):
        print(self.values["value"], end=' ')
        print(self.values["scaling_value"])

    def print_comp_at_rank(self, rank):
        print(self.values["value"] + rank*self.values["scaling_value"])
        
      