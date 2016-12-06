import shared
import pygame
import sys

class Character() :

    def __init__(self, pos) :

        self.state = 0
        self.animCooldown = 0
        self.position = 0
        self.positionDest = -1
        self.direction = 0
        self.score = 0
        self.lives = 3
        self.combo = 0
        self.action = "idle"
        self.actionSpriteCooldown = 30
        self.actionSpriteId = 0
        
        #self.updateCurrentSprite()

    def render(self) :
        
        if (self.action != "moving") :
            s = shared.imagedb["actions"][self.action][self.actionSpriteId]
            w, h = s.get_size()
            shared.game.screen.blit(s,
                                    (shared.characterBaseX - w/2 + self.position*shared.flowersSeparation,
                                     shared.characterBaseY - int(h*0.83)))
        else :
            s = self.currentSprite 
            w, h = s.get_size()
            shared.game.screen.blit(s,
                                    (shared.characterBaseX - w/2 + self.position*shared.flowersSeparation,
                                     shared.characterBaseY - h))

        
    def updateCurrentSprite(self) :

        if (self.positionDest == -1) :
            #self.currentSprite = shared.imagedb["char"]["standing"]
            return

        direction = "left" if (self.positionDest - self.position > 0) else "right"
        id = int(abs(self.positionDest - self.position) * 4)
            
        self.currentSprite = shared.imagedb["char"][direction][id]


    def update(self) :

        self.actionSpriteCooldown -= 1
        if (self.actionSpriteCooldown == 0) :
            self.actionSpriteId += 1
            if (self.actionSpriteId >= 2) :
                self.actionSpriteId = 0
                if (self.action != "idle") :
                    self.action = "idle"
            
            if (self.action == "idle") :
                self.actionSpriteCooldown = 30
            else :
                self.actionSpriteCooldown = 10

        if (self.positionDest == -1) : return

        direction = 1 if (self.positionDest - self.position > 0) else -1

        self.position += direction / (4*2)
        
        if  (abs(self.positionDest - self.position) <= 0.02) :
            self.position = self.positionDest
            self.positionDest = -1
            self.action = "idle"
        
        self.updateCurrentSprite()


    def water(self) :

        if (self.positionDest != -1) : return
        if (self.position == 0) : return
        if (self.action != "idle") : return

        self.action = "watering"
        self.actionSpriteCooldown = 10
        self.actionSpriteId = 0
        shared.flowers[self.position-1].water() 


    def cut(self) :

        if (self.positionDest != -1) : return
        if (self.position >= shared.numberOfFlowers) : return
        if (self.action != "idle") : return
 
        self.action = "cutting"
        self.actionSpriteCooldown = 10
        self.actionSpriteId = 0

        shared.flowers[self.position].cut()


    def move(self, direction) :

        if (self.action != "idle") : return
        if (self.positionDest != -1) : return
       
        self.action = "moving"

        self.positionDest = self.position + direction

        if (self.positionDest < 0) or (self.positionDest > shared.numberOfFlowers) :
            self.positionDest = -1


    def goodAction(self) :

        self.combo += 1
        self.score += 20

        if (self.combo >= 4) :
            self.combo = 0
            self.score += 100
            self.lives += 1
            if (self.lives > 4) :
                self.lives = 4

    def badAction(self) :

        self.combo = 0
        self.score -= 30
        self.lives -= 1

        if (self.lives <= 0) :
            print("Lost with score of "+str(self.score))
            pygame.quit()
            sys.exit(0)



