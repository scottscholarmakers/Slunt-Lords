# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 10:41:38 2019

@author: Daniel Bresnahan
"""

import pygame
from Game import Game

class MainMenu:
    
    pygame.init()
    clock = pygame.time.Clock()
    
    button_width = 100
    button_height = 30
    white = (255, 255, 255)
    black = (0, 0, 0)
    gray = (104, 103, 103)
    
    def text_objects(self, text, font):
        textSurface = font.render(text, True, self.black)
        return textSurface, textSurface.get_rect()
    
    def button(self, msg,x,y,w,h,screen, button, action=None):
        
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        if (x - (w / 2)) < mouse[0] < (x + (w / 2)) and y < mouse[1] < (y + h):
            pygame.draw.rect(screen, self.gray, button)
            
            if click[0] == 1 and action != None:
                startGame = Game(800, 600)
                startGame.gameLoop()
                pygame.quit()
        else:
            pygame.draw.rect(screen, self.black, button, 3)
            
        buttonTextStyle = pygame.font.Font("SLUNTFONT.TTF", 12)
        buttonTextSurface, buttonTextRect = self.text_objects(msg, buttonTextStyle)
        buttonTextRect.center = (x, (y + (h / 2)))
        screen.blit(buttonTextSurface, buttonTextRect)
        

    def __init__(self, display_width, display_height):
        
        self.display_width = display_width
        self.display_height = display_height
        self.screen = pygame.display.set_mode((display_width, display_height))
        pygame.display.set_caption("S L U N T")
        
        self.intro = True
        
    def gameLoop(self):
        while self.intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.intro = False
                    
            self.screen.fill(self.white)
        
            self.titleStyle = pygame.font.Font("SLUNTFONT.TTF", 50)
            self.titleTextSurface, self.titleTextRect = self.text_objects("SLUNT LORDS", self.titleStyle)
            self.titleTextRect.center = ((self.display_width / 2), (self.display_height / 4))
            
            
            self.startButton = pygame.Rect(((self.display_width/2) - (self.button_width / 2)), (self.display_height/4) * 3, self.button_width, self.button_height)
            
            self.screen.blit(self.titleTextSurface, self.titleTextRect)
            
            
            self.button("Start", self.display_width/2, ((self.display_height / 4) * 3), self.button_width, self.button_height, self.screen, self.startButton, "start_game")
            
            
            pygame.display.update()
            self.clock.tick(60)
        pygame.quit()
        quit()

            

