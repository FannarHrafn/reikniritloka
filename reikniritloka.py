#Fannar Hrafn Haraldsson
#3.5.19
#lokaverkefni tengt tölvuleiknum League of Legends og að kaupa items inn í leiknum

#stats on items in order: Name, Health, Armor, magic Resistance, Health Regen, Mana Regen, Attack Damage, Attack Speed, Critical Strike Chance, Ability power, Mana,
#  Cooldown Reduction, Movement Speed, Passive, Gold Value without Passive, Gold Value with Passive

itemsInShop = []

def itemShop(gold,baseHealth,baseArmor,inventory):

    def __init__(self):
        self.inventory = inventory
        self.gold = gold
        self.baseHealth = float(baseHealth)
        self.currHealth = float(baseHealth)
        self.baseArmor = float(baseArmor)
        self.currArmor = float(baseArmor)
        self.baseEffHP = float((1 + self.baseArmor/100) * self.baseHealth)
        self.currEffHP = float((1 + self.baseArmor/100) * self.baseHealth)

    def calcEffHP(self,extraHealth,extraArmor):
        return float((1 + (self.currArmor + extraArmor)/100) * (self.currHealth + extraHealth))

    #min money to buy anything assuming already owning atleast one ruby crystal is buying a crystalline bracer for 100 + 150 for buying rejuvination bead
    def smartShopper(self):
        if len(self.inventory) == 0:
            if calcEffHP(self,150,0) > calcEffHP(self,0,15):
                self.gold -= 400
                #self.inventory.append(ruby crystal)
            else:
                self.gold -= 300
                #self.inventory.append(cloth armor)
        elif

