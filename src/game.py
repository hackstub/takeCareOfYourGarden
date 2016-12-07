import sys
import src.shared as s

import pygame
from pygame.locals import *

import src.flowers as F

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
   
    def initTitleScreen(self) :

        s.mode = "title"

        # Init flowers
        s.flowers = []
        for i in range(s.numberOfFlowers) :
            s.flowers.append(F.Flower(i))
            s.flowers[i].height = 4
            if (i == 0) :
                s.flowers[i].evolve("good")
                s.flowers[i].nextStepCooldown = 100000
                s.flowers[i].enabled = True
            elif (i == 3):
                s.flowers[i].evolve("evil")
                s.flowers[i].nextStepCooldown = 100000
                s.flowers[i].enabled = True

        s.character.position = 2

    def gameover(self) :
       
        s.interface.initGameover()

        s.mode = "gameover"
        for flower in s.flowers :
            flower.enabled = False

        s.speedFactor = 1.0
     
    def start(self) :
        
        s.mode = "game"
        # Init flowers
        s.flowers = []
        for i in range(s.numberOfFlowers) :
            s.flowers.append(F.Flower(i))
        
        s.character.position = 2
        s.character.score = 0
        s.character.lives = 3
        s.character.combo = 0
        
        s.speedFactor = 1.0

    def mainLoop(self) :
        
        # Handle events
        self.eventHandler()
        
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
                if (event.key == pygame.K_d) :
                    if (s.mode == "title") : s.interface.popTutoKey("Dkey")
                    s.character.water()
                if (event.key == pygame.K_f) :
                    if (s.mode == "title") : s.interface.popTutoKey("Fkey")
                    s.character.cut()

                if (event.key == pygame.K_RETURN) and (s.mode == "gameover"):
                    self.start()
                    return

                moveDirection = 0
                if (event.key == pygame.K_LEFT)   : 
                    if (s.mode == "title") : s.interface.popTutoKey("leftkey")
                    moveDirection = -1
                if (event.key == pygame.K_RIGHT)  : 
                    if (s.mode == "title") : s.interface.popTutoKey("rightkey")
                    moveDirection = +1

                if (moveDirection != 0) :
                    s.character.move(moveDirection)




