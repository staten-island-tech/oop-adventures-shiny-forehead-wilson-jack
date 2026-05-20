import random

""" random.randint """

def storm(self):
    self.__energy -= 10
    self.__health -= 5
    print("A storm hits!")
def heavy_storm(self):
    self.__energy -= 20
    self.__health -= 10
    print("A heavy storm hits!")
def find_food(self):
    self.__hunger -= 20
    self.__energy += 20
    self.__happy += 10
    print("You found some food! It wasn't much, but, you ate it anyway.")
def get_sick(self):
    self.__health -= 10
    self.__happy -= 10
    print("Your immune system was compromised! Yes, you got sick...")
def perfect_weather(self):
    self.__happy += 15
    print("Perfect weather today. Somehow, you feel hopeful already.")


          

     


def supply_crate(self):
    print()
    print("You spot a supply crate in the near distance. You head over and see many supplies inside.")
    print("1. Bandages")
    print("2. Bottle of water")
    print("3. Comedy Book")
    print("4. Spear")
    print("5. Can of Beans")
    choice = input("Choose a maximum of 2 items.")
     

def wild_beast(self):
    print()
    print("A wild boar charges out from the forest!")
    print("1. Hide(costs energy, but you'll be safe)")
    print("2. Confront it (Risks injury, but maybe you could scare it off.)")
    choice = input("What do you do? (1/2): ")
    if choice == "1":
            self.__energy -= 10
            print("You dove into the thick brush. You're exhausted, but safe.")
    elif choice == "2":
         if random.choice([True, False]): self.__happy += 20
         print("You scared it off! You feel like a survivor.")
    else:
         self.__health -= 20
         print("The boar was not intimidated. It tackled you!")

def random_event(self):
    events = [self.storm, self.find_food, self.get_sick, self.perfect_weather, self.wild_beast, self.supply_crate]
    event = random.choice(events)
    event()