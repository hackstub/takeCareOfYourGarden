import src.shared as shared
import random

class Flower() :

    def __init__(self, pos) :

        self.position = pos
        self.regen()

    def regen(self) :
        
        self.step = 0
        self.height = 0
        self.stems = []
        for i in range(6) :
            self.stems.append(random.randint(0,3))
        self.evolveStep = random.randint(2,5)
        self.face = random.randint(0,2)
        self.nextStepCooldown = int(50 / shared.speedFactor)
        self.stemAnimCooldown = int(20 / shared.speedFactor)
        self.stemSprite = 0
        self.flowerType = "neutral"
        self.status = "growing"
    
    def evolve(self) :

        self.nextStepCooldown = int((200 + random.randint(-5,5)) / shared.speedFactor)
        self.face = random.randint(0,2)
        self.flowerType = ["good", "evil"][random.randint(0,1)] 
        self.status = "grown"
    
    def render(self) :

        for i in range(self.height) :
            stemId = self.stems[i]
            stem = shared.imagedb["stems"][self.stemSprite][stemId]

            wSprite, hSprite = stem.get_size()
            
            shared.game.screen.blit(stem,
                                    (shared.flowersBaseX - wSprite/2 + self.position*shared.flowersSeparation,
                                     shared.flowersBaseY - (i + 1) * hSprite))
        
        if (self.status in ["growing", "grown"]) :
            currentHead   = shared.imagedb["flowersHead"][self.flowerType][self.face]
        elif (self.status == "poping") :
            currentHead   = shared.imagedb["flowersPop"][self.flowerType][self.step]
        elif (self.status != "grown") :
            currentHead   = shared.imagedb["flowersDead"][self.flowerType]

        wHead,   hHead   = currentHead.get_size()
        shared.game.screen.blit(currentHead,
                                (shared.flowersBaseX - wHead/2 + self.position*shared.flowersSeparation,
                                 shared.flowersBaseY - hHead - 50*(self.height-1)))


    def update(self) :
       
        # Stems animation
        self.stemAnimCooldown -= 1
        if (self.stemAnimCooldown <= 0) :
            self.stemAnimCooldown = int(20 + random.randint(-2,2) / shared.speedFactor)
            self.stemSprite += 1
            if (self.stemSprite >= 2) :
                self.stemSprite = 0

        
        self.nextStepCooldown -= 1

        if (self.nextStepCooldown <= 0) :

            if  (self.status == "grown") :
                self.nextStepCooldown = int(50 / shared.speedFactor)
                self.status = "dying"
                shared.character.badAction()
                return
            elif (self.status == "growing") :
                self.nextStepCooldown = int((50 + random.randint(-5,5)) / shared.speedFactor)
                self.step += 1
                self.height += 1
                if (self.step >= self.evolveStep) : 
                    self.evolve()
                return
            elif (self.status == "poping") :
                self.step += 1
                self.nextStepCooldown = 5
                if (self.step >= len(shared.imagedb["flowersPop"][self.flowerType])) :
                    self.regen()
                return
            elif (self.status == "dying") :
                self.nextStepCooldown = int((50 + random.randint(-5,5)) / shared.speedFactor)

                self.step -= 1
                self.height -= 1
                if (self.step <= 0) :
                    self.regen()
                return


    def water(self) :

        if (self.status != "grown") :
            return
        
        if (self.flowerType == "good") :
            self.nextStepCooldown = 10
            self.status = "poping"
            self.step = 0
            shared.character.goodAction()
        elif (self.flowerType == "evil") : 
            self.nextStepCooldown = int(50  / shared.speedFactor)
            self.status = "dying"
            shared.character.badAction()

    def cut(self) :
        
        if (self.status != "grown") :
            return

        if (self.flowerType == "evil") :
            self.nextStepCooldown = 10
            self.status = "poping"
            self.step = 0
            shared.character.goodAction()
        elif (self.flowerType == "good") : 
            self.nextStepCooldown = int(50  / shared.speedFactor)
            self.status = "dying"
            shared.character.badAction()


