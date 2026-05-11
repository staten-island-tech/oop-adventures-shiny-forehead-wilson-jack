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



store = [
    "Sword": {"name": "Sword", "description": "Heavy and deals damage"},
    "Water": {"name": "Water Bottle", "description": "Refreshing"},

]
print[store]["name"]






#coins = 10 

'''while True: ##### We are gonna use a while statement. If user coins = 0. Break'''


'''window = tk.Tk()
window.title("Blackjack")
window.geometry("400x300")
window.resizable(False,False)

header = tk.Label(window, text = "BLACKJACK", font = 100)
header.pack(pady = 10)


btn = tk.Button(window, text = "Stand", font = 50)
btn.pack(side="bottom",padx=50)
btn = tk.Button(window, text="Hit", font = 50)
btn.pack(side="bottom",padx=50)
btn.pack()
window.mainloop()'''


