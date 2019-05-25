# -*- coding: utf-8 -*-
"""
Created on Wed May 22 17:42:51 2019

@author: Daniel

New Hexagon for optimized generation and storage
"""
from pygame import sprite
from pygame import image
import math
import os

"""
New hexagon class emphasises seperate hexagon coordinates, as apposed to 
cartesion pixel coordinates
"""

class Hexagon(sprite.Sprite):
    
    """
    When defining hexagons q, r, s are the cube coordinates of the hexagon
    """
    def __init__(self, q, r, s, Size):
        super(Hexagon, self).__init__()
        
        self.q, self.r, self.s = q, r, s
        
        #Size is the distance to the corner
        self.Size = Size
        
        SpriteNames = [os.getcwd + "/Recourses/images/Grass"]
        
        self.SpriteSet = [image.load(x) for x in SpriteNames]
        
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
    This function to generate cube coordinates from axial coordinates
    used in map generation 
    
    s = -q-r
    
    returns a tuble of coordinates
    """
    def axialToCube(q, r):
        return(q, r, -q-r)
        
        
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

    def hex_distance(self, a, b):
        return self.hex_length(self.hex_subtract(a, b))
    
    """
    This function deals with decimal coordinates
    Hexagon grid can only handle integer coordinates
    This function will transform decimal into integer by rounding
    
    However when rounding there is no quarentee that q + r + s = 0 after rounding
    
    to deal with these descripencies this algorithm finds the component with largest decimal
    and does some algebra to force it to equal what it should be to satisfy q + r + s = 0
    
    returns tuple of coordinates
    """
    
    def cube_round(hexagon):
        
        round_q = int(round(hexagon.q))
        round_r = int(round(hexagon.r))
        round_s = int(round(hexagon.s))
        
        q_diff = abs(round_q - hexagon.q)
        r_diff = abs(round_r - hexagon.r)
        s_diff = abs(round_s - hexagon.s)
        
        if q_diff > r_diff and q_diff > s_diff:
            round_q = -round_r - round_s
        else:
            if r_diff > s_diff:
                round_r = -round_q - round_s
            else:
                round_s = -round_q - round_r
        return (round_q, round_r, round_s)
    
    """
    LERP or linear interpolation 
    is a method that allows you to find some point on a line that represents a ratio
    classically this would be a line mid point calculator with a t value of 0.5
    
    used in line drawing
    """
    
    def LERP(Point1, Point2, t):
        return Point1 + (Point2 - Point1) * t
    
    """
    This utilizes the LERP function to find some point on the line between 2 hexes
    would represent a midpoint with a t value of 0.5
    
    returns a tuple of coordinates
    """
    
    def hexagon_LERP(self, Hex1, Hex2, t):
        return(self.LERP(Hex1.q, Hex2.q, t),
               self.LERP(Hex1.r, Hex2.r, t),
               self.LERP(Hex1.s, Hex2.r, t))
    
    
    
    """
    This function will actually draw the line between two hexes
    returns a list of hexes on the line
    """
    
    def hex_linedraw(self, Hex1, Hex2):
        
        N = self.hex_distance(Hex1, Hex2)
        
        results = []
        step = 1.0 / max(N, 1)
        
        for i in range(0, N + 1):
            results.append(self.hex_round(self.hexagon_LERP(Hex1, Hex2, step * i)))
        return results
    
    """
    These two functions are in charge of finding the neighbors
    """

    
    def getNeighbours(self):
        
        NeighborDirections = [(self.q + 1, self.r -1, self.s), 
                              (self.q + 1, self.r, self.s -1), 
                              (self.q, self.r + 1, self.s -1), 
                              (self.q -1, self.r + 1, self.s), 
                              (self.q -1, self.r , self.s + 1), 
                              (self.q, self.r -1, self.s + 1) ]
        
        return NeighborDirections
    
    
    def IsNeighbour(self, Hexagon):
        
        if (Hexagon.q, Hexagon.r, Hexagon.s) in self.getNeighbours:
            return True
        else:
            return False
    
    
    """
    Method for turning the map of hex coordinates into pixel coordinates
    works by defining basis vector and multiplying it be the number of hexagons. 
    
    x = 3/2 * hex.q * scalar y = sqrt(3)/2 * hex.r * scalar
    
    this method will find the pixel middle of a hexagon
    
    Returns a list of Tuples, where each tuple is a corner coordinate
    """
    
    def hexagon_to_Pixel(self, hexagon):
        
        x = self.Size * (     3/2 * hexagon.q                               )
        y = self.Size * (math.sqrt(3)/2 * hex.q  +  math.sqrt(3) * hexagon.r)
        
        cornerList = []
        
        for i in range(6):
            
            angle_deg = 60 * i - 30
            angle_rad = round(math.pi / 180 * angle_deg, 2)
            
            cornerList.append(round(x + (self.Size * math.cos(angle_rad)), 2), 
                              round(y + (self.Size * math.sin(angle_rad)), 2))
        
        return cornerList
        
    
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
        
        
class Chasm(Hexagon):
    
    def __init__(self, q, r, s, Size):
        super().__init__(q, r, s, Size)
        
        SpriteNames = [os.getcwd + "/Recourses/images/Grass"]
        
        self.SpriteSet = [image.load(x) for x in SpriteNames]
        
class Forest(Hexagon):
    
    def __init__(self, q, r, s, Size):
        super().__init__(q, r, s, Size)
        
        SpriteNames = [os.getcwd + "/Recourses/images/Grass"]
        
        self.SpriteSet = [image.load(x) for x in SpriteNames]
        
class Hill(Hexagon):
    
    def __init__(self, q, r, s, Size):
        super().__init__(q, r, s, Size)
        
        SpriteNames = [os.getcwd + "/Recourses/images/Grass"]
        
        self.SpriteSet = [image.load(x) for x in SpriteNames]
        
class Valley(Hexagon):
    
    def __init__(self, q, r, s, Size):
        super().__init__(q, r, s, Size)
        
        SpriteNames = [os.getcwd + "/Recourses/images/Grass"]
        
        self.SpriteSet = [image.load(x) for x in SpriteNames]
        
class Water(Hexagon):
    
    def __init__(self, q, r, s, Size):
        super().__init__(q, r, s, Size)
        
        SpriteNames = [os.getcwd + "/Recourses/images/Grass"]
        
        self.SpriteSet = [image.load(x) for x in SpriteNames]
        