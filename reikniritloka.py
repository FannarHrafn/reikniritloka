#Fannar Hrafn Haraldsson
#3.5.19
#lokaverkefni tengt tölvuleiknum League of Legends og að kaupa items inn í leiknum

#stats on items in order: Name, Health, Armor, magic Resistance, Health Regen, Mana Regen, Attack Damage, Attack Speed, Ability power, Mana,
#  Cooldown Reduction, Movement Speed, Passive, Gold Value without Passive, Gold Value with Passive
tier1items = [
    {"name":"ruby crystal","health":150,"gold value":400,"gold cost":400},
    {"name":"Amplifying Tome","ability power":20,"gold value":435,"gold cost":435},
    {"name":"cloth armor","armor":15,"gold value":300,"gold cost":300},
    {"name":"dagger","attack speed":12,"gold value":300,"gold cost":300},
    {"name":"faerie charm","mana-regen":25,"gold value":125,"gold cost":125},
    {"name":"long sword","attack damage":10,"gold value":350,"gold cost":350},
    {"name":"blasting wand","ability power":40,"gold value":870,"gold cost":850},
    {"name":"null-magic mantle","magic resist":25,"gold value":450,"gold cost":450},
    {"name":"pickaxe","attack damage":25,"gold value":875,"gold cost":875},
    {"name":"rejuvenation bead","health-regen":50,"gold value":150,"gold cost":150},
    {"name":"sapphire crystal","mana":250,"gold value":350,"gold cost":350},
    {"name":"stopwatch","gold value":900,"gold cost":600},
    {"name":"B.F. sword","attack damage":40,"gold value":1400,"gold cost":1300}
]

tier2items = [
    {"name":"stinger","recipe":["dagger","dagger"],"attack speed":35,"CDR":10,"gold value":1142,"gold cost":1100},
    {"name":"sheen","recipe":["sapphire crystal"],"mana":250,"CDR":10,"gold value":617,"gold cost":1050},
    {"name":"aegis of the legion","recipe":["null-magic mantle","cloth armor"],"armor":30,"magic resist":30,"gold value":1140,"gold cost":1100},
    {"name":"aether wisp","recipe":["amplifying tome"],"ability power":30,"movement speed":5,"gold value":850,"gold cost":850},
    {"name":"bami's cinder","recipe":["ruby crystal"],"health":200,"gold value":534,"gold cost":900},
    {"name":"bramble vest","recipe":["cloth armor","cloth armor"],"armor":35,"gold value":700,"gold cost":1000},
    {"name":"catalysts of aeons","recipe":["ruby crystal","sapphire crystal"],"health":225,"mana":300,"gold value":1020,"gold cost":1100},
    {"name":"chain vest","recipe":["cloth armor"],"armor":40,"gold value":800,"gold cost":800},
    {"name":"crystalline bracer","recipe":["ruby crystal","rejuvenation bead"],"health":200,"health-regen":50,"gold value":684,"gold cost":650},
    {"name":"fiendish codex","recipe":["amplifying tome"],"ability power":35,"CDR":10,"gold value":1028,"gold cost":900},
    {"name":"forbidden idol","recipe":["faerie charm","faerie charm"],"CDR":10,"HNS power":5,"mana-regen":50,"gold value":800,"gold cost":800},
    {"name":"giant's belt","recipe":["ruby crystal"],"health":380,"gold value":1014,"gold cost":1000},
    {"name":"glacial shroud","recipe":["sapphire crystal","cloth armor"],"armor":20,"CDR":10,"mana":250,"gold value":1017,"gold cost":900},
    {"name":"haunting guise","recipe":["ruby crystal","amplifying tome"],"ability power":35,"health":200,"gold value":1294,"gold cost":1500},
    {"name":"hextech revolver","recipe":["amplifying tome","amplifying tome"],"ability power":40,"gold value":870,"gold cost":1050},
    {"name":"jaurim's  fist","recipe":["long sword","ruby crystal"],"attack damage":15,"health":200,"gold value":1058,"gold cost":1200},
    {"name":"kindlegem","recipe":["ruby crystal"],"CDR":10,"health":200,"gold value":800,"gold cost":800},
    {"name":"negatron cloak","recipe":["null-magic mantle"],"magic resist":40,"gold value":720,"gold cost":720},
    {"name":"oblivion orb","recipe":["ruby crystal","amplifying tome"],"ability power":20,"health":200,"magic pen":15,"gold value":1435,"gold cost":1600},
    {"name":"phage","recipe":["ruby crystal","long sword"],"attack damage":15,"health":200,"gold value":1778,"gold cost":1250},
    {"name":"raptor cloak","recipe":["rejuvenation bead","cloth armor"],"armor":30,"health-regen":125,"gold value":1765,"gold cost":900},
    {"name":"seeker's armguard","recipe":["cloth armor","amplifying tome","cloth armor"],"ability power":20,"armor":30,"gold value":1661,"gold cost":1100},
    {"name":"serrated dirk","recipe":["long sword","long sword"],"attack damage":25,"lethality":10,"gold value":1100,"gold cost":1100},
    {"name":"spectre's cowl","recipe":["ruby crystal","null-magic mantle"],"health":250,"magic resist":25,"gold value":1567,"gold cost":1200},
    {"name":"tiamat","recipe":["long sword","rejuvenation bead","long sword"],"attack damage":25,"health-regen":50,"gold value":1025,"gold cost":1325},
    {"name":"warden's mail","recipe":["cloth armor","cloth armor"],"armor":40,"gold value":800,"gold cost":1000}
]

tier3items = [
    {"name":"abyssal mask","recipe":["catalyst of aeons","negatron cloak"],"CDR":10,"health":350,"magic resist":55,"mana":300,"gold value":2610,"gold cost":3000},
    {"name":"adaptive helm","recipe":["null-magic mantle","spectre's cowl","rejuvenation bead"],"CDR":10,"health":350,"health-regen":100,"magic resist":55,"gold value":2490,"gold cost":2800},
    {"name":"dead man's plate","recipe":["chain vest","giant's belt"],"armor":60,"health":425,"gold value":3053,"gold cost":2900},
    {"name":"edge of night","recipe":["pickaxe","serrated dirk","ruby crystal"],"attack damage":55,"health":250,"gold value":2997,"gold cost":3000},
    {"name":"frozen heart","recipe":["warden's mail","glacial shroud"],"armor":100,"CDR":20,"mana":400,"gold value":3093,"gold cost":2700},
    {"name":"frozen mallet","recipe":["jaurim's fist","giant's belt"],"attack damage":30,"health":700,"gold value":2917,"gold cost":3100},
    {"name":"gargoyle stoneplate","recipe":["chain vest","stopwatch","negatron cloak"],"armor":40,"magic resist":40,"gold value":3040,"gold cost":2500},
    {"name":"guardian angel","recipe":["B.F. sword","chain vest","stopwatch"],"armor":40,"attack damage":45,"gold value":2375,"gold cost":2800},
    {"name":"hextech protobelt-01","recipe":["hextech revolver","kindlegem"],"ability power":60,"CDR":10,"health":300,"gold value":2372,"gold cost":2500},
    {"name":"iceborn gauntlet","recipe":["sheen","glacial shroud"],"armor":65,"CDR":20,"mana":500,"gold value":2533,"gold cost":2700},
    {"name":"knight's vow","recipe":["kindlegem","chain vest"],"armor":40,"CDR":10,"health":250,"gold value":2725,"gold cost":2200},
    {"name":"liandry's torment","recipe":["haunting guise","blasting wand"],"ability power":75,"health":300,"gold value":2431,"gold cost":3100},
    {"name":"locket of the iron solari","recipe":["aegis of the legion","null-magic mantle"],"armor":30,"magic resist":60,"gold value":1680,"gold cost":2200},
    {"name":"morellonomicon","recipe":["oblivion orb","blasting wand"],"ability power":70,"health":300,"gold value":2789,"gold cost":3000},
    {"name":"ohmwrecker","recipe":["raptor cloak","kindlegem"],"armor":50,"CDR":10,"health":300,"health-regen":150,"gold value":3340,"gold cost":2650},
    {"name":"randuin's omen","recipe":["warden's mail","giant's belt"],"armor":60,"health":400,"gold value":2267,"gold cost":2900},
    {"name":"redemption","recipe":["forbidden idol","crystalline bracer"],"CDR":10,"HNS power":10,"health":200,"health-regen":50,"mana-regen":150,"gold value":2267,"gold cost":2100},
    {"name":"righteous glory","recipe":["glacial shroud","crystalline bracer"],"armor":30,"CDR":10,"health":400,"health-regen":100,"mana":300,"gold value":5616,"gold cost":2650},
    {"name":"rod of ages","recipe":["catalyst of aeons","blasting wand"],"ability power":100,"health":500,"mana":100,"gold value":4068,"gold cost":2700},
    {"name":"rylai's crystal scepter","recipe":["blasting wand","amplifying tome","ruby crystal"],"ability power":90,"health":300,"gold value":2757,"gold cost":2600},
    {"name":"shurelya's reverie","recipe":["kindlegem","aether wisp","faerie charm"],"ability power":40,"CDR":10,"health":200,"mana-regen":100,"gold value":3947,"gold cost":2250},
    {"name":"spear of shojin","recipe":["B.F. sword","kindlegem","long sword"],"attack damage":60,"CDR":20,"health":250,"gold value":4550,"gold cost":3400},
    {"name":"spirit visage","recipe":["kindlgem","spectre's cowl"],"CDR":10,"health":450,"health-regen":100,"magic resist":55,"gold value":2937,"gold cost":2800},
    {"name":"sterak's gage","recipe":["jaurim's fist","pickaxe","ruby crystal"],"health":450,"gold value":2976,"gold cost":3200},
    {"name":"sunfire cape","recipe":["bami's cinder","ruby crystal","chain vest"],"armor":60,"health":425,"gold value":2333,"gold cost":2750},
    {"name":"the black cleaver","recipe":["phage","kindlegem"],"attack damage":40,"CDR":20,"health":400,"gold value":3000,"gold cost":3000},
    {"name":"thornmail","recipe":["bramble vest","ruby crystal","warden's mail"],"armor":80,"health":250,"gold value":2267,"gold cost":2900},
    {"name":"titanic hydra","recipe":["tiamat","ruby crystal","jaurim's fist"],"attack damage":40,"health":450,"health-regen":100,"gold value":3500,"gold cost":3500},
    {"name":"trinity force","recipe":["stinger","sheen","phage"],"attack damage":25,"attack speed":40,"CDR":20,"health":250,"movement speed":5,"mana":250,"gold value":4342,"gold cost":3733},
    {"name":"warmog's armor","recipe":["giant's belt","kindlegem","crystalline bracer"],"CDR":10,"health":800,"health-regen":200,"gold value":3000,"gold cost":2850},
    {"name":"zeke's convergence","recipe":["aegis of the legion","glacial shroud"],"armor":60,"CDR":10,"magic resist":30,"mana":250,"gold value":2357,"gold cost":2250},
    {"name":"zhonya's hourglass","recipe":["seeker's armguard","stopwatch","fiendish codex"],"ability power":75,"armor":45,"CDR":10,"gold value":3098,"gold cost":2900},
    {"name":"zz'rot portal","recipe":["raptor cloak","negatron cloak"],"armor":55,"health-regen":125,"magic resist":55,"gold value":3255,"gold cost":2700}
]
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

    def calcEffHP(self,extraHealth = 0,extraArmor = 0):
        return float((1 + (self.currArmor + extraArmor)/100) * (self.currHealth + extraHealth))

    def findPursuit(self,items):
        currentPursuit = items[0]
        for x in items:
            if currentPursuit.calcEffHP(self,currentPursuit["health"],currentPursuit["armor"]) < x.calcEffHP(self,x["health"],x["armor"]) and x not in self.inventory:
                currentPursuit = x
        return currentPursuit

    def findItems(self,list):
        shoppingList = []
        for x in list:
            if x in tier2items:
                for z in tier2items:
                    if z["name"] == x:
                        shoppingList.append(z)
            else:
                for z in tier1items:
                    if z["name"] == x:
                        shoppingList.append(z)
        return shoppingList

    def tier3Shopper(self):
        if len(self.inventory) != 6 and self.gold > 150:
            #find item to pursue
            self.pursuit = findPursuit(self,tier3items)
            #buy pursuit item if possible
            if self.gold >= self.pursuit["gold cost"]:
                self.gold -= self.pursuit["gold cost"]
                self.inventory.append(self.pursuit)
                return tier3Shopper(self)
            else:
                findingList = self.pursuit["recipe"]
                shoppingList = findItems(self,findingList)
                return tier2Shopper(self,shoppingList)

    def tier2Shopper(self,shoppingList):
        if len(self.inventory) !=6 and self.gold > 150:
            #find item to pursue
            self.pursuit = findPursuit(self,shoppingList)
            #buy pursuit if possible
            if self.gold >= self.pursuit["gold cost"]:
                self.gold -= self.pursuit["gold cost"]
                self.inventory.append(self.pursuit)
                shoppingList.remove(self.pursuit)
                return tier2Shopper(self,shoppingList)
            else:
                shoppingList.remove(self.pursuit)

















