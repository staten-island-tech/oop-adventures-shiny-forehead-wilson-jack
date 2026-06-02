import random

def storm(self):
    self.__energy -= 10
    self.__health -= 5
    print("A storm hits!")
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
def message_in_a_bottle(self):
     self.__happy += 10
     print("You spot a message in a bottle drifting to shore. Hopeful, you retrieved it and uncrumpled the piece of paper. 'I like trains...' While stupid and unhelpful as it is, you couldn't help but giggle.")
def quicksand(self):
     print()
     print("You stepped into quicksand!")
     print("1. Panic")
     print("2. Wiggle your feet, distribute your body weight, and slowly get to solid ground")
     choice = input("what do you do (1/2): ")
     if choice == "1":
          self.energy -= 15
          print("You panicked, and you've exhausted much of your energy escaping the quicksand.")
     elif choice == "2":
          if random.choice([True, False]): self.happy += 5
          print("Phew. You escaped the quicksand safe and sound.")

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
    roll = random.randint(1,100)
    if roll <= 10:
         self.storm()
    elif roll <= 30:
         self.find_food()
    elif roll <= 35:
         self.get_sick()
    elif roll <= 40:
         self.quicksand()
    elif roll <= 65:
         self.perfect_weather()
    elif roll <= 75:
         self.message_in_a_bottle()
    elif roll <= 90:
         self.wild_beast()
         
    """ events = [self.storm, self.find_food, self.get_sick, self.perfect_weather, self.message_in_a_bottle, self.wild_beast, self.supply_crate]
    event = random.choice(events)
    event() """