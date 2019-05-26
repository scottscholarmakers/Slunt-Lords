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
    
    def __init__(self, displayWidth, displayHeight, ThisBoard="TestGram.txt"):
        
        self.displayWidth = displayWidth
        self.displayHeight = displayHeight
        
        self.gameDisplay = pygame.display.set_mode((self.displayWidth, self.displayHeight))
        pygame.display.set_caption('S L U N T')
        
        self.crashed = False
        
        self.GameBoard = Board()
        
        self.GameBoard.LoadMap(ThisBoard)
        
        self.GameBoard.generateBoard()
        
        self.BoardMap = self.GameBoard.getBoard()
        
        
        self.origin = ((self.displayWidth/2)- (max([Hex.q for Hex in self.BoardMap])/2) * self.BoardMap[0].width,
                       (self.displayHeight/2) - (max([Hex.r for Hex in self.BoardMap])/2) * self.BoardMap[0].height 
                        )
        
        self.HexSize = self.GameBoard.getHexSize()
        
        
    
    def gameLoop(self):
        
        self.gameDisplay.fill(self.white)
        for Tile in self.BoardMap:
            pygame.draw.polygon(self.gameDisplay, self.black, Tile.hexagon_to_Pixel(self.origin), 3)
                
        while not self.crashed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.crashed = True

        
            pygame.display.update()
            self.clock.tick(60)
            
        pygame.quit()

            