import shared

class Character() :

    def __init__(self, pos) :

        self.state = 0
        self.animCooldown = 0
        self.position = 0
        self.positionDest = -1
        self.direction = 0
        self.score = 0
        self.lives = 4
        self.combo = 0
        self.watering = False
        self.wateringSpriteCooldown = 0
        self.wateringSpriteId = 0
        
        self.updateCurrentSprite()

    def render(self) :
        
        w, h = self.currentSprite.get_size()

        shared.game.screen.blit(self.currentSprite,
                                (shared.characterBaseX - w/2 + self.position*shared.flowersSeparation,
                                 shared.characterBaseY - h))

        if (self.watering) :
            shared.game.screen.blit(shared.imagedb["watering"][self.wateringSpriteId],
                                    (shared.flowersBaseX + (self.position-1)*shared.flowersSeparation + 20,
                                     shared.flowersBaseY - 30))


        
    def updateCurrentSprite(self) :

        if (self.positionDest == -1) :
            self.currentSprite = shared.imagedb["char"]["standing"]
            return

        direction = "left" if (self.positionDest - self.position > 0) else "right"
        id = int(abs(self.positionDest - self.position) * 4)
            
        self.currentSprite = shared.imagedb["char"][direction][id]


    def update(self) :

        if (self.watering) :

            self.wateringSpriteCooldown -= 1
            if (self.wateringSpriteCooldown == 0) :
                self.wateringSpriteCooldown = 5
                self.wateringSpriteId += 1
                if (self.wateringSpriteId >= len(shared.imagedb["watering"])) :
                    self.wateringSpriteId = 0

        if (self.positionDest == -1) : return

        direction = 1 if (self.positionDest - self.position > 0) else -1

        self.position += direction / (4*2)
        
        if  (abs(self.positionDest - self.position) <= 0.02) :
            self.position = self.positionDest
            self.positionDest = -1
        
        self.updateCurrentSprite()


    def water(self) :

        if (self.positionDest != -1) : return
        if (self.position == 0) : return
        
        if (self.watering) : 
            self.watering = False
            return

        self.watering = True
        self.wateringSpriteCooldown = 5
        self.wateringSpriteId = 0
        shared.flowers[self.position-1].water() 


    def cut(self) :

        if (self.positionDest != -1) : return
        if (self.position >= shared.numberOfFlowers) : return

        shared.flowers[self.position].cut()


    def move(self, direction) :

        if (self.positionDest != -1) : return
       
        self.watering = False

        self.positionDest = self.position + direction

        if (self.positionDest < 0) or (self.positionDest > shared.numberOfFlowers) :
            self.positionDest = -1


    def addCombo(self) :

        self.combo += 1
        self.score += 100

        if (self.combo >= 4) :
            print("Combo !!")
            self.combo = 0
            self.score += 100


