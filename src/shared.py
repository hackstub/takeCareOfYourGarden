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
        
speedFactor = 1.0

imagedb = { }

def loadImages() :

    # Background
    bg      = pygame.image.load("assets/bg.png")
    imagedb["bg"] = bg

    # Indicators
    indicators = pygame.image.load("assets/indicators.png")
    imagedb["indicator"] = {}
    imagedb["indicator"]["life"] = []
    imagedb["indicator"]["combo"] = []
    for i in range(4) :
        imagedb["indicator"]["life"].append(getSprite(indicators, i, 0, 87, 87))
        imagedb["indicator"]["combo"].append(getSprite(indicators, i, 2, 87, 87))

    # Tuto stuff
    tutostuff = pygame.image.load("assets/tuto.png")
    imagedb["tuto"] = {}
    imagedb["tuto"]["leftkey"]  = []
    imagedb["tuto"]["rightkey"] = []
    imagedb["tuto"]["Dkey"]     = []
    imagedb["tuto"]["Fkey"]     = []
    imagedb["tuto"]["poof"]     = []
    for i in range(2) :
        imagedb["tuto"]["rightkey"].append(getSprite(tutostuff, i, 0, 175, 175))
        imagedb["tuto"]["leftkey"] .append(getSprite(tutostuff, i, 1, 175, 175))
        imagedb["tuto"]["Dkey"]    .append(getSprite(tutostuff, i, 2, 175, 175))
        imagedb["tuto"]["Fkey"]    .append(getSprite(tutostuff, i, 3, 175, 175))
        imagedb["tuto"]["poof"]    .append(getSprite(tutostuff, i, 4, 175, 175))

    # Title
    title = pygame.image.load("assets/title.png")
    imagedb["title"] = []
    imagedb["title"].append(getSprite(title, 0, 0, 610, 250))
    imagedb["title"].append(getSprite(title, 0, 1, 610, 250))

    # Game over stuff
    gameover = pygame.image.load("assets/gameover.png")
    imagedb["gameoverscorebg"] = getSprite(gameover, 0, 0, 400, 250) 
    imagedb["again"]           = getSprite(gameover, 1, 0, 400, 250) 

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

    imagedb["flowersDead"] = {}
    imagedb["flowersDead"]["good"] = getSprite(flowersHead, 3, 0, 175, 175)
    imagedb["flowersDead"]["evil"] = getSprite(flowersHead, 3, 1, 175, 175)

    flowersPop = pygame.image.load("assets/flowersPop.png")
    imagedb["flowersPop"] = {}
    imagedb["flowersPop"]["good"] = []
    imagedb["flowersPop"]["evil"] = []
    for i in range(4) :
        imagedb["flowersPop"]["good"].append(getSprite(flowersPop, i, 0, 250, 250))
        imagedb["flowersPop"]["evil"].append(getSprite(flowersPop, i, 1, 250, 250))

    # Character sprites
    #char = pygame.image.load("assets/perso.png")
    #imagedb["char"] = {}
    #imagedb["char"]["standing"] = getSprite(char, 0, 0, 48, 64)
    #imagedb["char"]["left"]  = []
    #imagedb["char"]["right"] = []
    
    #for i in range(4) :
    #    imagedb["char"]["left"].append(getSprite(char, i, 1, 48, 64))
    #    imagedb["char"]["right"].append(getSprite(char, i, 2, 48, 64))

    # Cut animation
    persoActions = pygame.image.load("assets/persoActions.png")
    imagedb["actions"] = {}
    imagedb["actions"]["movingleft"]  = []
    imagedb["actions"]["movingright"] = []
    imagedb["actions"]["idle"]        = []
    imagedb["actions"]["cutting"]     = []
    imagedb["actions"]["watering"]    = []
    imagedb["actions"]["gethit"]      = []

    for i in range(4) :    
        imagedb["actions"]["movingleft"] .append(getSprite(persoActions, i, 0, 225, 225))
        imagedb["actions"]["movingright"].append(getSprite(persoActions, i, 1, 225, 225))
    
    for i in range(2) :
        imagedb["actions"]["idle"]    .append(getSprite(persoActions, i, 2, 225, 225))
        imagedb["actions"]["cutting"] .append(getSprite(persoActions, i, 3, 225, 225))
        imagedb["actions"]["watering"].append(getSprite(persoActions, i, 4, 225, 225))
        imagedb["actions"]["gethit"]  .append(getSprite(persoActions, i, 5, 225, 225))

def getSprite(img, x, y, w=32, h=32) :

    return img.subsurface((x*w, y*h, w, h))


