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
    def storm(self):
        self.__energy -= 10
        self.__health -= 5
        print("A storm hits!")
    def heavy_storm(self):
        self.__energy -= 20
        self.__health -= 10
        print("A heavy storm hits!")
    def find_food(self):
        self.__hunger -= 10
        self.__happy += 5
        print("You found some food! It's not much, but, you're content with it.")
    def get_sick(self):
        self.__health -= 15
        self.__mood -= 15
        print("Your immune system was compromised. Yes, you got sick...")
    def perfect_weather(self):
        self.__happy += 15
        print("Perfect weather today. Somehow, you feel eventful already.")

    def random_event(self):
        events = [self.storm, self.heavy_storm, self.find_food, self,get_sick, self.perfect_weather]
        event = random.choice(events)
        event()


store = [
"Sword": {"name": "Sword", "description": "Heavy and deals damage"},
"Water": {"name": "Water Bottle", "description": "Refreshing"}, 
"Shovel": {"name": "Shovel", "description": "Dig for treasure"}, 
"WW2 Rations": {"name": "WW2 Rations", "description": "Food for energy"},
"Energy Drnk": {"name": "Energy Drink", "description": "Drink for Energy"},
"Fishing Rod": {"name": "Fishing Rod", "description": "Fish for Food"}
]










