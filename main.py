import sys

import pygame
from pygame.locals import *

import interface as I
import character as C
import flowers as F
import shared as S
import game as G

def main() :
    
    S.game = G.Game()

    # Load images...
    S.loadImages()

    # Init flowers
    S.flowers = []
    for i in range(S.numberOfFlowers) :
        S.flowers.append(F.Flower(i))

    # Init character
    S.character = C.Character(0)

    # Init interface
    S.interface = I.Interface()

    # Loop
    while True :
        S.game.mainLoop()

main()

