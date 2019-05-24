# -*- coding: utf-8 -*-
"""
Created on Wed May 22 17:42:51 2019

@author: Daniel

New Hexagon for optimized generation and storage
"""
from pygame import sprite
from pygame import image

"""
New hexagon class emphasises seperate hexagon coordinates, as apposed to 
cartesion pixel coordinates
"""

class Hexagon(sprite.Sprite):
    
    """
    When defining hexagons q, r, s are the cube coordinates of the hexagon
    Sprite Set is the Set of the names of the sprites to use (Names with Path)
    """
    def __init__(self, q, r, s, Size, SpriteSet):
        super(Hexagon, self).__init__()
        
        self.q, self.r, self.s = q, r, s
        self.Size = Size
        self.SpriteSet = [image.load(x) for x in SpriteSet]
        
        self.index = 0
        self.Sprite = self.SpriteSet[self.index]
     
    """
    Call this to check cube coordinates of hexagon
    """
    def getCoords(self):
        return self.q, self.r, self.s
    
    """
    Use this to set new coords, new coords should be touple
    """
    def setCoords(self, NewCoordsTuple):
        self.q = NewCoordsTuple[0]
        self.r = NewCoordsTuple[1]
        self.s = NewCoordsTuple[2]
    
    def HexEquality(self, Hex2):
        
        if self.q == Hex2.q and self.r == Hex2.r and self.s == Hex2.s:
            return True
        
        else:
            return False
        
    """
    This set of functions represents the math that might need to be done with hex coordinates
    Simply use them like regular cube coordinate math
    returns a tuple
    """
    
    def hex_add(a, b):
        return (a.q + b.q, a.r + b.r, a.s + b.s)

    def hex_subtract(a, b):
        return (a.q - b.q, a.r - b.r, a.s - b.s)
    
    def hex_scale(a, k):
        return (a.q * k, a.r * k, a.s * k)
    
    def hex_length(hexagon):
        return (abs(hexagon.q) + abs(hexagon.r) + abs(hexagon.s)) // 2

    def hex_distance(a, b):
        return hex_length(hex_subtract(a, b))

    """
    This method is in charge of updating the current sprite
    with every update of the game
    call it inside of the game loop
    """
    def update(self):
        
        self.index += 1
        if self.index >= len(self.SpriteSet):
            self.index = 0
        
        self.Sprite = self.SpriteSet[self.index]
        