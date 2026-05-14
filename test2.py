import random

random.randint

def storm(self):
    self.__energy -= 10
    self.__health -= 5
    print("A storm hits!")
def find_food(self):
    self.__health += 15
    self.__hunger -= 15
    self.__happy += 10
    print("You found some food! It wasn't much, but you gobble it up anyway.")
def get_sick(self):
    self.__health -= 10
    self.__mood -= 15
    self.__happy -= 15
    print("Your immune system was compromised. Yes, you got sick...")
def perfect_weather(self):
    self.__happy += 10
    print("Perfect weather today. Somehow, you feel hopeful already.")
def volcanic_eruption(self):
        self.__health -= 25
        self.__energy -= 25
        self.__happy -= 15
        print("A volcano erupts! The air is thick with suffocating smoke as you rush towards safety.")

def supply_crate(self):
     print()
     print("1. Bandages")
     print("2. Can of beans")
     print("3. Bottle of water")
     print("4. Bag of coins")
     print("5. Spear")
     choice = input("Which items will you take(Max 2)?: ")
     #  COME BACK AGAIN WHEN INVENTORY IS ADDED


def wild_beast(self):
    print()
    print("A wild boar charges out from the forest!")
    print("1. Hide(costs energy, but you're safe)")
    print("2. Confront it (Risks injury, but might gain happiness)")
    choice = input("What do you do? (1/2): ")
    if choice == "1":
            self.__energy -= 15
            print("You dove into the thick brush. You're exhausted, but safe.")
    elif choice == "2":
         if random.choice([True, False]): 
              self.__happy += 20
              print("You scared it off! You feel like a survivor.")
         else:
             self.__health -= 20
             self.__happy -= 10
             print("The boar tackled you!")
    else:
        self.__happy -= 1
        print("The boar wasn't hungry, and lost interest in you. Phew.")

def random_event(self):
    events = [self.storm, self.find_food, self.get_sick, self.perfect_weather, self.volcanic_eruption, self.supply_crate, self.wild_beast]
    event = random.choice(events)
    event()