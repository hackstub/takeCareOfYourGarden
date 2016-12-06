import shared
import pygame
from pygame.locals import *

class Interface() :

    def __init__(self) :

        self.scoreFont = pygame.font.Font("./assets/bitdust2.ttf",32)
        self.scoreText = self.makeScoreText(shared.character.score)


    def update(self) :

        self.scoreText = self.makeScoreText(shared.character.score)

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
            shared.game.screen.blit(shared.imagedb["life"], (10 + i*20, 10))

    def renderCombo(self) :

        offset = shared.character.combo * 0.5

        for i in range(shared.character.combo) :
            shared.game.screen.blit(shared.imagedb["comboicon"],
                    (shared.game.width/2 + (i - offset) * 70, shared.game.height  - 70))





