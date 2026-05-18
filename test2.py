import random

random.randint

def storm(self):
    self.__energy -= 10
    self.__health -= 5
    print("A storm hits!")
def heavy_storm(self):
    self.__energy -= 20
    self.__health -= 10
    print("A heavy storm hits!")
def find_food(self):
    self.__hunger -= 15
    self.__happy += 5
    print("You found some food! It's not much, but, you're content with it.")
def get_sick(self):
    self.__health -= 15
    self.__mood -= 15
    print("Your immune system was compromised. Yes, you got sick...")
def perfect_weather(self):
    self.__happy += 15
    print("Perfect weather today. Somehow, you feel hopeful already.")


          

     


def supply_crate(self):
    print()
    print("You spot a supply crate in the near distance. You head over and see many supplies instide")
    print("1. Bandages")
    print("2. Bottle of water")
    print("3. Comedy Book")
    print("4. Spear")
    print("5. Can of Beans")
     

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
         if random.choice([True, False]): self.__happy += 20
         print("You scared it off! You feel like a survivor.")
    else:
         self.__health -= 20
         self.__happy -= 10
         print("The boar tackled you! Ouch...")

def random_event(self):
    events = [self.storm, self.find_food, self.get_sick, self.perfect_weather, self.wild_beast]
    event = random.choice(events)
    event()