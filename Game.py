# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 20:11:03 2019

@author: Daniel Bresnahan
"""

import pygame
from Board import Board
from boardPieces import Hexagon
import random

class Game:
    
    pygame.init()
    
    black = (0,0,0)
    white = (255,255,255)
    green = (0, 255, 0)
    
    clock = pygame.time.Clock()
    
    def __init__(self, displayWidth, displayHeight, rows, width, height, size):
        
        self.displayWidth = displayWidth
        self.displayHeight = displayHeight
        
        self.gameDisplay = pygame.display.set_mode((self.displayWidth, self.displayHeight))
        pygame.display.set_caption('S L U N T')
        
        self.crashed = False
        
        self.rows = rows
        self.width = width
        self.height = height
        self.size = size
        
        self.board = Board(self.rows, self.width, self.height, self.size)
    
    def gameLoop(self):
        
        self.gameDisplay.fill(self.white)
        for row in self.board.getBoard():
            for i in row:
                pygame.draw.polygon(self. gameDisplay, i.getSprite(), i.getCoords(), 3)
                
        while not self.crashed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.crashed = True

        
            pygame.display.update()
            self.clock.tick(60)
            
        pygame.quit()

            
        
    



"""
for row in TestBoard:
    print(row)
    print("\n")
    for i in row:
        pygame.draw.polygon(gameDisplay, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), i)

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
"""
