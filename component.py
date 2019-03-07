#!/usr/local/bin/env python
class Component:
    '''Base class for the parts of an item or ability
        
        Uses base dict structure to replicate pieces of an ability that are combined in the damage_heal class
        
        TODO: Further test comp_at_rank()
    '''

    def __init__(self, value_array=[0, 0, 0, 0, 0]):
      self.scaling = {"value": value_array}

    def print_comp(self):
        for value in self.scaling["value"]:
            print(value, end=' ')

        
      