import random

class Desert:
    def __init__(self, name, happy, hunger, iventory, thrist, energy, mood, health):
        self.name = name
        self.__happy = happy
        self.__hunger = hunger
        self.__inventory = iventory
        self.__thrist = thrist
        self.__energy = energy
        self.__mood = mood
        self.__health = health
    
    def newnumber():
        return random.randint(20,50)

    def water(self):
        self.__thrist += self.newnumber()
        self.__energy += self.newnumber()
        self.__happy += self.newnumber()
        self.__health += self.newnumber()

    def feeling(self):
        if self.__thrist < 25 and self.__energy < 25 and self.__happy < 25 and self.__health < 25:
            print("Near Death")
        elif self.__thrist < 50 and self.__energy < 50 and self.__happy < 50 and  self.__health < 50:
            print("Depressed")
        elif self.__thrist > 50 and self.__energy > 50 and self.__happy > 50 and self.__health > 50:
            print("Alright")
    def fishing(self):
        asker = input("Fish?").lower()
        if asker == "yes":
            self.__energy += self.newnumber
            self.__happy += self.newnumber
            self.__health += self.newnumber
            self.__hunger += self.newnumber



store = [
"Sword": {"name": "Sword", "description": "Heavy and deals damage"},
"Water": {"name": "Water Bottle", "description": "Refreshing"}, 
"Shovel": {"name": "Shovel", "description": "Dig for treasure"}, 
"WW2 Rations": {"name": "WW2 Rations", "description": "Food for energy"},
"Energy Drnk": {"name": "Energy Drink", "description": "Drink for Energy"},
"Fishing Rod": {"name": "Fishing Rod", "description": "Fish for Food"}
]










