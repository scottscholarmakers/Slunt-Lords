# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 19:37:10 2019

@author: Daniel Bresnahan
"""

class Hexagon:
    
    def __init__(self, Points, Center, Size):
        self.Coords = Points
        self.Center = Center
        self.Size = Size
        self.sprite = (255, 0, 10)
        
    def addPoints(self, pointsToAdd):
        self.Coords = pointsToAdd
        
        
    def getCoords(self):
        return self.Coords
    
    def getSprite(self):
        return self.sprite
    

class Chasm(Hexagon):
    
    def __init__(self, Points, Center, Size):
        super().__init__(Points, Center, Size)
        self.sprite = (0, 0, 0)
        
class Forest(Hexagon):
    
    def __init__(self, Points, Center, Size):
        super().__init__(Points, Center, Size)
        self.sprite = (41, 137, 71)
        
class Hill(Hexagon):
    
    def __init__(self, Points, Center, Size):
        super().__init__(Points, Center, Size)
        self.sprite = (0, 255, 80)
        
class Valley(Hexagon):
    
    def __init__(self, Points, Center, Size):
        super().__init__(Points, Center, Size)
        self.sprite = (130, 55, 58)
        
class Water(Hexagon):
    
    def __init__(self, Points, Center, Size):
        super().__init__(Points, Center, Size)
        self.sprite = (104, 117, 255)

    

    
    
        