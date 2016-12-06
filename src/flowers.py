import shared
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
        self.nextStepCooldown = 50
        self.stemAnimCooldown = 20
        self.stemSprite = 0
        self.flowerType = "neutral"
        self.status = "growing"

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

        wHead,   hHead   = currentHead.get_size()
        shared.game.screen.blit(currentHead,
                                (shared.flowersBaseX - wHead/2 + self.position*shared.flowersSeparation,
                                 shared.flowersBaseY - hHead - 50*(self.height-1)))


    def update(self) :
        
        self.stemAnimCooldown -= 1
        if (self.stemAnimCooldown <= 0) :
            self.stemAnimCooldown = 20
            self.stemSprite += 1
            if (self.stemSprite >= 2) :
                self.stemSprite = 0

        #if (shared.character.watering) and (shared.character.position == self.position+1) :
        #   self.evolveCooldown -= 2
        #   if (self.state == 5) and (self.evolveCooldown <= 1) :
        #       shared.character.addCombo()

        if (self.status != "grown") :
            self.nextStepCooldown -= 1

        if (self.nextStepCooldown <= 0) :
            self.step += 1
            if ((self.status == "growing") and (self.step >= self.evolveStep)) :
                self.nextStepCooldown = 10000 + random.randint(-10,10)
                self.face = random.randint(0,2)
                flowerType = [ "good", "evil" ]
                self.flowerType = flowerType[random.randint(0,1)] 
                self.status = "grown"
            elif (self.status == "poping") :
                self.nextStepCooldown = 5
            else :
                self.nextStepCooldown = 50 + random.randint(-5,5)

            if (self.status == "poping") and (self.step >= len(shared.imagedb["flowersPop"][self.flowerType])) :
                self.regen()
                return
            if (self.status == "growing") :
                self.height += 1

    def water(self) :
        
        if (self.flowerType == "neutral") :
            return
        if (self.flowerType == "good") :
            shared.character.addCombo()
        print("("+str(self.position)+") I iz being watered <3")
        self.nextStepCooldown = 10 
        self.status = "poping"
        self.step = 0

    def cut(self) :

        print("("+str(self.position)+") I iz being cut emaged !")
