import pygame
from pygame.locals import *


#debug = False
debug = True
numberOfFlowers = 4
flowersSeparation = 210
characterBaseX = 67
characterBaseY = 550
flowersBaseX = 167
flowersBaseY = 530

imagedb = { }

def loadImages() :

    # Background
    bg      = pygame.image.load("assets/bg.png")
    imagedb["bg"] = bg

    # Life indicator
    life = pygame.image.load("assets/heart.png")
    imagedb["life"] = life
    
    # Stems
    stems =  pygame.image.load("assets/stems.png")
    imagedb["stems"] = [[],[]]
    for i in range(4) :
        imagedb["stems"][0].append(getSprite(stems, i, 0, 140, 54))
        imagedb["stems"][1].append(getSprite(stems, i, 1, 140, 54))

    # Flower sprites
    flowersHead = pygame.image.load("assets/flowersHead.png")
    imagedb["flowersHead"] = {}
    imagedb["flowersHead"]["neutral"] = []
    imagedb["flowersHead"]["good"] = []
    imagedb["flowersHead"]["evil"] = []
    for i in range(3) :
        imagedb["flowersHead"]["good"]   .append(getSprite(flowersHead, i, 0, 175, 175))
        imagedb["flowersHead"]["evil"]   .append(getSprite(flowersHead, i, 1, 175, 175))
        imagedb["flowersHead"]["neutral"].append(getSprite(flowersHead, i, 2, 175, 175))

    imagedb["flowersHead-good-dead"] = getSprite(flowersHead, 3, 0, 175, 175)
    imagedb["flowersHead-evil-dead"] = getSprite(flowersHead, 3, 1, 175, 175)

    flowersPop = pygame.image.load("assets/flowersPop.png")
    imagedb["flowersPop"] = {}
    imagedb["flowersPop"]["good"] = []
    imagedb["flowersPop"]["evil"] = []
    for i in range(4) :
        imagedb["flowersPop"]["good"].append(getSprite(flowersPop, i, 0, 250, 250))
        imagedb["flowersPop"]["evil"].append(getSprite(flowersPop, i, 1, 250, 250))

    # Character sprites
    char = pygame.image.load("assets/perso.png")
    imagedb["char"] = {}
    imagedb["char"]["standing"] = getSprite(char, 0, 0, 48, 64)
    imagedb["char"]["left"]  = []
    imagedb["char"]["right"] = []
    
    for i in range(4) :
        imagedb["char"]["left"].append(getSprite(char, i, 1, 48, 64))
        imagedb["char"]["right"].append(getSprite(char, i, 2, 48, 64))

    # Watering animation
    watering = pygame.image.load("assets/watering.png")
    imagedb["watering"] = []
    
    for i in range(3) :
        print(i)
        imagedb["watering"].append(getSprite(watering, i, 0, 64, 64))

    # Combo icon
    imagedb["comboicon"] = pygame.image.load("assets/flowericon.png")

    print(imagedb)

def getSprite(img, x, y, w=32, h=32) :

    return img.subsurface((x*w, y*h, w, h))


