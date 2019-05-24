# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 15:37:47 2019

@author: Daniel Bresnahan
"""

class Modifier:
    
    def __init__(self, Coordinates):
        
        self.Coordinates = Coordinates
        
    def getCoordinates(self):
        
        return self.Coordinates
    
class AmmoDump(Modifier):
    
    def __init__(self, Coordinates):
        super().__init__(Coordinates)
        
class City(Modifier):
    
    def __init__(self, Coordinates):
        super().__init__(Coordinates)
        
class Road(Modifier):
    
    def __init__(self, Coordinates):
        super().__init__(Coordinates)
        
class VictoryPoint(Modifier):
    
    def __init__(self, Coordinates):
        super().__init__(Coordinates)
    