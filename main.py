import sys

import pygame
from pygame.locals import *

import src.interface as I
import src.character as C
import src.shared as S
import src.game as G

def main() :
    
    S.game = G.Game()

    # Load images...
    S.loadImages()

    # Init character
    S.character = C.Character(0)

    # Init interface
    S.interface = I.Interface()
    
    # Init title
    S.game.initTitleScreen()
   
   # Loop
    while True :
        S.game.mainLoop()

main()
