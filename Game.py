# -*- coding: utf-8 -*-
"""
Created on Sat May 25 11:24:38 2019

@author: Daniel
"""

import pygame
from Board import Board
from boardPieces.Hexagon import Hexagon


class Game:
    
    pygame.init()
    
    black = (0,0,0)
    white = (255,255,255)
    green = (0, 255, 0)
    
    clock = pygame.time.Clock()
    
    def __init__(self, displayWidth, displayHeight, defaultBoard="Basic-Triangle.txt"):
        
        self.displayWidth = displayWidth
        self.displayHeight = displayHeight
        
        self.gameDisplay = pygame.display.set_mode((self.displayWidth, self.displayHeight))
        pygame.display.set_caption('S L U N T')
        
        self.crashed = False
        
        self.GameBoard = Board()
        
        self.GameBoard.LoadMap(defaultBoard)
        
        self.GameBoard.generateBoard()
        
        self.HexSize = self.GameBoard.getHexSize()
        
        
    
    def gameLoop(self):
        
        self.gameDisplay.fill(self.white)
        for Tile in self.GameBoard.getBoard():
            pygame.draw.polygon(self.gameDisplay, self.black, Tile.hexagon_to_Pixel(), 3)
                
        while not self.crashed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.crashed = True

        
            pygame.display.update()
            self.clock.tick(60)
            
        pygame.quit()

            
        
    


