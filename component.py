#!/usr/local/bin/env python
class Component:
    '''Base class for the parts of an item or ability
        
        Uses base dict structure to replicate pieces of an ability that are combined in the damage_heal class
        
        TODO: Further test print_comp_at_rank()
    '''

    def __init__(self, value_array):
      self.values = {"value": value_array}

    def print_comp(self):
        print(self.values["value"], end=' ')

    def comp_at_rank(self, rank):
        return (self.values["value"][rank-1])
        
      