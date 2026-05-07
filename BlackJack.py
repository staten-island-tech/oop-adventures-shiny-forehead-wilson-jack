import requests
import tkinter as tk
import random

#url = https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1

'''class BlackJack:
    def __init__(self, value, suit):
        self.value = value
        self. suit = suit'''

        





#coins = 10 

'''while True: ##### We are gonna use a while statement. If user coins = 0. Break'''


window = tk.Tk()
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
window.mainloop()


