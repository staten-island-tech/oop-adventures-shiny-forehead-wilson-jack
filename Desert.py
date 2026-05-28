import random

class Starter:
    def __init__(self, name, health, coins):
        self.name = name
        self.health = health
        self.coins = coins

class NPC(Starter):
    def __init__(self,name,health, coins): #Find way to make this useful ig
        super().__init__(name, health, coins)
    
    def attacked(self):
        rando = random.randint(1,50)
        self.health -= rando
        if rando > 25:
            print("U just got jumped")
        else:
            print("Tiny Damage")
    
class Deserted(Starter):
    def __init__(self, name, happy, hunger,  thrist, energy, mood):
        super().__init__(name, health = 100, coins = 0)
        self.cart = []
        self.__happy = happy
        self.__hunger = hunger
        self.__thrist = thrist
        self.__energy = energy
        self.__mood = mood
    
    def rich(self):
        richer = input("Do You Want To Shovel For Coins?").lower()
        if richer == "yes":
            if self.__energy > 45:
                self.coins += random.randint(1,20)
            else:
                print("Too Weak")
    
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
        if "Fishing Rod" not in self.cart:
            print("Buy a fishing rod.")
            return
        asker = input("Fish? ").lower()
        if asker == "yes":
            self.__energy += self.newnumber()
            self.__happy += self.newnumber()
            self.health += self.newnumber()
            self.__hunger += self.newnumber()
            print("You have decided to fish")
    
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

    def item_use(self):
        if len(self.cart) == 0:
            print("Empty Invnetory")
            return
        print("Inventory",self.cart)
        use = input("What do u want to use??").lower()
        if use not in self.cart:
            print("Not avaiable")
        elif use == "water bottle":
            self.__thrist += 30
            self.cart.remove(use)
            print("Thrist has been quenched")
        elif use == "ww2 rations":
            self.__hunger += 30
            self.cart.remove(use)
            print("Hunger Restored")
        elif use == "energy drink":
            self.__energy += 30
            self.__thrist += 30
            self.cart.remove(use)
            print("Energy and thrist fixed")
        else:
            print("Cant use")

    
    def market(self):

        store = [
         {"name": "Sword", "description": "Heavy and deals damage", "Coins": int(10)},
         {"name": "Water Bottle", "description": "Refreshing", "Coins": 5}, 
         {"name": "Shovel", "description": "Dig for treasure","Coins": 0}, 
         {"name": "WW2 Rations", "description": "Food for energy", "Coins": 5},
         {"name": "Energy Drink", "description": "Drink for Energy", "Coins": 3},
         {"name": "Fishing Rod", "description": "Fish for Food", "Coins": 6},
         {"name": "Life Raft", "description": "Escape Boat To FREEDOM", "Coins": 1000}
        ]

        while True:
            for index, items in enumerate(store):
                print(index, ":", items["name"],"-", "Description:", items["description"], "-", "Cost:", items["Coins"])

            asker = int(input("Buy What?? ")) 
            if self.coins >= store[asker]["Coins"]:
                self.coins -= store[asker]["Coins"]
                self.cart.append(store[asker]["name"])
                print(self.cart)
                print(self.coins)
            else:
                print("You're Too Poor")

            asker = input('Do You Want To Continue??').upper()
            if asker == "NO":
                break

    def days(self):
        self.__energy -= 10
        self.__thrist -=10
        self.__hunger -= 10
        self.__happy -= 10
        if self.health <= 0:
            self.health -= 20
            print(f"{self.name} is near death. -20 health" )
        if self.__hunger <=40:
            self.health -= 5
            print(f"{self.name} is so hungry. -5 health")
        if self.__thrist <=40:
            self.health -= 10
            print(f"{self.name} is so thristy. -10 health")

        self.__happy = max(0, min(100, self.__happy))
        self.__energy = max(0, min(100, self.__energy))
        self.health = max(0, min(100, self.health))
        self.__hunger = max(0, min(100, self.__hunger))
        self.__mood = max(0, min(100, self.__mood))

    def checker(self):
        return self.health, self.__energy
    
    def sleep(self):
        self.__energy += 40
        self.__mood = random.randint(10,30)

    def alive(self):
        if self.health > 0 and self.__energy > 0 and self.__thrist > 0:
            return True
        else:
            return False

    def show_stat(self):
        print(f"---{self.name}'s stats:---")
        print(f"Happy: {self.__happy}")
        print(f"Energy: {self.__energy}")
        print(f"Hunger: {self.__hunger}")
        print(f"Health: {self.health}")
        print(f"Mood: {self.__mood}")
        print(f"Coins: {self.coins}")

    
name = input("Character Name: ")


player = Deserted(name, happy = random.randint(50,100), hunger = random.randint(30,100), thrist= random.randint(60,100), energy = random.randint(50,100), mood = random.randint(40,100))


print("Welcome", name, "your job is to survive this deserted island and escape using the Life Raft")
player.show_stat()
day = 0
if not player.alive():
    print("Frail Character!")
else:
    print("Excellent Character!")

while player.alive():
    print()
    print("-What Would You Like To Do?-")
    print("1 -Fish")
    print("2 -Drink water")
    print("3 -Shovel for coins")
    print("4 -Sleep")
    print("5 -Store")
    print("6 -Stats")
    print("7 - Inventory")
    print("8 - Use item")
    
    while True:
        option = input("What to do? ")
        if option in ["1","2","3","4","5","6","7","8"]:
            break
        print("Not a choice")

    if option == "1":
        player.fishing()
        player.show_stat()
    elif option == "2":
        player.water()
        player.show_stat()
    elif option == "3":
        player.rich()
        player.show_stat()
    elif option == "4":
        player.sleep()
        player.show_stat()
    elif option == "5":
        player.market()
    elif option == "6":
        player.show_stat()
    elif option == "7":
        print("Inventory", player.cart)
    elif option == "8":
        player.item_use()
        player.show_stat()

    else:
        print("Not a chouce")

    if random.randint(1,4) == 4:
        player.random_event()
    if random.randint(1,8) == 6:
        player.wild_beast()

    player.days()
    day += 1
    print("You have survived", day)
    input("Press enter to continue")
    
print(f" {player.name} died... You failed!")
