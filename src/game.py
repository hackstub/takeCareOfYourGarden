import sys
import shared as s

import pygame
from pygame.locals import *

class Game() :

    def __init__(self) :

        # Initialize PyGame
        pygame.init()

        # Set dimensions
        self.width, self.height = (960, 735)

        self.screen = pygame.display.set_mode( (self.width, self.height), 0, 32)
        pygame.display.set_caption("Anata no niwa o sewa shite kudasai")

        # Set up FPS clock
        self.fps = 30
        self.fpsClock = pygame.time.Clock()
        
        
        
    
    def mainLoop(self) :
        
        # Handle events
        self.eventHandler()
        
        # Handle keys
        self.keysHandler()

        # Update stuff
        s.interface.update()
        s.character.update()
        for flower in s.flowers :
            flower.update()

        # Render stuff
        self.screen.blit(s.imagedb["bg"], (0,0))
        for flower in s.flowers :
            flower.render()
        s.character.render()
        s.interface.render()
            
        # Update screen
        pygame.display.update()
        self.fpsClock.tick(self.fps)
 
    def eventHandler(self) :

        for event in pygame.event.get():

            if (event.type == pygame.QUIT) :
                pygame.quit()
                sys.exit()
            
            if (event.type == pygame.KEYDOWN) :
                if (event.key == pygame.K_e) :
                    s.character.water()
                if (event.key == pygame.K_f) :
                    s.character.cut()


    def keysHandler(self) :
        
        keyPressed = pygame.key.get_pressed()

        moveDirection = 0
        if (keyPressed[pygame.K_LEFT])  : moveDirection = -1
        if (keyPressed[pygame.K_RIGHT]) : moveDirection = +1

        if (moveDirection != 0) :
            s.character.move(moveDirection)




