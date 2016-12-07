import src.shared as shared
import random
import pygame
from pygame.locals import *


maxLives = 4
maxCombo = 3

class Interface() :

    def __init__(self) :

        self.scoreFont = pygame.font.Font("./assets/bitdust2.ttf",32)
        self.scoreText = self.makeScoreText(shared.character.score)
        self.speedUpCooldown = 500
        shared.speedFactor = 1.0

        self.livesAnimCooldown = [  ]
        self.livesSpriteId     = [  ]
        for i in range(maxLives) :
            self.livesAnimCooldown.append(20 + random.randint(-3,3))
            self.livesSpriteId.append(random.randint(0,3))

        self.comboAnimCooldown = [  ]
        self.comboSpriteId     = [  ]
        for i in range(maxCombo) :
            self.comboAnimCooldown.append(20 + random.randint(-3,3))
            self.comboSpriteId.append(random.randint(0,3))

    def update(self) :

        self.scoreText = self.makeScoreText(shared.character.score)

        self.speedUpCooldown -= 1
        if (self.speedUpCooldown <= 0) :
            self.speedUpCooldown = 500
            shared.speedFactor += 0.3

        for i in range(maxLives) :
            self.livesAnimCooldown[i] -= 1
            if (self.livesAnimCooldown[i] == 0) :
                self.livesAnimCooldown[i] = 20 + random.randint(-3,3)
                self.livesSpriteId[i] += 1
                if (self.livesSpriteId[i] >= 3) :
                    self.livesSpriteId[i] = 0

        for i in range(maxCombo) :
            self.comboAnimCooldown[i] -= 1
            if (self.comboAnimCooldown[i] == 0) :
                self.comboAnimCooldown[i] = 20 + random.randint(-3,3)
                self.comboSpriteId[i] += 1
                if (self.comboSpriteId[i] >= 3) :
                    self.comboSpriteId[i] = 0

    def render(self) :

        self.renderScore()
        self.renderLives()
        self.renderCombo()

    def makeScoreText(self, score, insideColor = (255,255,255), outsideColor=(0,0,0)) :

        bs = 3
        textIn   = self.scoreFont.render(str(score), 1, insideColor )
        textOut  = self.scoreFont.render(str(score), 1, outsideColor)
        size = textIn.get_width() + 2*bs, textIn.get_height() + 2*bs
        s = pygame.Surface(size, pygame.SRCALPHA, 32)
        s.blit(textOut,(0,0))    
        s.blit(textOut,(2*bs,2*bs))    
        s.blit(textOut,(2*bs,0))    
        s.blit(textOut,(0,2*bs))    
        s.blit(textIn, (bs,bs))    

        return s

    def renderScore(self) :

        w, h = self.scoreText.get_size()
        shared.game.screen.blit(self.scoreText, (shared.game.width/2 - w/2, 10))

    def renderLives(self) :

        for i in range(shared.character.lives) :
            s = shared.imagedb["indicator"]["life"][self.livesSpriteId[i]]
            w, h = s.get_size()
            shared.game.screen.blit(s, (0 + i*(w-20), 10))

    def renderCombo(self) :

        offset = shared.character.combo * 0.5

        for i in range(shared.character.combo) :
            s = shared.imagedb["indicator"]["combo"][self.comboSpriteId[i]]
            w, h = s.get_size()
            shared.game.screen.blit(s, (shared.game.width/2 + (i - offset) * (w+5), shared.game.height - h - 5))





