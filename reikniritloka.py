#Fannar Hrafn Haraldsson
#3.5.19
#lokaverkefni tengt tolvuleiknum League of Legends og ad kaupa items inn i leiknum

#All items that build into items relevent to the program I.E. items that build into tier 3 items that have either health, armor or both
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
#where the magic happens
class itemShop:
    #construct a class object with everything needed to calculate what to buy and gold to spend
    #everything with base is later used to compare before and after shopping
    #everything with curr is actually worked with
    def __init__(self,baseHealth,baseArmor,gold):
        #starts with nothing in inventory
        self.inventory = []
        #gold to spend in shop
        self.basegold = gold
        self.gold = gold
        #starts with dummy pursuit
        self.pursuit = {"name":"default pursuit","recipe":tier3items,"health":0,"armor":0,"gold cost":1000,"gold value":1000}
        #used for when it cant buy more tier 3 items and must resort to buying as much of the recipe for a tier 3 as it can
        self.recipe = []
        #health and armor used to find most effectice health on purchase
        self.baseHealth = baseHealth
        self.currHealth = baseHealth
        self.baseArmor = baseArmor
        self.currArmor = baseArmor
        #gold value to starts at 0,  later used to see how much gold was effectively lost/gained
        self.goldValue = 0
        #effective health, the main purpose of the program is to increase this number as much as it can
        self.baseEffHP = float((1 + self.baseArmor/100) * self.baseHealth)
        self.currEffHP = float((1 + self.baseArmor/100) * self.baseHealth)
    #simple effective health calculator, used to compare items to each other based on which would give more effective health
    #returns the effective health if the item were to be bought
    def calcEffHP(self,extraHealth = 0,extraArmor = 0):
        return (1 + (self.currArmor + extraArmor)/100) * (self.currHealth + extraHealth)
    #used by findPursuit to help it calculate which of two items gives better effective health and returns the better item
    def compareItems(self,currentItem,xItem):
            if self.calcEffHP(currentItem.get("health",0),currentItem.get("armor",0)) < self.calcEffHP(xItem.get("health",0),xItem.get("armor",0)):
                currentItem = xItem
            return currentItem
    #finds the best item to try to buy based on what item would give most effective health and returns it
    def findPursuit(self,items):
        currentPursuit = tier1items[0]
        for x in items:
            #it will keep trying to buy finished tier 3 items as long as it can with the small rule that it cant buy multiple
            #of the same tier 3 item because that would  be very inefficient
            if x in tier3items and x not in self.inventory:
                currentPursuit = self.compareItems(currentPursuit,x)
            #when it runs out of money to buy finished items it will feed findPursuit the recipe of the item
            #it wants to buy but can't so findPursuit finds which of the items in the recipe it should buy first
            elif x["name"] in self.recipe:
                currentPursuit = self.compareItems(currentPursuit,x)
        return currentPursuit
    #recipes for items are kept as a list in the items dictionary that contains the names of the items in its recipe
    #findRecipeItems makes a list of the actual items in the recipe by finding them by their names
    def findRecipeItems(self,list):
        shoppingList = []
        for x in list:
            #Logic dictates that if its using findRecipeItems its doing so because it cant buy more tier3items
            #thus there is no reason to look for the name in tier3items and just check tier1 and tier2
            for y in tier2items+tier1items:
                if y["name"] == x:
                    shoppingList.append(y)
        return shoppingList
    #used to make sure that the program knows when to give up because it cant even buy the lowest cost item in
    #the recipe of whatever tier3 item its currently buying the recipe for
    #returns the gold needed to buy the cheapest  item in the recipe
    def minGoldForRecipe(self):
        minGold = 0
        #if there is nothing in the recipe then it hasn't run out of money for tier3items yet so it sets the bar as 0
        if len(self.recipe) != 0:
            #if it is following a recipe it first finds the actual items  in the recipe
            recipe = self.findRecipeItems(self.recipe)
            #dummy number
            minGold = 10000
            #goes through items in the  recipe
            for x in recipe:
                #compares gold costs of items in recipe
                minGold = min(x["gold cost"],minGold)
                #also checks if the current item has its own recipe because its a tier2 and compares gold there
                if "recipe" in x.keys():
                    minirecipe = self.findRecipeItems(x["recipe"])
                    for x in minirecipe:
                        minGold = min(x["gold cost"],minGold)
        return minGold
    #the magnum opus of the program, smartShopper actual does all of the smart shopping
    #it buys the best items based on effective health, balancing buying more health or buying more armor
    #it also knows when to stop and save its money
    #simply returns  "good shopping" when its done
    def smartShopper(self,shoppingList):
        #first it must gain access to the shop
        #when it first goes  to the shop it will have nothing in its inventory so it gets in automaticly because of the or statement
        #after that it it will only gain access if it doesn't have a full inventory, has atleast enough gold for the cheapest item in the recipe
        #and for some  added safety it will also be blocked if its doesn't have enough gold for the cheapest item available: faerie charm
        if len(self.inventory) != 6 and self.gold >= self.minGoldForRecipe() and self.gold > 125 or len(self.inventory) == 0:
            #find item to pursue
            self.pursuit = self.findPursuit(shoppingList)
            #buy pursuit item if possible
            if self.gold >= self.pursuit["gold cost"]:
                #if it can buy the pursuit item it subtracs the gold for it and adds the relevant stats to the champion
                self.gold -= self.pursuit["gold cost"]
                self.currHealth += self.pursuit.get("health",0)
                self.currArmor += self.pursuit.get("armor",0)
                self.goldValue += self.pursuit.get("gold value",0)
                self.currEffHP = self.calcEffHP(self.pursuit.get("health",0),self.pursuit.get("armor",0))
                #adds the  item to inventory
                self.inventory.append(self.pursuit)
                #for when its buying from a recipe so that it doesn't buy more than it should
                #it keeps track of what it needs from the recipe
                if self.pursuit["name"] in self.recipe:
                    self.recipe.remove(self.pursuit["name"])
                    #if it finished buying everything it can from the recipe it means it should stop
                    #so that it can eventually in the context of the game save enough gold to finish the item
                    if len(self.recipe) == 0:
                        return "good shopping"
                #calls on itself again to keep buying more items
                return self.smartShopper(shoppingList)
            else:
                #if it can't buy more tier 3 items it falls down here for the first time
                #and makes a new shopping list out of the recipe for  the tier3 item it wanted to buy but couldn't
                #keeps basic recipe here to keep track of what it already has and whats missing
                self.recipe = self.pursuit.get("recipe",[])
                #makes new list of recipe
                findingList = self.pursuit.get("recipe",[])
                #finds the actualy items of the recipe
                newShoppingList = self.findRecipeItems(findingList)
                #starts shopping from only items in the recipe
                return self.smartShopper(newShoppingList)
        else:
            return "good shopping"

#user interface loop
while True:
    #starts by checking if a champion exists or not
    try:
        champion
    #if not it forces user to make one
    except NameError:
        numberInput = 1
        print("Start by making a champion:")
    #else it gives player control over what to do
    else:
        print("------------------------------------")
        print("1: Make a champion object")
        print("2: Print champion statistics")
        print("3: Print inventory")
        print("4: Print items in shop")
        print("5: quit")
        numberInput = int(input("Pick a numer: "))
    #makes a champion by asking user for all the starting stats
    if  numberInput == 1:
        print("------------------------------------")
        print("to make a champion pick its starting health, armor and gold to spend in the shop")
        startingHealth = int(input("Starting Health: "))
        startingArmor = int(input("Starting Armor: "))
        startingGold = int(input("Starting Gold: "))
        #makes champion
        champion = itemShop(startingHealth,startingArmor,startingGold)
        #buys what it can with gold given
        champion.smartShopper(tier3items)
    #prints out all relevant stats of the champion
    elif numberInput == 2:
        print("------------------------------------")
        print("Champion statistics:")
        print("Current Health:",champion.currHealth)
        print("Current Armor:",champion.currArmor)
        print("Current Effective Health:",round(champion.currEffHP,2))
        print("Health gained:",champion.currHealth - champion.baseHealth)
        print("Armor gained:",champion.currArmor - champion.baseArmor)
        print("Effective Health gained:",round(champion.currEffHP - champion.baseEffHP,2))
        print("Gold value gained:",champion.goldValue,"from spending:",champion.basegold - champion.gold,"gold in the shop")
        print("Leftover gold:",champion.gold)
    #prints all items in inventory
    elif numberInput == 3:
        print("------------------------------------")
        print("Champion inventory:")
        for x in champion.inventory:
            print(x["name"])
            print(x)
    #prints all available items in tier order
    elif numberInput == 4:
        print("------------------------------------")
        print("All items in shop:")
        print("Tier 1 items:")
        for x in tier1items:
            print(x["name"])
            print(x)
        print("------------------------------------")
        print("Tier 2 items")
        for x in tier2items:
            print(x["name"])
            print(x)
        print("------------------------------------")
        print("Tier 3 items")
        for x in tier3items:
            print(x["name"])
            print(x)
    #ends the program
    elif numberInput == 5:
        print("------------------------------------")
        print("Program will now end")
        break
    #in case the user submitted something else than 1,2,3,4 or 5
    else:
        print("------------------------------------")
        print("Bad input, only one number in input please")
