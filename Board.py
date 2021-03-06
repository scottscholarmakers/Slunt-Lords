# -*- coding: utf-8 -*-
"""
Created on Fri May 24 20:09:07 2019

@author: Daniel
"""

import math
from boardPieces.Hexagon import Hexagon, Valley, Water, Forest, Chasm, Hill
import os
import csv

class Board:
    
    def __init__(self):
        
        self.Directory = os.getcwd()
        self.Map = []
        self.HexSize = 0
        self.gameBoard = []
        
        
    """
    returns board for drawing
    and hexSize
    """
    def getBoard(self):
        return self.gameBoard
    
    def getHexSize(self):
        return self.HexSize
    
    """
    Function used to create basic parallelogram maps, of differing sizes
    orientation 1 = Top left
    orientation 2 = Middle
    orientation 3 = Top Right
    
    returns 
    """
    
    def createParallelograms(self, orientation, start, end, NewSize):
        
        ReturnMap = []
        
        if orientation == 1:
            
            for q in range(start, end):
                
                for r in range(start, end):
                    
                    ReturnMap.append(Hexagon(q, r, -q-r, NewSize))
                    
                    
        return ReturnMap

        
    
    def generateBoard(self):
        
        for Tile in self.Map:
            
            if Tile[2] == "Valley":
                self.gameBoard.append(Valley(Tile[0], Tile[1], Hexagon.axialToCube(Tile[0], Tile[1]), self.HexSize))
                
            elif Tile[2] == "Water":
                self.gameBoard.append(Water(Tile[0], Tile[1], Hexagon.axialToCube(Tile[0], Tile[1]), self.HexSize))
                
            elif Tile[2] == "Forest":
                self.gameBoard.append(Forest(Tile[0], Tile[1], Hexagon.axialToCube(Tile[0], Tile[1]), self.HexSize))
                
            elif Tile[2] == "Chasm":
                self.gameBoard.append(Chasm(Tile[0], Tile[1], Hexagon.axialToCube(Tile[0], Tile[1]), self.HexSize))
                
            elif Tile[2] == "Hill":
                self.gameBoard.append(Hill(Tile[0], Tile[1], Hexagon.axialToCube(Tile[0], Tile[1]), self.HexSize))
                
            else:
                self.gameBoard.append(Hexagon(Tile[0], Tile[1], Hexagon.axialToCube(Tile[0], Tile[1]), self.HexSize))
    
    
    def LoadMap(self, MapName):
        
        self.Map = []
        
        with open(self.Directory + "\\Maps" + "\\" + MapName, 'r') as File:
            
            csv_reader = csv.reader(File, delimiter=',')
            
            for index, row in enumerate(csv_reader):
                
                print(row)
                
                if row:
                
                    if index == 0:
                        self.HexSize = int(row[0])
                    
                    else:
                        self.Map.append((int(row[0]), int(row[1]), row[2]))
                    
                
        
    def saveMap(self, Map, MapName):
        
        with open(self.Directory + "\Maps" + "\\" + MapName + ".txt", 'w') as File:
            csv_writer = csv.writer(File, delimiter=',')
            
            for index, row in enumerate(Map):
                if index == 0:
                    rowList = [row.Size]
                    
                else:
                    rowList = [row.q, row.r, row.getType()]
                    
                csv_writer.writerow(rowList)