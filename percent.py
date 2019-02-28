#!/usr/local/bin/env python
class Percent:
    'Percent object for containers'

    def __init__ (self, kind, default, scale):
        self.kind = kind
        self.default = default
        self.scale = scale
