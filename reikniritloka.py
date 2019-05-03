#Fannar Hrafn Haraldsson
#3.5.19
#lokaverkefni tengt tölvuleiknum League of Legends og að kaupa items inn í leiknum


def itemShop(gold,baseHealth,baseArmor,baseResist):

    def __init__(self):
        self.gold = gold
        self.baseHealth = baseHealth
        self.baseArmor = baseArmor
        self.baseResist = baseResist
        self.currArmor = self.baseArmor
        self.currResist = self.baseResist
        self.baseEffArmorHP = self.baseHealth + self.baseHealth * (self.baseArmor/self.baseHealth)
        self.baseEffResistHP = self.baseHealth + self.baseHealth * (self.baseResist/self.baseHealth)
        self.currEffArmorHP = self.baseEffArmorHP
        self.currEffResistHP = self.baseEffResistHP

    def compareArmorHP(self):

