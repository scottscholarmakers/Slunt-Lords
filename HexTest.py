# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 16:33:44 2019

@author: Daniel Bresnahan
"""
import math
import pygame
import random


pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('S L U N T')

black = (0,0,0)
white = (255,255,255)
green = (0, 255, 0)

clock = pygame.time.Clock()
crashed = False


def pointy_hex_corner(center, size, i):
    angle_deg = 60 * i - 30
    angle_rad = round(math.pi / 180 * angle_deg, 2)
    return (round(center[0] + size * math.cos(angle_rad), 2),
                 round(center[1] + size * math.sin(angle_rad), 2))
    

def HexLine(n, size, Start=(display_width/2, display_height/2)):
    
    HexLine = []
    
    for i in range(n):
        
        HexLine.append([pointy_hex_corner(Start, size, c) for c in range(6)])
        
        Start = (Start[0] + size * math.sqrt(3), Start[1])
        
        
    return(HexLine)
    
def createBoard(hexSize, numRows):
    
    #Finds the x Coordinate of the left-most hex in middle row
    startX = (display_width / 2) - ((math.floor(numRows/ 2)) * (hexSize * math.sqrt(3)))
    #Sets start to the coordinates of left-most hex in middle row
    Start = (startX, display_height / 2)

    HexBoard = []
    
    midPoint = int(math.floor(numRows / 2) + 1)
    NHex = midPoint
    
    #transitions start coordinate to that of the left-most in top row
    for i in range (midPoint , 1, -1):
        Start = (Start[0] + (hexSize * math.sqrt(3))/2, Start[1] - (hexSize * 2) * 3/4)
        
    
    
    for i in range(1, numRows + 1):
        

        
        if i < midPoint:
            
            HexBoard.append(HexLine(NHex, hexSize, Start=Start))
            NHex += 1
            
            Start = (Start[0] - (hexSize * math.sqrt(3))/2, Start[1] + (hexSize * 2)* 3/4)
            
        else:
            
            HexBoard.append(HexLine(NHex, hexSize, Start=Start))
            NHex -= 1
            
            Start = (Start[0] + (hexSize * math.sqrt(3))/2, Start[1] + (hexSize * 2) * 3/4)
            
    return HexBoard
            
            
            

        
TestBoard = createBoard(20, 17)


gameDisplay.fill(white)

for row in TestBoard:
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
