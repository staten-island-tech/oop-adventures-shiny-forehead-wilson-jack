import random

class Starter:
    def __init__(self, name, health, coins):
        self.name = name
        self.health = health
        self.coins = coins
    

class NPC(Starter):
    def __init__(self,name,health, coins):
        super().__init__(name, health, coins)
    



class Deserted(Starter):
    def __init__(self, name, happy, hunger, inventory, thrist, energy, mood, health, coins):
        super().__init__(name, health, coins)
        self.__happy = happy
        self.__hunger = hunger
        self.__inventory = []
        self.__thrist = thrist
        self.__energy = energy
        self.__mood = mood
    
    def rich(self):
        richer = input("Do You Want To Shovel For Coins?").lower()
        if richer == "yes":
            self.coins += random.randint(1,20)


    
    def newnumber(self):
        return random.randint(20,50)

    def water(self):
        self.__thrist += self.newnumber()
        self.__energy += random.randint(5,15)
        self.__happy += self.newnumber()
        self.health += random.randint(1,10)

    def feeling(self):
        if self.__thrist < 25 and self.__energy < 25 and self.__happy < 25 and self.health < 25:
            print("Near Death")
        elif self.__thrist < 50 and self.__energy < 50 and self.__happy < 50 and  self.health < 50:
            print("Depressed")
        elif self.__thrist > 50 and self.__energy > 50 and self.__happy > 50 and self.health > 50:
            print("Alright")
    def fishing(self):
        asker = input("Fish?").lower()
        if asker == "yes":
            self.__energy += self.newnumber()
            self.__happy += self.newnumber()
            self.health += self.newnumber()
            self.__hunger += self.newnumber()
    def storm(self):
        self.__energy -= 10
        self.health -= 5
        print("A storm hits!")
    def heavy_storm(self):
        self.__energy -= 20
        self.health -= 10
        print("A heavy storm hits!")
    def find_food(self):
        self.__hunger -= 10
        self.__happy += 5
        print("You found some food! It's not much, but, you're content with it.")
    def get_sick(self):
        self.health -= 15
        self.__mood -= 15
        print("Your immune system was compromised. Yes, you got sick...")
    def perfect_weather(self):
        self.__happy += 15
        print("Perfect weather today. Somehow, you feel eventful already.")

    def random_event(self):
        events = [self.storm, self.heavy_storm, self.find_food, self.get_sick, self.perfect_weather]
        event = random.choice(events)
        event()
    def wild_beast(self):
        print()
        print("A wild boar charges out from the forest!")
        print("1. Hide (costs energy, but you're safe)")
        print("2. Confront it (Risks injury, but might gain happiness)")
        choice = input("What do you do? (1/2):")
        if choice == "1":
            self.__energy -= 15
            print("You dove into the thick brush. You're exhausted, but safe.")
        elif choice == "2":
            if random.choice([True, False]): self.__happy += 20
            print("You scared it off! Your Ego Is Massive NOW")
        else:
            self.health -= 20
            self.__happy -= 10
            print("The boar tackled you! Ouch...")
    def market(self ):
        consumer = input("Do You Want To Buy From Store??? ").lower()
        if consumer == "yes":
            print(store)
        store = {
        1 : {"name": "Sword", "description": "Heavy and deals damage", "Coins": 10},
        2 : {"name": "Water Bottle", "description": "Refreshing", "Coins": 5}, 
        3 : {"name": "Shovel", "description": "Dig for treasure","Coins": 0}, 
        4 : {"name": "WW2 Rations", "description": "Food for energy", "Coins": 5},
        5 : {"name": "Energy Drink", "description": "Drink for Energy", "Coins": 3},
        6 : {"name": "Fishing Rod", "description": "Fish for Food", "Coins": 6},
        7 : {"name": "Life Raft", "description": "Escape Boat To FREEDOM", "Coins": 1000}
        }
    def days(self):
        self.__energy -= 10
        self.__thrist -=10
        self.__hunger -= 10
        self.__happy -= 10
        if self.__energy == 0 or self.__thrist == 0 or self.__hunger == 0 or self.__happy == 0:
            return False
        else:
            return True
    def checker(self):
        return self.__health, self.__energy
    
        



name = input("Character Name: ")


player = Deserted(name, happy = random.randint(50,100), hunger = random.randint(30,100), thrist= random.randint(60,100), energy = random.randint(50,100))

if player.checker() < 50:
    print("You started as frail. Good Luck")
else:
    print("You started off as a strong person!!!!!!!!!!!!!!!!!!!!!!z121!!!!!!1")



