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