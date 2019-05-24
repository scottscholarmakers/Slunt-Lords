# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 19:42:50 2019

@author: Daniel Bresnahan
"""
import math
from boardPieces.Hexagon import Hexagon, Valley, Water, Forest, Chasm, Hill
import random

class Board:
    
    def __init__(self, rows, width, height, size):
        self.width = width
        self.height = height
        self.rows = rows
        self.hexSize = size
        self.gameBoard = self.createBoard(self.hexSize, self.rows)
        
    def getBoard(self):
        return self.gameBoard
        
        
    def hexCoords(self, center, size, i):
        angle_deg = 60 * i - 30
        angle_rad = round(math.pi / 180 * angle_deg, 2)
        return (round(center[0] + size * math.cos(angle_rad), 2),
                 round(center[1] + size * math.sin(angle_rad), 2))
    
    """
    Hexline is the module used to generate lines of Hexagons of n length 
    TODO: Change the system for choosing the tile type to be manual and not Random
    """
    
    def HexLine(self, n, size, Start):
    
        HexLine = []
    
        for i in range(n):
            
            rand = random.randint(0, 100)
            
            if rand < 40:
                HexLine.append(Hexagon([self.hexCoords(Start, size, c) for c in range(6)], Start, size))
            
            elif rand >= 40 and rand < 60:
                HexLine.append(Chasm([self.hexCoords(Start, size, c) for c in range(6)], Start, size))
                    
            elif rand >= 60 and rand < 70:
                HexLine.append(Water([self.hexCoords(Start, size, c) for c in range(6)], Start, size))
        
            elif rand >= 70 and rand < 80:
                HexLine.append(Valley([self.hexCoords(Start, size, c) for c in range(6)], Start, size))
            
            elif rand >= 80 and rand < 90:
                HexLine.append(Hill([self.hexCoords(Start, size, c) for c in range(6)], Start, size))
            elif rand >= 90:
                HexLine.append(Forest([self.hexCoords(Start, size, c) for c in range(6)], Start, size))
                
                
            #HexLine.append(Hexagon([self.hexCoords(Start, size, c) for c in range(6)], Start, size))
        
            Start = (Start[0] + size * math.sqrt(3), Start[1])
        
#        print("HexLine Method")
#        print(HexLine)
#        print("~~~~~~ \n")
        return(HexLine)
        
    def createBoard(self, hexSize, numRows):
        
        """
        TODO: Make this part more efficient 
        """
    
        #Finds the x Coordinate of the left-most hex in middle row
        startX = (self.width / 2) - ((math.floor(numRows/ 2)) * (hexSize * math.sqrt(3)))
        #Sets start to the coordinates of left-most hex in middle row
        Start = (startX, self.height / 2)

        HexBoard = []
    
        midPoint = int(math.floor(numRows / 2) + 1)
        NHex = midPoint
    
        #transitions start coordinate to that of the left-most in top row
        for i in range (midPoint , 1, -1):
            Start = (Start[0] + (hexSize * math.sqrt(3))/2, Start[1] - (hexSize * 2) * 3/4)
        
    
#        print("numRows \n" + str(numRows) + "\n~~~~~\n")
        
        for i in range(1, numRows + 1):
            
#            print("Generate Loop\n" + str(i) + "\n~~~\n")
    
        
            if i < midPoint:
            
                HexBoard.append(self.HexLine(NHex, hexSize, Start=Start))
                NHex += 1
            
                Start = (Start[0] - (hexSize * math.sqrt(3))/2, Start[1] + (hexSize * 2)* 3/4)
            
            else:
            
                HexBoard.append(self.HexLine(NHex, hexSize, Start=Start))
                NHex -= 1
            
                Start = (Start[0] + (hexSize * math.sqrt(3))/2, Start[1] + (hexSize * 2) * 3/4)
            
        return HexBoard